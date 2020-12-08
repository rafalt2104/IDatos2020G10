import mysql.connector
import xlrd 
import re
import datetime
import metodosCarga

from rdflib import Graph, Literal, RDF, URIRef, BNode, Namespace
# rdflib knows about some namespaces, like FOAF
from rdflib.namespace import FOAF, XSD, OWL

# create a Graph
g = Graph()

g.bind("foaf", FOAF)

Alumno =  Namespace("https://estudiantesuruguay.com.uy/")
g.bind("Alumno", Alumno)

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

def contructorRDF():
        records = metodosCarga.datosRDF()

        i = 0
        for record in records:
            identificador = record[0]
            localidad = record[1]
            fechaNac = record[2]
            mutualista = record[3]
            emergencia = record[4]
            carneSaludVencimiento = record[5]
            calificacion = record[6]
            inasistencias = record[7]
            instituto = record[8]

            #Obtener URI's
            localidadURI,mutualistaURI,emergenciaURI,institutoURI = metodosCarga.getURI(localidad,mutualista,emergencia,instituto)

            idAlumno = URIRef("Alumno" + str(identificador))
            # Add triples using store's add() method.

            g.add((idAlumno, RDF.type, URIRef("https://estudiantesuruguay.com.uy/Alumno/")))
            
            if (fechaNac != ""):
                g.add((idAlumno, Alumno.fechaNac, Literal(fechaNac)))
            if (localidad != ""):
                g.add((idAlumno, Alumno.localidad, URIRef(localidadURI)))
            if (mutualista != ""):
                g.add((idAlumno, Alumno.mutualista, URIRef(mutualistaURI)))
            if (emergencia != ""):
                g.add((idAlumno, Alumno.emergencia, URIRef(emergenciaURI)))
            if (carneSaludVencimiento != ""):
                g.add((idAlumno, Alumno.carneSaludVencimiento,Literal(carneSaludVencimiento)))
            if (calificacion != ""):
                g.add((idAlumno, Alumno.calificacion, Literal(calificacion)))
            if (inasistencias != ""):
                g.add((idAlumno, Alumno.inasistencias, Literal(inasistencias)))

            print(instituto,institutoURI)
            if (instituto != ""):
                g.add((idAlumno, Alumno.instituto, URIRef(institutoURI)))

            i += 1
            if i == 2:
                break

            
                
            
contructorRDF()

g.serialize(destination='grafo.xml', format='xml')