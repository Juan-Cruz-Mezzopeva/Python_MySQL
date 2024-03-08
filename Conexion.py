#  comando usado para instalar conector: pip install mysql-connector-python
import mysql.connector


# CConexion = Clase Coneccion 
class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user="root", password="PCMezzo89637",
                                               host="127.0.0.1",
                                               database="clientesdb",
                                               port="3306")

            print("Conexion Correcta")

            return conexion
        except mysql.connector.Error as error:

            print("Error al conectarse a la Base de Datos mostrar la interfaz, error {}".format(error))
            return conexion

    ConexionBaseDeDatos()