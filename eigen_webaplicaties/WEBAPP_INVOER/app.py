from flask import Flask, render_template, request, redirect, psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Databaseconfiguratie (vervang deze gegevens door je eigen PostgreSQL-instellingen)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://henk:henk01@localhost/postgres_dabatabase_henk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

####################################
########### ophalen query ##########
####################################
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

# opgehaald query verwerken
@app.route('/')
def index():
    data = fetch_data()  # Haal gegevens uit de database
    return render_template('index.html', data=data)

#############################
########### INVOER ##########
#############################
# Database Model
class Invoer1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), nullable=False)
    adres = db.Column(db.String(200), nullable=False)

# Zorg ervoor dat de tabellen bestaan
with app.app_context():
    db.create_all()

# Route voor het tonen van het formulier
@app.route('/')
def index():
    return render_template('index.html')

# Route voor het verwerken van de invoer1
@app.route('/submit', methods=['POST'])
def submit():
    naam = request.form['naam']
    adres = request.form['adres']

    if naam and adres:
        nieuwe_invoer1 = Invoer1(naam=naam, adres=adres)
        db.session.add(nieuwe_invoer1)
        db.session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)