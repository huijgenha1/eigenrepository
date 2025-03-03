from flask import Flask, request, render_template, jsonify
import psycopg2

app = Flask(__name__)

# Database instellingen (pas aan naar jouw setup)
DB_CONFIG = {
    "dbname": "postgres_dabatabase_henk",
    "user": "henk",
    "password": "henk01",
    "host": "localhost",
    "port": "5432"
}

def connect_db():
    """Maakt een verbinding met de database en retourneert een cursor."""
    conn = psycopg2.connect(**DB_CONFIG)
    return conn, conn.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    """Verwerkt het formulier en slaat de invoer op in de database."""
    naam = request.form["naam"]
    adres = request.form["adres"]

    conn, cursor = connect_db()
    cursor.execute("INSERT INTO INVOER (naam, adres) VALUES (%s, %s)", (naam, adres))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Data opgeslagen!"})

@app.route("/data")
def get_data():
    """Haalt alle gegevens op uit de database en stuurt ze als JSON."""
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM INVOER")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
