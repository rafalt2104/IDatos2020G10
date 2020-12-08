import mysql.connector
import xlrd 

db_host = 'localhost'
db_port = 3306
usuario = 'root'
clave = 'root'
base_de_datos = 'integracion_datos'

config = {
        'user':usuario,
        'password': clave,
        'host': db_host,
        'database': base_de_datos,
        'raise_on_warnings': True
}

archivo = 'C:/Users/Max/Desktop/ID/arauxiliarmatricula.xlsx'
  
wb = xlrd.open_workbook(archivo) 

hoja = wb.sheet_by_name('Hoja1')

linea1 = hoja.cell_value(0, 0)

print(linea1)

insBD(linea1)

def insBD(nombre):

    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO " + base_de_datos + ".`plane` (nombre) VALUES (NULL, '%s')" % (nombre)
    cursor.execute(sql)
        
    db.commit()
    db.close()
