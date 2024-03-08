from Conexion import *

#CClientes = classe clientes 
class CClientes:
    def ingresarClientes(nombre, apellido, sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()

            sql = "insert into usuarios values(null, %s, %s, %s);"
            #La variables valores tiene que ser una tupla 
            #como minoma exprecion es (valor,), la coma indica que es una tupla en caso de que  
            #tenga un solo valor  

            valores = (nombre, apellido, sexo)
            cursor.execute(sql,valores)
            cone.commit()
            
            print(cursor.rowcount, "Registro ingresado")
            cone.close


        except mysql.connector.Error as error:
            
            print("Error de ingreso de datos{}".format(error))
         