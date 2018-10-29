import hashlib

class Usuario:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor              

    def crear (self, usuario, contra, tipo):
        insertar = ("INSERT INTO usuario(correo, password,tipo)\
         VALUES(%s, %s, %s)")
        hash = hashlib.new('sha256',bytes(contra,'utf-8'))
        hash = hash.hexdigest()
        self.cursor.execute(insertar,(usuario, hash, tipo))
        self.conexion.commit()
    def login(self, usuario, contra):
        print(usuario, contra)
        buscar = ("SELECT * FROM usuario WHERE correo = %s AND password = %s ")
        hash = hashlib.new('sha256', bytes(contra, 'utf-8'))
        hash = hash.hexdigest()
        self.cursor.execute(buscar, (usuario, hash))
        resultado = self.cursor.fetchall()
        if resultado:
            return True
        else:
            return False
