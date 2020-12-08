import xlrd 
import re
import datetime
import metodosCarga
import sys

#archivo = sys.argv[1]
#instituto = sys.argv[2]

archivo = 'C:/Users/Rafael/Desktop/Facultad/IntegracionDatos/escuelaDelPlataAuxmatricula.xlsx'
instituto = 'ESCUELA DEL PLATA'

wb = xlrd.open_workbook(str(archivo))

hoja = wb.sheet_by_index(0)

datosAlumnos = []
datos = {}
idAlumno = 1
inasistencias = 0
grupo = hoja.cell_value(1,52)
datos['grupo'] = grupo


#for i in range(1,hoja.nrows):
print('Num rows = ',hoja.nrows)
for i in range(1,66):
        iter = hoja.cell_value(i,0)
        #if iter == 'Localidad':
        iter = str(iter)

        if re.search("^Localidad.*", iter):
                #print(1)
                datos['Alumno'] = 'Alumno' + str(idAlumno)
                localidad = hoja.cell_value(i,3)
                localidad = str(localidad)
                if re.search("\n", localidad):
                        valor = localidad.split('\n')
                        valor = valor[0]
                else:
                        valor = localidad
                datos['Localidad'] = valor
        elif iter == 'Año lectivo':
                #print(2)
                datos['inasistencias'] = inasistencias
                datosAlumnos.append(datos)
                idAlumno+=1
                inasistencias = 0
                datos = {}
                grupo = hoja.cell_value(i+1,54)
                datos['grupo'] = grupo
        elif re.search("de identidad.*", iter):
                #print(3)
                aux = hoja.cell_value(i,41)
                aux = str(aux)
                aux = aux.split("\n")
                aux = aux[0]
                aux = aux.split('/')
                valor = datetime.date(int(aux[2]), int(aux[1]), int(aux[0]))
                datos['FechaNac'] = valor    
                print(datos)    									
        elif re.search("Vencimiento CEV.*", iter):
                #print(4)
                aux = hoja.cell_value(i,39)                
                valor = aux
                datos['Mutualista'] = valor        
        elif re.search(".*Emergencia.*", iter,re.DOTALL):
                #print(5)
                #print(re.search(".*Emergencia.*", iter,re.DOTALL))
                aux = hoja.cell_value(i,10)   
                #print(re.search("^\d", aux))
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
                        #print('else y aux = ',aux)
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
                                datos['VencSalud'] = valor

        elif re.search(".*Venc..*", iter,re.DOTALL):
                aux = hoja.cell_value(i,0)   
                print('aux = ',str(aux)) 
                valor = re.search("[\d|/]+$", aux,re.DOTALL)
                print('valor = ',valor)
                if valor is not  None:
                        print('hola')
                        datos['VencSalud'] = valor.__getitem__(0)
                else:
                        print('kjdajkad')
                        aux = hoja.cell_value(i,1)
                        print(aux)

        elif re.search(".*Promovido.*", iter,re.DOTALL):
                aux = hoja.cell_value(i,36)
                valor = metodosCarga.mapeoCalif(aux)
                datos['Calificacion'] = aux
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

print(datosAlumnos)
#metodosCarga.insBD(datosAlumnos,instituto)