import xlrd 
import re
import datetime
import metodosCarga
import sys

archivo = sys.argv[1]
#archivo = 'C:/Users/Rafael/Desktop/Facultad/IntegracionDatos/colegioAmerica.xlsx'
instituto = 'COLEGIO AMÉRICA'

wb = xlrd.open_workbook(str(archivo))

hoja = wb.sheet_by_index(0)

datosAlumnos = []
datos = {}

for i in range(3,hoja.nrows):
    datos = {}
    datos['Localidad'] = hoja.cell_value(i,23)
    aux = hoja.cell_value(i,11)
    aux = aux.split('/')
    anio = '20' + aux[2]
    valor = datetime.date(int(anio), int(aux[1]), int(aux[0]))
    datos['FechaNac'] = valor
    datos['Mutualista'] = hoja.cell_value(i,59)
    aux = hoja.cell_value(i,70)
    aux = aux.split('/')
    anio = '20' + aux[2]
    valor = datetime.date(int(anio), int(aux[1]), int(aux[0]))
    datos['VencSalud'] = valor
    calif = int(hoja.cell_value(i,75))
    datos['Calificacion'] = str(calif)
    faltas = int(hoja.cell_value(i,76))
    datos['inasistencias'] = faltas
    datos['grupo'] = hoja.cell_value(i,1)

    valor = hoja.cell_value(i,60)
    valor = metodosCarga.validarEmergencia(valor)
    if valor != None:
        datos['Emergencia'] = valor
    print(datos)
    datosAlumnos.append(datos)

metodosCarga.insBD(datosAlumnos,instituto)
