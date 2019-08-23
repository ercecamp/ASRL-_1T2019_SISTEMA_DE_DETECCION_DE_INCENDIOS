#!/usr/bin/env python
#coding=utf-8
#Variables
#ip del servidor
host = '192.168.2.194'
port = 8085
#Se importan los módulos necesarios
import time
#from random import randint
import socket
import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #Ajustamos la placa en modo BCM
GPIO.setup(4, GPIO.IN) #Declaramos que el pin 4 será de entrada

nombre_nodo=b"Alb_Rasp1_Guay;"
while True:
    #Lectura de temperatura del sensor
    humidity, temperature = Adafruit_DHT.read_retry(22, 17)#lectura del sensor DHT22 Conectado al pin 17
    lectura = GPIO.input(4)
    temp = int(temperature)
    gas = int(lectura)
    try:
        #Creación de un objeto socket (del lado del cliente)
        obj = socket.socket()
 
        #Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
        obj.connect((host, port))
        print("Conectado al servidor")
        #Convertimos a string los valores e imprimimos su valor
        dato_Temperatura = str(temp)
        print(dato_Temperatura)
        dato_Gas = str(gas)
        print(dato_Gas)
        #Enviar los datos al servidor
        obj.send(nombre_nodo+dato_Temperatura.encode()+b";"+dato_Gas.encode())
    
        #Cerramos la instancia del objeto servidor
        obj.close()

        #Imprimimos la palabra Adiós para cuando se cierre la conexión
        print("Conexión cerrada")
    except:
        print("Error al conectarse con el servidor")
        
    time.sleep(600)
#mesaje de fin del programa
print("Fin del programa")
