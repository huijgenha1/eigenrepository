maak een webpagina waarbij je links de invoer kunt doen. Deze komt in de tabel INVOER.
Aan de rechterkant moet dat 2 seconden de invoer getoond worden.
Dat betekent dat als je een invoer doet je deze binnen 2 seconden op hetzelfde scherm ziet.

Dus de webapplicatie app.py applicatie moet een trigger maken die elke 2 seconden een query output op het scherm (html pagina) zet. 
Fase 2: je zou ook kunnen kijken of er verschillen zijn tov de vorige keer, dus een soort check tabel maken. zodra deze anders is tov de vorige keer dan pas de output tonen.


in chatgpt:
Maak een webapplicatie met python die elke 2 seconden een query output (vanuit postgress) op het scherm (html pagina) zet. De query is alles van tabel INVOER.





in de 1e webapp is een html pagina gemaakt die een invoer kan verwerken van 2 inputwaarden.
Deze worden als naam, adres opgeslagen in een postgres database in de tabel INVOER.

Zorg er in deze 2e webapp voor dat er in de html (index) aan de rechterkant de output van de INVOER tabel wordt getoont. (let op aanpassen webapp naar webapp1 (path aanpassingen maken dus)
Hievoor staat in chatgpt het volgende:

from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Databaseconfiguratie (vervang met jouw gegevens)
DB_HOST = "localhost"
DB_NAME = "jouw_database"
DB_USER = "jouw_gebruiker"
DB_PASS = "jouw_wachtwoord"

# Functie om gegevens uit PostgreSQL op te halen
def fetch_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT naam, adres FROM INVOER")  # Pas de query aan naar je behoefte
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        return [("Fout bij ophalen", str(e))]

@app.route('/')
def index():
    data = fetch_data()  # Haal gegevens uit de database
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


-------------------------html
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PostgreSQL Data Weergave</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: space-between;
            padding: 20px;
        }
        .content {
            width: 60%;
        }
        .sidebar {
            width: 35%;
            background-color: #f4f4f4;
            padding: 10px;
            border-left: 2px solid #ccc;
            position: fixed;
            right: 0;
            top: 0;
            height: 100vh;
            overflow-y: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <div class="content">
        <h2>Welkom op de pagina</h2>
        <p>Dit is een voorbeeldpagina waar aan de rechterkant gegevens uit een PostgreSQL-database worden weergegeven.</p>
    </div>
    
    <div class="sidebar">
        <h2>Database Resultaten</h2>
        <table>
            <tr>
                <th>Naam</th>
                <th>Adres</th>
            </tr>
            {% for naam, adres in data %}
            <tr>
                <td>{{ naam }}</td>
                <td>{{ adres }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>


