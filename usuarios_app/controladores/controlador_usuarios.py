from flask import Flask, render_template, request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario


#RUTA 1, la ruta del index OK, falta html
@app.route( '/', methods=['GET'] )
def despliegaRegistroLogin():
    return render_template( "index.html" )

#Ruta 1A POST insertas información y click, redirecciona a ruta 2
@app.route( '/registroUsuario', methods=["POST"] )
def registrarUsuario():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    session["nombre"] = request.form["nombre"]
    session["apellido"] = request.form["apellido"]
    resultado = Usuario.agregaUsuario( nuevoUsuario )
    print( "Resultado", resultado )
    return redirect( '/dashboard' )


#---------------------------------------------------------------------------
#RUTA 2A despliega dashboard, portal usuario GET, click del boton y
# redirecciona al registro usuario ruta 1-

@app.route( '/dashboard', methods=["GET"] )
def despliegaDashboard():
    if 'nombre' in session:
        listaUsuarios = Usuario.obtenerListaUsuarios()
        return render_template( "dashboard.html", usuarios=listaUsuarios ) 
    else:
        return redirect( '/' ) 

#2B Show
@app.route( '/usuario/show/<id>', methods=["GET"] )
def despliegaShow(id):
    usuarioAShow = {
        "id": id
    }
    resultado = Usuario.obtenerDatosUsuario( usuarioAShow )
    return render_template( "show.html", usuario=resultado[0] )


#Ruta 2B boton Eliminar (POST), click, elimina y redirecciona a Ruta 2
@app.route( '/usuario/remover/<id>', methods=["POST"])
def eliminarUsuario( id ):
    print( id )
    usuarioAEliminar = {
        'id': id
    }
    resultado = Usuario.eliminarUsuario( usuarioAEliminar )
    print( resultado ) #print
    return redirect( '/dashboard' )

#Ruta 2C boton Editar (GET), no se añade informacion por eso es GET, click y 
# renderiza a Ruta 3 template, antes de renderizarlo vamos a jalar los datos del id 
# en el modelo-
@app.route( '/usuario/editar/<id>', methods=["GET"] )
def despliegaEditar( id ):
    usuarioAEditar = {
        "id": id
    }
    resultado = Usuario.obtenerDatosUsuario( usuarioAEditar )
    return render_template( "editarUsuario.html", usuario=resultado[0] ) #para el placeholder[0]

#ahora vamos a crear el template en html, editarUsuario.html
#---------------------------------------------------------------------------

#Ruta 3 despliega edicion usuario GET

#RUTA 3A
#el html 3 no es un post, la caja que contiene el form es un post, al dar editar en
# este boton colocando los nuevos valores me redireccionará a la ruta 2 con los nuevos valores-
@app.route( '/usuario/editar/<id>', methods=["POST"] )
def editarUsuario( id ):
    usuarioAEditar = {
        "id": id,
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    resultado = Usuario.editarUsuario( usuarioAEditar )
    print(resultado)
    session["nombre"] = request.form["nombre"]
    session["apellido"] = request.form["apellido"]
    return redirect ( '/dashboard' )

