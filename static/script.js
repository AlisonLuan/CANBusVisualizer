document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const resultsContainer = document.getElementById('resultsContainer');

    uploadForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const dbcFile = document.getElementById('dbcFile').files[0];
        const traceFile = document.getElementById('traceFile').files[0];

        console.log("DBC File Selected:", dbcFile);
        console.log("Trace File Selected:", traceFile);

        if (!dbcFile || !traceFile) {
            alert('Please select both DBC and trace files.');
            return;
        }

        const formData = new FormData();
        formData.append('dbc', dbcFile);
        formData.append('trace', traceFile);

        // Debugging log
        for (let pair of formData.entries()) {
            console.log(pair[0] + ':', pair[1]);
        }

        try {
            resultsContainer.innerHTML = 'Processing files...';
            const response = await fetch('/process-files', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const data = await response.json();
            console.log("=== FRONTEND DEBUG LOGS ===");
            console.log("API Response Data:", data);

            displayResults(data);
        } catch (error) {
            console.error(`Error during file processing: ${error}`);
            resultsContainer.innerHTML = `<p class="error">${error.message}</p>`;
        }
    });

    function displayResults(data) {
        if (data.error) {
            resultsContainer.innerHTML = `<p class="error">${data.error}</p>`;
            return;
        }

        console.log("Decoded Signals (from API):", data.decoded_signals);

        const table = document.createElement('table');
        const thead = document.createElement('thead');
        thead.innerHTML = `
            <tr>
                <th>Signal</th>
                <th>ID</th>
                <th>Value</th>
            </tr>
        `;
        table.appendChild(thead);

        const tbody = document.createElement('tbody');
        data.decoded_signals.forEach((signal, index) => {
            console.log(`Signal ${index}:`, signal);

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${signal.SIGNALS}</td>
                <td>${signal.ID}</td>
                <td>${signal.VALUE}</td>
            `;
            tbody.appendChild(tr);
        });

        table.appendChild(tbody);
        resultsContainer.innerHTML = '';
        resultsContainer.appendChild(table);
    }
});
