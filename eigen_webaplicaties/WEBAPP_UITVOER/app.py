from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Databaseconfiguratie (vervang met jouw gegevens)
DB_HOST = "localhost"
DB_NAME = "postgres_dabatabase_henk"
DB_USER = "henk"
DB_PASS = "henk01"

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
        cur.execute("SELECT naam, adres FROM INVOER1")  # Pas de query aan naar je behoefte
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
