from flask import Flask, request, jsonify, send_from_directory
import os
import can
import cantools
import tempfile

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Ensure uploads folder exists
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Set max file size to 50 MB

@app.route('/')
def serve_index():
    """Serve the main HTML page."""
    return send_from_directory('static', 'index.html')

def load_trace(trace_path):
    """Parse the trace file to extract CAN messages."""
    messages = []
    with can.BLFReader(trace_path) as reader:
        for msg in reader:
            messages.append({
                "timestamp": msg.timestamp,
                "arbitration_id": msg.arbitration_id,
                "data": msg.data
            })
    return messages

def translate_trace(messages, dbc_path):
    """Decode CAN messages using a DBC file."""
    decoded_signals = []
    db = cantools.database.load_file(dbc_path)
    for msg in messages:
        try:
            decoded = db.decode_message(msg["arbitration_id"], msg["data"])
            decoded_signals.append((msg["timestamp"], decoded))
        except KeyError:
            # Ignore messages not defined in the DBC file
            pass
    return decoded_signals

@app.route('/process-files', methods=['POST'])
def process_files():
    """Handle the upload and processing of DBC and trace files."""
    dbc_file = request.files.get('dbc')
    trace_file = request.files.get('trace')

    if not dbc_file or not trace_file:
        return jsonify({"error": "Both DBC and trace files are required."}), 400

    try:
        # Save files temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".dbc") as temp_dbc:
            temp_dbc.write(dbc_file.read())
            dbc_path = temp_dbc.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".blf") as temp_trace:
            temp_trace.write(trace_file.read())
            trace_path = temp_trace.name

        # Process the trace file
        messages = load_trace(trace_path)
        decoded_signals = translate_trace(messages, dbc_path)

        # Format the decoded signals for the frontend
        formatted_signals = []
        for timestamp, signals in decoded_signals:
            for signal_name, value in signals.items():
                formatted_signals.append({
                    "SIGNALS": signal_name,
                    "ID": hex(int(timestamp)),  # Placeholder, replace with actual ID logic if available
                    "VALUE": value
                })

        return jsonify({"decoded_signals": formatted_signals})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'dbc_path' in locals() and os.path.exists(dbc_path):
            os.remove(dbc_path)
        if 'trace_path' in locals() and os.path.exists(trace_path):
            os.remove(trace_path)

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for better performance
