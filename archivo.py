from flask import Flask
from flask import render_template
import MySQLdb
from flask import request
from database import DBHelper

app = Flask(__name__)
diccionario = {}
db = DBHelper()
#db.crearTablalogin()
#db.crearTablaReserva()
#db.insertarlogin()
#db.quemada()
'''
@app.route("/")
def inicio():    
    #retorno = db.leer("demo1")
    #print(retorno)
    #diccionario[retorno[0]] = [retorno[1], retorno[2]]
    print(diccionario)
    return render_template('index.html', dict=diccionario)
'''




@app.route("/tabla")
def index():
    return render_template('../index.html')


@app.route("/", methods=['GET', 'POST'])
def test():

    base = db.todos()

    for item in base:
        diccionario[item[0]] = [item[1], item[2]]

    if request.method == 'GET':
        return render_template("test.html", dict = diccionario)
    elif request.method == 'POST':
        print("HOLAAAAAAAAAAAAAAAA")
        if "user" in request.form:
            print(request.form['id'])
            db.update(request.form['user'], request.form['id'], request.form['estado'])
            print("hola desde el post: " + request.form["user"])
        if "uno" in request.form:
            nombre = request.form['uno']
            try:
                print(nombre)
                if not nombre.isalnum():
                    raise Exception
            except:
                print("Oiga, usted es un desgraciado")
                return render_template("test.html", dict = diccionario)
            db.insertarlogin(request.form['uno'], request.form['dos']) 
            print(request.form['uno'], request.form['dos'])
            #d = {'demo1' : ['liss', 'ocupado'], 'demo2' : ['liss', 'ocupado']}
            return render_template("index.html" , nombre = nombre, dict = diccionario)
        #return '200'
        
        return render_template("test.html", dict = diccionario)

app.run(debug=True, port=8000)
