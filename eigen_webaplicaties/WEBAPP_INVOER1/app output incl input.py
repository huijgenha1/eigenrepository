from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Databaseconfiguratie (vervang deze gegevens door je eigen PostgreSQL-instellingen)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://henk:henk01@localhost/postgres_dabatabase_henk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
