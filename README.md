
# **CAN Bus Visualizer**

The **CAN Bus Visualizer** is a web-based tool for uploading and visualizing CAN (Controller Area Network) trace data using a DBC (Database CAN) file. It processes trace files to decode signals and displays the extracted information in a user-friendly interface.

---

## **Features**

- Upload `.dbc` files (CAN Database Files) for decoding.
- Upload `.blf` or other supported CAN trace files.
- Decode signals and present them in a dynamic table.
- Simple and responsive web interface.
- Lightweight backend powered by Flask.

---

## **Getting Started**

Follow these instructions to set up and run the project on your local machine.

### **Prerequisites**

Ensure you have the following installed:

1. **Python 3.7+**
2. **pip** (Python package manager)

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/can-bus-visualizer.git
   cd can-bus-visualizer
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Running the Application**

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Use the interface to upload `.dbc` and `.blf` files and visualize decoded signals.

---

## **Project Structure**

```plaintext
CANBusVisualizer/
├── app.py                  # Main Flask application
├── static/
│   ├── index.html          # Frontend HTML
│   ├── script.js           # JavaScript logic
│   ├── style.css           # Styling
├── uploads/                # Temporary file uploads (auto-created)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
```

---

## **Supported Formats**

- **DBC Files**: CAN database files that define the structure of CAN messages.
- **BLF Files**: Binary Log Files, commonly used for logging CAN traffic.
- Additional trace formats can be added by extending the `load_trace` function.

---

## **Usage**

1. Navigate to the homepage.
2. Upload your `.dbc` file (required) and a `.blf` trace file (or any supported format).
3. Click the "Process Files" button.
4. View the decoded signals in the displayed table.

---

## **Dependencies**

The project uses the following Python libraries:

- **Flask**: For the web backend.
- **cantools**: For parsing and decoding `.dbc` files.
- **python-can**: For processing CAN trace files.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Screenshots**

### **Upload Interface**
![Upload Interface](https://via.placeholder.com/800x400?text=Screenshot+of+Upload+Interface)

### **Decoded Signals Table**
![Decoded Signals](https://via.placeholder.com/800x400?text=Screenshot+of+Decoded+Signals+Table)

---

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**

- [Flask](https://flask.palletsprojects.com/)
- [cantools](https://cantools.readthedocs.io/)
- [python-can](https://python-can.readthedocs.io/)
