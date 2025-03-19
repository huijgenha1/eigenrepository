      // **Functie om gegevens op te halen en de tabel bij te werken**
        function fetchData() {
            fetch("/data")
                .then(response => response.json())
                .then(data => {
                    let tableBody = document.getElementById("dataTable");
                    tableBody.innerHTML = "";  // Huidige inhoud wissen
                    data.forEach(row => {
                        let tr = document.createElement("tr");
                        tr.innerHTML = `<td>${row[0]}</td><td>${row[1]}</td>`;
                        tableBody.appendChild(tr);
                    });
                })
                .catch(error => console.error("Fout bij ophalen van data:", error));
        }