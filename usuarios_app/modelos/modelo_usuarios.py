from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__( self, id, nombre, apellido, email, created_at, updated_at ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

        #RUTA 1A. Registrar acá insertamos los nuevos usuarios
    @classmethod #controlador ruta 1a para registro
    def agregaUsuario( cls, nuevoUsuario ): #diccionario creado
        query = "INSERT INTO usuarios(nombre, apellido, email) VALUES(%(nombre)s, %(apellido)s, %(email)s)"
        resultado= connectToMySQL( "users_schema" ).query_db( query, nuevoUsuario )
        return resultado #se lo vamos a devolver al controlador

        #RUTA 2A ver el portal con usuario /
    @classmethod
    def obtenerListaUsuarios( self ):
        query = "SELECT * FROM usuarios;"
        resultado = connectToMySQL( "users_schema" ).query_db( query ) #nombre de la BD
        listaUsuarios = []
        for usuario in resultado:
            listaUsuarios.append( Usuario( usuario["id"], usuario["nombre"], usuario["apellido"], usuario["email"], usuario["created_at"], usuario["updated_at"]))
        return listaUsuarios



        #RUTA 2B Eliminar AQUÍ!!!!!!!!!!!!!!!!!!!
    @classmethod
    def eliminarUsuario( cls, usuario ):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_schema" ).query_db( query, usuario )
        return resultado

        #Ruta 2C boton Editar (GET), no se añade informacion por eso es GET, click y renderiza a Ruta 3 template, antes de renderizarlo vamos a jalar los datos del id en el controlador-
    @classmethod
    def obtenerDatosUsuario( self, usuario ):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL( "users_schema" ).query_db( query, usuario )
        return resultado

        #RUTA 3A #el html 3 no es un post, la caja que contiene el form es un post
    @classmethod
    def editarUsuario( self, usuarioAEditar ):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s WHERE id = %(id)s;" #####
        resultado = connectToMySQL( "users_schema" ).query_db( query, usuarioAEditar )
        return resultado
