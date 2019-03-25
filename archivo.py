from flask import Flask
from flask import render_template
import MySQLdb
from flask import request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/tabla")
def index():
    return render_template('index.html')


app.run(debug=True, port=5000)
