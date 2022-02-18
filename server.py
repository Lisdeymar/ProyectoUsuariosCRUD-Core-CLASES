#from flask import Flask
from usuarios_app import app
from usuarios_app.controladores import controlador_usuarios

#from carpetageneral.carpetaControladores import archivocontroladorNombreTabla.py

if __name__ == "__main__":
    app.run( debug = True )