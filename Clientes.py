from Conexion import *

class CClientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
         cone = CConexion.ConexionBaseDeDatos();
         cursor = cone.cursor()
         sql ="insert into usuarios values(null,%s,%s,%s);"
         valores =(nombres,apellidos,sexo)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Actualizado")
         cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))


    def mostrarClientes():
       
       try:
         cone = CConexion.ConexionBaseDeDatos();
         cursor = cone.cursor()
         cursor.execute("select * from usuarios;")
         miResultado = cursor.fetchall()         
         cone.commit()         
         cone.close()
         return miResultado

       except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarClientes(idUsuario,nombres,apellidos,sexo):

        try:
         cone = CConexion.ConexionBaseDeDatos();
         cursor = cone.cursor()
         sql ="UPDATE usuarios SET usuarios.nombres = %s,usuarios.apellidos = %s,usuarios.sexo = %s Where usuarios.id =%s; "
         valores =(nombres,apellidos,sexo,idUsuario)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Actualizado")
         cone.close()

        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))

    def EliminarClientes(idUsuario):

        try:
         cone = CConexion.ConexionBaseDeDatos();
         cursor = cone.cursor()
         sql ="DELETE from usuarios WHERE usuarios.id= %s; "
         valores =(idUsuario,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Eliminado")
         cone.close()

        except mysql.connector.Error as error:
            print("Error de Eliminacion de datos {}".format(error))


    