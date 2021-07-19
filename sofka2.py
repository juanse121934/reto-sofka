import random
import json
from pathlib import Path
import time

# Se define la clase Carro
class Carro:

    def __init__(self, name,pista,distancia):
        self.name = name
        self.pista = pista
        self.distancia = distancia

#Para almacenar cada una de las clases creadas
lista = []

#Cantidad de metros que tiene cada pista
distanciaTotal = 10000

listaNombres = ["Pedro","Maria","Ricardo","Angela","Gino","Juanita","Juanse"]
contador = 1
#Se crea cada clase con el nombre ingresado
for elemento in listaNombres:
    lista.append(Carro(elemento,contador,0))
    contador += 1

#Si no existe un archivo con los resultados de las competencias se inicializa 
#un Json vacío para guardarlos
if not Path('resultados.json').is_file():
    #se crea el Json
    dict_resultado = {}
    dict_resultado['Podio']=[]

#Se verifica si existe un archivo con los ganadores, si existe se abre el archivo
#si no existe se crea un Json vacío para guardar la información
if Path('ganadores.json').is_file():
    # Se lee el json
    with open('ganadores.json') as file:
        dict_ganadores = json.load(file)    
else:
    #se crea el Json    
    dict_ganadores = {}

#Se crea una variable boolena para controlar si la carrera termina o no
blnCarrera = True

while blnCarrera:
#para cada uno de los participantes se lanza el dado  
    for elemento in lista:
        resultado = random.randint(1,6)
        elemento.distancia += resultado * 100
        if elemento.distancia >= distanciaTotal:
            blnCarrera = False

#Una vez terminada la carrera se orden la lista para obtener el podio
lista2 =  sorted(lista, key=lambda Carro: Carro.distancia, reverse=True)

#Se imprime el orden de llegada
print ("Orden de llegada")

print ("Primer Lugar:", lista2[0].name, "metros recorridos ", lista2[0].distancia )
print ("Segundo Lugar:", lista2[1].name, "metros recorridos ", lista2[1].distancia )
print ("Tercer Lugar:", lista2[2].name,  "metros recorridos ", lista2[2].distancia )

#Se guardan los resultados de cada competencia
dict_resultado['Podio'].append({
    'Fecha_hora' : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
    'Primero': lista2[0].name,
    'Segundo': lista2[1].name,
    'tercero': lista2[2].name})

with open('resultados.json', 'w') as file:
    json.dump(dict_resultado, file, indent=4)

#Se actualizan la lista de ganadores
if lista2[0].name in dict_ganadores:
    dict_ganadores[lista2[0].name] += 1
else:
    dict_ganadores[lista2[0].name] = 1         

with open('ganadores.json', 'w') as file:
    json.dump(dict_ganadores, file, indent=4)

print ("Fin de carrera")