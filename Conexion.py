import mysql.connector

class CConexion:

 def ConexionBaseDeDatos():
     try:
        conexion = mysql.connector.connect(user='root',password='2804',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
        print("Conexion Correcta")

        return conexion

     except mysql.connector.Error as error:
        print("Error al conectarse a la base Datos {}".format(error))

        return conexion
    
 ConexionBaseDeDatos()





