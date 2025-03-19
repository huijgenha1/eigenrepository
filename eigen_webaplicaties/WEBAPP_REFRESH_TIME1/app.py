from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/time")
def get_time():
    """Geeft de huidige tijd als JSON terug, zodat de pagina kan worden bijgewerkt."""
    return {"time": datetime.datetime.now().strftime("%H:%M:%S")}

#if __name__ == "__main__":
#    app.run(debug=True)
    
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)