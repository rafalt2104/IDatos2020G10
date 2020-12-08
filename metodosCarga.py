import mysql.connector

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

def validarEmergencia(dato):
        dato = dato.upper()
        dato = dato.strip()
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        sql = "Select emergenciaNombre From " + base_de_datos + ".`emergencia` where '" + str(dato) + "' LIKE CONCAT('%',UPPER(TRIM(emergenciaNombre)),'%')"
        #sql = "Select EmergenciaNombre From " + base_de_datos + ".`emergencias` where UPPER(TRIM(EmergenciaNombre)) LIKE '%" + str(dato) + "%'"
        #print(sql)
        cursor.execute(sql)
        
        result = cursor.fetchone()
        if result is not None:
                emergenciaNombre = result[0]  
        else:
                emergenciaNombre = None                
                

        db.close()
        return emergenciaNombre


def mapeoCalif(calif):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        
        sql = "Select valorNum From " + base_de_datos + ".`calificaciones` where valor = '" + str(calif) + "'"
        cursor.execute(sql)

        valorNum = cursor.fetchone()[0]
        db.close()
        return valorNum

def insBD(datosAlumnos,instituto):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        for alumno in datosAlumnos:
                if not 'Emergencia' in alumno:
                        alumno['Emergencia'] = ''
                if not 'grupo' in alumno:
                        alumno['grupo'] = ''
                
                sql = "INSERT INTO " + base_de_datos + ".`alumnos` (localidad,fechaNac,mutualista,emergencia,carneSaludVenc,calificacion,inasistencias,instituto,grupo) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (alumno['Localidad'],alumno['FechaNac'],alumno['Mutualista'],alumno['Emergencia'],alumno['VencSalud'],alumno['Calificacion'],alumno['inasistencias'],instituto,alumno['grupo'])
                #print(sql)
                cursor.execute(sql)

        db.commit()
        db.close()

def datosRDF():
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        sql = "SELECT * FROM " + base_de_datos + ".alumnos"

        ## getting records from the table
        cursor.execute(sql)

        ## fetching all records from the 'cursor' object
        records = cursor.fetchall()

        return records

def getURI(localidad,mutualista,emergencia,instituto):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        localidad = localidad.upper()
        localidad = localidad.strip()
        mutualista = mutualista.upper()
        mutualista = mutualista.strip()
        emergencia = emergencia.upper()
        emergencia = emergencia.strip()
        instituto = instituto.upper()
        instituto = instituto.strip()

        #localidad
        if localidad is not None and localidad != '':
            sql = "SELECT localidadURI FROM " + base_de_datos + ".localidad where '" + str(localidad) + "' LIKE CONCAT('%',UPPER(TRIM(localidadNombre)),'%')"
            cursor.execute(sql)
            localidadURI = cursor.fetchone()[0]
            print(localidadURI)
        else:
            localidadURI = ''
        
        print(mutualista)
        #mutualista
        if mutualista is not None and mutualista != '':
            print('entraste puto')
            sql = "SELECT servicioSaludURI FROM " + base_de_datos + ".serviciosalud where '" + str(mutualista) + "' LIKE CONCAT('%',UPPER(TRIM(servicioSaludNombre)),'%')"
            cursor.execute(sql)
            mutualistaURI = cursor.fetchone()[0]
            print(mutualistaURI)
        else:
            mutualistaURI = ''

        #emergencia
        if emergencia is not None and emergencia != '':
            sql = "SELECT emergenciaURI FROM " + base_de_datos + ".emergencia where '" + str(emergencia) + "' LIKE CONCAT('%',UPPER(TRIM(emergenciaNombre)),'%')"
            cursor.execute(sql)
            emergenciaURI = cursor.fetchone()[0]
            print(emergenciaURI)
        else:
            emergenciaURI = ''

        #instituto
        if instituto is not None and instituto != '':
            sql = "SELECT instututoURI FROM " + base_de_datos + ".instituto where '" + str(instituto) + "' LIKE CONCAT('%',UPPER(TRIM(institutoNombre)),'%')"
            cursor.execute(sql)
            institutoURI = cursor.fetchone()[0]
            print(institutoURI)
        else:
            institutoURI = ''

        return localidadURI,mutualistaURI,emergenciaURI,institutoURI