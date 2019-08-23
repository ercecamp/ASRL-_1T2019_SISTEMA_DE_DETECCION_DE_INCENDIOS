#!/usr/bin/env python
 
#Se importan los módulos
import MySQLdb
import time
import easygui as eg
from pylab import *
import matplotlib.pyplot as plt
import time

#Función para ingresar un nuevo nodo a la base de datos
def ingresoNodo():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Pedido de datos para el ingreso a la 
    	print("Ingrese un codigo de maximo 20 caracteres")
    	cod_Nodo = raw_input()
    	print("Ingrese una descripcion para el nodo")
    	Descrip_Nodo = raw_input()
    	print("Ingrese la longitud del donde esta ubicado el nodo")
    	Longitud_Nodo = raw_input()
    	print("Ingrese la latitud del donde esta ubicado el nodo")
    	Latitud_Nodo = raw_input()
    	print("Ingrese un numero de contacto para casos de emergencia")
    	Numero_Nodo = raw_input()
    
    	aux = 0
        #Verificar el cod del sector
	while aux==0:
	    print("Ingrese el codigo del sector")
	    Cod_Sect_N = raw_input()
	    my_query="SELECT * FROM Sector WHERE Cod_sector='"+Cod_Sect_N+"'"
	    cursor.execute(my_query)
            result_Nodo=cursor.fetchone()
            if(result_Nodo==None):
	        print("Codigo del sector no existe en la base de datos")
		print("Intente con las siguientes opciones: ")
		print("Cod_Sector          Nombre")
	        my_query="SELECT * FROM Sector"
	        cursor.execute(my_query)
		for rw in cursor.fetchall():
		    print(rw[0]+"       "+rw[1])
		    time.sleep(0.5)
	    else:
		aux = 1
	
	#Ingreso a la base de datos   
	my_query="INSERT INTO Nodo VALUES('"+cod_Nodo+"','"+Descrip_Nodo+"','"+Longitud_Nodo+"','"+Latitud_Nodo+"',"+Numero_Nodo+",'"+Cod_Sect_N+"')"
	cursor.execute(my_query)
	db.commit()
	#Cerrar la conexion con la base de datos
    	db.close()
	print("Nodo ingresado correctamente")
    except:
	print("Ha ocurrido un error de registro")
    

#Función para eliminar un nodo
def eliminarNodo():
    #Conectar con la base de datos
    try:
    	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")
    try:
	print("Ingrese el código del Nodo a eliminar")
	cod_Nodo = raw_input()
        my_query="DELETE FROM Nodo WHERE Cod_Nodo='"+cod_Nodo+"'"
        cursor.execute(my_query)
	db.commit()
	#Cerrar la conexion con la base de datos
    	db.close()
	print("Eliminacion del nodo exitoso")
    except:
	print("Error al eliminar el nodo") 


#Funcion para ingresar un nuevo sector a la base de datos
def ingresoSector():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Pedido de datos para el ingreso a la 
    	print("Ingrese un código de móximo 20 caracteres")
    	cod_Sector = raw_input()
    	print("Ingrese el nombre del sector")
    	Nombre_sector = raw_input()
    	print("Ingrese la población")
    	Poblacion_Sector = raw_input()
    	print("Ingrese el nómero de manzanas")
    	Manzanas_Sector = raw_input()
    
    	aux = 0
        #Verificar el cod de la parroquia
	while aux==0:
	    print("Ingrese el código de la parroquia")
	    Cod_Parroquia_S = raw_input()
	    my_query="SELECT * FROM Parroquia WHERE Cod_Parroquia='"+Cod_Parroquia_S+"'"
	    cursor.execute(my_query)
            result_Parroquia=cursor.fetchone()
            if(result_Parroquia==None):
	        print("Código de la parroquia no existe en la base de datos")
		print("Intente con las siguientes opciones: ")
		print("Cod_Parroquia          Nombre")
	        my_query="SELECT * FROM Parroquia"
	        cursor.execute(my_query)
		for rw in cursor.fetchall():
		    print(rw[0]+"       "+rw[1])
		    time.sleep(0.5)
	    else:
		aux = 1

	#Ingreso a la base de datos   
	my_query="INSERT INTO Sector VALUES('"+cod_Sector+"','"+Nombre_sector+"',"+Poblacion_Sector+","+Manzanas_Sector+",'"+Cod_Parroquia_S+"')"
	cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Sector ingresado correctamente")
    except:
	print("Ha ocurrido un error de registro")
    

#Funcion para eliminar un sector
def eliminarSector():
    #Conectar con la base de datos
    try:
    	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")
    try:
	print("Ingrese el código del Sector a eliminar")
	cod_Sector = raw_input()
        my_query="DELETE FROM Sector WHERE Cod_Sector='"+cod_Sector+"'"
        cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Eliminación del sector exitoso")
    except:
	print("Error al eliminar el sector") 


#Funcion para ingresar una nueva parroquia a la base de datos
def ingresoParroquia():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Pedido de datos para el ingreso a la base de datos
    	print("Ingrese un código de máximo 20 caracteres")
    	Cod_Parroquia = raw_input()
    	print("Ingrese el nombre de la parroquia")
    	Nombre_Parroquia = raw_input()
    	
    	aux = 0
        #Verificar el cod de la ciudad
	while aux==0:
	    print("Ingrese el codigo de la ciudad")
	    Cod_Ciudad_P = raw_input()
	    my_query="SELECT * FROM Ciudad WHERE Cod_Ciudad='"+Cod_Ciudad_P+"'"
	    cursor.execute(my_query)
            result_Nodo=cursor.fetchone()
            if(result_Nodo==None):
	        print("Codigo de la parroquia no existe en la base de datos")
		print("Intente con las siguientes opciones: ")
		print("Cod_Ciudad          Nombre")
	        my_query="SELECT * FROM Ciudad"
	        cursor.execute(my_query)
		for rw in cursor.fetchall():
		    print(rw[0]+"       "+rw[1])
	   	    time.sleep(0.5)
	    else:
		aux = 1
   
	#Ingreso a la base de datos
	my_query="INSERT INTO Parroquia VALUES('"+Cod_Parroquia+"','"+Nombre_Parroquia+"','"+Cod_Ciudad_P+"')"
	cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Parroquia ingresada correctamente")
    except:
	print("Ha ocurrido un error de registro")
    

#Función para eliminar una parroquia
def eliminarParroquia():
    #Conectar con la base de datos
    try:
    	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")
    try:
	print("Ingrese el código de la parroquia a eliminar")
	cod_Parroquia = raw_input()
        my_query="DELETE FROM Parroquia WHERE Cod_Parroquia='"+cod_Parroquia+"'"
        cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Eliminación de la parroquia exitoso")
    except:
	print("Error al eliminar la parroquia") 


#Función para ingresar una nueva ciudad a la base de datos
def ingresoCiudad():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Pedido de datos para el ingreso a la base de datos
    	print("Ingrese un código de máximo 20 caracteres")
    	Cod_Ciudad = raw_input()
    	print("Ingrese el nombre")
    	Nombre_Ciudad = raw_input()
    	print("Ingrese la densidad de población")
    	Densidad_Ciudad = raw_input()
    	print("Ingrese el área en km2")
    	Area_Ciudad = raw_input()
    	print("Ingrese la poblacion existente")
    	Poblacion_Ciudad = raw_input()
    
	#Ingreso a la base de datos	
	my_query="INSERT INTO Ciudad VALUES('"+Cod_Ciudad+"','"+Nombre_Ciudad+"',"+Densidad_Ciudad+","+Area_Ciudad+","+Poblacion_Ciudad+")"
	print(my_query)
	cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Ciudad ingresada correctamente")
    except:
	print("Ha ocurrido un error de registro")
    

#Función para eliminar una ciudad
def eliminarCiudad():
    #Conectar con la base de datos
    try:
    	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")
    try:
	print("Ingrese el código de la ciudad a eliminar")
	cod_Ciudad = raw_input()
        my_query="DELETE FROM Ciudad WHERE Cod_Ciudad='"+cod_Ciudad+"'"
        cursor.execute(my_query)
	db.commit()
	#Cerrar la conexión con la base de datos
    	db.close()
	print("Eliminación de la ciudad exitosa")
    except:
	print("Error al eliminar la ciudad") 

#Función para consultar los nodos 
def consultaNodos():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Consulta de nodos
	print("Cod_Nodo          Descripción")
        my_query="SELECT * FROM Nodo"
        cursor.execute(my_query)
	for rw in cursor.fetchall():
	    print(rw[0]+"       "+rw[1])   
   	    time.sleep(0.5)
    except:
	print("Error con la base de datos")

#Función para consulta de sectores
def consultaSectores():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Consulta de sectores
	print("Cod_Sector          Nombre")
        my_query="SELECT * FROM Sector"
        cursor.execute(my_query)
	for rw in cursor.fetchall():
	    print(rw[0]+"       "+rw[1])  
	    time.sleep(0.5)
    except:
	print("Error con la base de datos")

#Función para consultar parroquias
def consultaParroquias():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Consulta de parroquias
	print("Cod_Parroquia          Nombre")
        my_query="SELECT * FROM Parroquia"
        cursor.execute(my_query)
	for rw in cursor.fetchall():
	    print(rw[0]+"       "+rw[1])   
   	    time.sleep(0.5)
    except:
	print("Error con la base de datos")

#Función para consultar ciudades
def consultaCiudades():
    #Conectar con la base de datos
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()
    except:
        print("Error al conectar con la base de datos")

    try:
    	#Consulta de nodos
	print("Cod_Ciudad          Nombre")
        my_query="SELECT * FROM Ciudad"
        cursor.execute(my_query)
	for rw in cursor.fetchall():
	    print(rw[0]+"       "+rw[1])   
   	    time.sleep(0.5)
    except:
	print("Error con la base de datos")

#Función para obtener gráficas de los registros de la base de datos
def graficaPastel():
    print("Esta gráfica muestra un análisis del porcentaje de incendios que han detectado los nodos")
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()

	#Consultar La cantidad de nodos que hay en la base de datos
	my_query="SELECT * FROM Nodo"
	cursor.execute(my_query)
	lista_nodos=cursor.fetchall()
	y=[]
	etiquetas=[]
	for rw in lista_nodos:
	    #De cada nodo se consulta en cuantos se produjo un incendio
	    my_query="SELECT * FROM Censado WHERE Cod_Nodo_C='"+rw[0]+"' AND Incendio=1"
	    cursor.execute(my_query)
	    lista_Cens_N=cursor.fetchall()
	    acu=0
	    for i in lista_Cens_N:
		acu+=1
	    y.append(acu)
	    etiquetas.append(rw[0])
	#Gráfico pastel
	pie(y)
	#xlabel('mi gráfico')
	title('Gráfico Pastel de Incendio en los Nodos')
	legend( (etiquetas), loc = 'upper left')
	draw()
	grid(True)
	show()
	#cerrar la conexión con la base de datos
	db.close()
    except:
	print("Error al graficar")
#Función de grafico de barras por fechas
def graficoBarras():
    try:
	#Conectar con la base de datos
    	db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")
    	#crear un cursor
    	cursor = db.cursor()

	#Pedido de fechas de consulta
	print("Ingrese la fecha de inicio con formato y-m-d")
	FechaInicio=raw_input()
	print("Ingrese la fecha final con formato y-m-d")
	FechaFinal=raw_input()
	#Declarar las listas vacias	
	y=[]
	etiquetas=[]
	#Consulta de cuantos nodos se tiene en la base de datos
	my_query="SELECT * FROM Nodo"
        cursor.execute(my_query)
	for rw in cursor.fetchall():
	    #Consulta de la cantidad de incendios en rango de fechas de cierto nodo
	    my_query="SELECT * FROM Censado WHERE Cod_Fecha_C BETWEEN '"+FechaInicio+"' AND '"+FechaFinal+"' AND Cod_Nodo_C='"+rw[0]+"' AND Incendio=1"
	    cursor.execute(my_query)
	    lista_Censad=cursor.fetchall()
	    acu=0
	    for i in lista_Censad:
		acu+=1
	    y.append(acu)
	    etiquetas.append(rw[0])
	
	#Gráfico de barras
	fig = plt.figure(u'Grafico de barras')
	ax = fig.add_subplot(111)
	xx = range(len(y))

	ax.bar(xx, y, width=0.8, align='center')
	ax.set_xticks(xx)
	ax.set_xticklabels(etiquetas)

	plt.show()
    except:
	print("Error en el proceso")
#Menú del programa
op=-1
while op!=15:
    print("====================================================================")
    print("               MENÚ DE ADMINISTRACIÓN DE BASE DE DATOS              ")
    print("====================================================================")
    print("1. Ingresar un nuevo nodo")
    print("2. Eliminar un nodo existente")
    print("3. Ingresar un sector")
    print("4. Eliminar un sector")
    print("5. Ingresar una parroquia")
    print("6. Eliminar una parroquia")
    print("7. Ingresar una ciudad")
    print("8. Eliminar una ciudad")
    print("9. Gráfica pastel del total de incendios en los nodos")
    print("10. Gráfico de barras de incendios por nodo segun una fecha")
    print("11. Consulta de nodos registrados")
    print("12. Consulta de sectores reguistrados")
    print("13. Consulta de parroquias registradas")
    print("14. Consulta de ciudades registradas")
    print("15. Salir")
    try:
    	print("Ingrese una opción: ")
    	op = input() 
    except:
	print("Error al ingreso de opción")
    if(op==1):
	ingresoNodo()
	time.sleep(2)
    elif(op==2):
        eliminarNodo()
	time.sleep(2)
    elif(op==3):
	ingresoSector()
	time.sleep(2)
    elif(op==4):
        eliminarSector()
	time.sleep(2)
    elif(op==5):
	ingresoParroquia()
	time.sleep(2)
    elif(op==6):
        eliminarParroquia()
	time.sleep(2)
    elif(op==7):
	ingresoCiudad()
	time.sleep(2)
    elif(op==8):
        eliminarCiudad()
	time.sleep(2)
    elif(op==9):
        graficaPastel()
	time.sleep(2)
    elif(op==10):
	graficoBarras()
	time.sleep(2)
    elif(op==11):
	consultaNodos()
	time.sleep(2)
    elif(op==12):
	consultaSectores()
	time.sleep(2)
    elif(op==13):
	consultaParroquias()
	time.sleep(2)
    elif(op==14):
	consultaCiudades()
	time.sleep(2)
    elif(op==15):	
        print("Gracias por su visita")
	time.sleep(2)
    else:	
        print("Opcion incorrecta")
	time.sleep(2)

