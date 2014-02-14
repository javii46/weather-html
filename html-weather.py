#encoding=utf-8
import json
import requests

def funcion(orientacion):
	if orientacion == 90:
		return 'E'
	if orientacion > 90 and orientacion < 180:
		return 'SE'
	if orientacion == 180:
		return 'S'
	if orientacion > 180 and orientacion < 270:
		return 'SO'
	if orientacion == 270:
		return 'O'
	if orientacion > 270:
		return 'NO'

print 'Lista de las ciudades.' """

1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla

"""

diccionario = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}

consulta = raw_input("Introduce el número de la ciudad para saber sus condiciones meteorologicas: ")
prov=diccionario[consulta]
respuesta=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,%s' % (prov, "spain")})
dicc=json.loads(respuesta.text)
temperaturamaxima=dicc["main"]["temp_max"] - 273
temperaturaminima=dicc["main"]["temp_min"] - 273
viento=dicc["wind"]["speed"]
orientacion=dicc["wind"]["deg"]
orientacion1=funcion(orientacion)

print "La temperatura maxima de",prov,"es",temperaturamaxima,"grados centígrados."
print "La temperatura minima de",prov,"es",temperaturaminima,"grados centígrados."
print "La velocidad del viento en",prov,"es de",round(viento*1600/1000),"kilometros por hora en direccion",orientacion1,




