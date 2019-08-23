#!/usr/bin/env python
 
#Se importan los módulos necesarios
import socket
import MySQLdb
import time
import easygui as eg

#instanciamos un objeto para trabajar con el socket
ser = socket.socket()
 
#Puerto y servidor que debe escuchar
ser.bind(("", 8085))
 
#Aceptamos conexiones entrantes con el método listen. Por parámetro las conexiones simultáneas.
ser.listen(100)
while True: 
    #Instanciamos un objeto cli (socket cliente) para recibir datos
    cli, addr = ser.accept()

    #Recibimos el mensaje, con el método recv recibimos datos. Por parámetro la cantidad de bytes para recibir
    recibido = cli.recv(1024)

    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

    #Se hace split al mensaje recibido
    listaRecibida = recibido.split(";")

#Ingreso de datos sensado a la base de datos
    #Conectar con la base de datos
    db = MySQLdb.connect(host="localhost",user="root",passwd="Valentina_16",db="proyectolinux")

    #crear un cursor
    cursor = db.cursor()

    #Se asigna los valores recibidos a las respectivas variables
    CodNodo=listaRecibida[0].decode()
    Temperatura=listaRecibida[1]
    Gas=listaRecibida[2]

    #Se verifica si existe el nodo registrado
    my_query="SELECT * FROM Nodo WHERE Cod_Nodo='"+CodNodo+"'"
    cursor.execute(my_query)
    resultado=cursor.fetchone()
    mens_nodo="El nodo = "+CodNodo+" No está registrado en la base de datos"
    if(resultado==None):
	eg.msgbox(msg=mens_nodo, title="Mensaje de Alerta ")
    else:
        #Obtener fecha de sensado
        fecha=time.strftime("%y-%m-%d")

	#Obtener la hora exacta
	hora=time.strftime("%H:%M:%S")

	#Ingresar la hora en caso de no estar ingresada en la tabla hora
	my_query="SELECT * FROM Hora WHERE Cod_Hora='"+hora+"'"
	cursor.execute(my_query)
        resul=cursor.fetchone()
        if(resul==None):
	    print("Ingresando nueva hora")
	    my_query="INSERT INTO Hora VALUES('"+hora+"','"+hora+"')"
	    cursor.execute(my_query)
	    db.commit()

	#Ingresar la fecha en caso de no estar ingresada en la tabla fecha
	my_query="SELECT * FROM Fecha WHERE Cod_Fecha='"+fecha+"'"
	cursor.execute(my_query)
        result=cursor.fetchone()
        if(result==None):
	    print("Ingresando nueva fecha")
            my_query="INSERT INTO Fecha VALUES('"+fecha+"','"+fecha+"')"
            cursor.execute(my_query)
            db.commit()

	#Mensaje de alerta en caso de incendio
	mensaje_alerta="Se está produciendo un incendio en el nodo:  "+CodNodo
        Incendio=0
	if(float(Gas)>12.5):
            if(float(Temperatura)>60):
                Incendio=1
                eg.msgbox(msg=mensaje_alerta, title="Mensaje de Alerta ")
            else:
                if (float(Gas)>74 and float(Temperatura)>10):
                    Incendio=1
                    eg.msgbox(msg=mensaje_alerta, title="Mensaje de Alerta ")

        #Ingresar el dato sensado a la base de datos
	print("Cargando resultados de muestreo a la base de datos")
	my_query="INSERT INTO Sensado VALUES(DEFAULT,"+Gas+","+Temperatura+",'"+fecha+"','"+hora+"','"+CodNodo+"','"+str(Incendio)+"')"
	cursor.execute(my_query)
	db.commit()

    #Cerrar la conexión con la base de datos
    db.close()

    print("Cerrar sesión con cliente")
    #Cerramos la instancia del socket cliente y servidor
    cli.close()
ser.close()
print("Conexiones cerradas")
