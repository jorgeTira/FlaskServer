from flask import Flask, request
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user = "luis",
                           password = "12345",
                           database = "invernadero")
cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"
@app.route("/login/", methods=['GET'])
def login():
    usuario = request.args.get('usuario')
    passw = request.args.get('password')
    userDB = Usuario(conexion, cursor)
    print(userDB.login(usuario, password))
    return usuario

if __name__=='__main__':
    app.run(debug=True)