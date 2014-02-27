# coding: utf-8
import json
import requests
from jinja2 import template
import webbrowser




def funcion(orientacion):
	if orientacion > "337,5" and orientacion <= "22,5":
		return 'N'
	if orientacion > "22,5" and orientacion <= "67,5":
		return 'NE'
	if orientacion > "67,5" and orientacion <= "112,5":
		return 'E'
	if orientacion > "112,5" and orientacion <= "157,5":
		return 'SE'
	if orientacion > "157,5" and orientacion <= "202,5":
		return 'S'
	if orientacion > "202,5" and orientacion <= "247,5":
		return 'SO'
	if orientacion > "247,5" and orientacion <= "292,5":
		return 'O'
	if orientacion > "292,5" and orientacion <= "337,5":

variable = open('plantilla','w')

html = ''

for linea in variable
	html += linea

plantilla = Template(html)

prov = ['Almería', 'Cádiz', 'Córdoba', 'Huelva', 'Jaén', 'Málaga', 'Sevilla']

consulta1 = raw_input("Introduce el número de la ciudad para saber sus condiciones meteorologicas: ")
prov=diccionario[consulta1]
respuesta=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,%s' % (prov, "spain")})
dicc=json.loads(respuesta.text)
temperaturamaxima=dicc["main"]["temp_max"] - 273
temperaturaminima=dicc["main"]["temp_min"] - 273
viento=dicc["wind"]["speed"]
orientacion=dicc["wind"]["deg"]
orientacion1=funcion(orientacion)


inserccion = plantilla.render(capital=prov,temp_min=temperaturaminima,temp_max=temperaturamaxima,viento1=viento,orientacion2=orientacion1)
archivo = open('salida-html','w')
archivo.write(inserccion)
archivo.close()
webbrowser.open("salida-html.html")






