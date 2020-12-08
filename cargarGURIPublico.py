import xlrd 
import re
import datetime
import metodosCarga
import sys

archivo = sys.argv[1]
#archivo = 'C:/Users/Rafael/Desktop/Facultad/IntegracionDatos/IDatos/arauxiliarmatricula.xlsx'
instituto = 'ESCUELA TC 118'

wb = xlrd.open_workbook(str(archivo))

hoja = wb.sheet_by_index(0)

datosAlumnos = []
datos = {}
inasistencias = 0
grupo = hoja.cell_value(1,54)
datos['grupo'] = grupo


#print('Num rows = ',hoja.nrows)
for i in range(1,hoja.nrows):
        iter = hoja.cell_value(i,0)
        iter = str(iter)

        if re.search("^Localidad.*", iter):
                localidad = hoja.cell_value(i,3)
                localidad = str(localidad)
                if re.search("\n", localidad):
                        valor = localidad.split('\n')
                        valor = valor[0]
                else:
                        valor = localidad
                datos['Localidad'] = valor
        elif iter == 'Año lectivo':
                datos['inasistencias'] = inasistencias
                datosAlumnos.append(datos)
                inasistencias = 0
                datos = {}
                grupo = hoja.cell_value(i+1,54)
                datos['grupo'] = grupo
        elif re.search("de identidad.*", iter):
                aux = hoja.cell_value(i,43)
                aux = str(aux)
                aux = aux.split("\n")
                aux = aux[0]
                aux = aux.split('/')
                valor = datetime.date(int(aux[2]), int(aux[1]), int(aux[0]))
                datos['FechaNac'] = valor        									
        elif re.search("Vencimiento CEV.*", iter):
                aux = hoja.cell_value(i,39)                
                valor = aux
                datos['Mutualista'] = valor        
        elif re.search(".*Emergencia.*", iter,re.DOTALL):
                aux = hoja.cell_value(i,10)   
                if re.search("^\d", aux):
                        aux = str(aux)
                        aux = aux.split("\n")
                        if aux.len() > 1:
                                valor = aux[1]
                                valor = metodosCarga.validarEmergencia(valor)
                                if valor != None:
                                        datos['Emergencia'] = valor
                        else:
                                datos['Emergencia'] = ''
                else:
                        if aux == None or aux == 'NO TIENE':
                                datos['Emergencia'] = ''
                        else:        
                                valor = re.search("^\D*", aux)
                                valor = valor.__getitem__(0)
                                valor = metodosCarga.validarEmergencia(valor)
                                if valor != None:
                                        datos['Emergencia'] = valor
                                
                                valor = re.search("[\d|/]+$", aux,re.DOTALL)
                                valor = valor.__getitem__(0)
                                aux = valor
                                aux = aux.split('/')
                                valor = datetime.date(int(aux[2]), int(aux[1]), int(aux[0]))
                                datos['VencSalud'] = valor

        elif re.search(".*Venc..*", iter,re.DOTALL):
                aux = hoja.cell_value(i,0)   
                valor = re.search("[\d|/]+$", aux,re.DOTALL)
                aux = valor.__getitem__(0)
                aux = aux.split('/')
                valor = datetime.date(int(aux[2]), int(aux[1]), int(aux[0]))
                datos['VencSalud'] = valor

        elif re.search(".*Promovido.*", iter,re.DOTALL):
                aux = hoja.cell_value(i,36)
                valor = metodosCarga.mapeoCalif(aux)
                datos['Calificacion'] = valor
        elif re.search(".*FALTAS JUSTIFICADAS.*", iter,re.DOTALL):
                aux = hoja.cell_value(i,11)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,17)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,22)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,28)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,31)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,37)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,42)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,46)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,51)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,54)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,56)
                inasistencias += int(aux)
        elif re.search(".*FALTAS INJUSTIFICADAS.*", iter,re.DOTALL):
                #print('Injustificadas')
                aux = hoja.cell_value(i,11)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,17)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,22)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,28)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,31)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,37)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,42)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,46)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,51)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,54)
                inasistencias += int(aux)
                aux = hoja.cell_value(i,56)
                inasistencias += int(aux)

datos['inasistencias'] = inasistencias
datosAlumnos.append(datos)

metodosCarga.insBD(datosAlumnos,instituto)