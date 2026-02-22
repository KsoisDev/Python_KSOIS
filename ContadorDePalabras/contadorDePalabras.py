#Contador de palabras de un archivo
#Crear un programa que solicite al usuario 
#la ruta de un archivo de texto y muestre como resultado 
#el número total de palabras, líneas y caracteres que contiene.
#El sistema deberá manejar posibles errores,
#como archivos inexistentes.
import os
ruta = input("Ingresa la ruta de un archivo: ")
ruta = ruta.replace('"', '')
extension = ruta.split('.')[-1].lower()
def contarPalabras(ruta):
    numeroDePalabras = 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabras = linea.strip().split()
            for palabra in palabras:
                numeroDePalabras += 1
    return numeroDePalabras
def contarLetras(ruta):
    numeroDeLetras = 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            caracteres = linea.strip()
            for caracter in caracteres:
                numeroDeLetras += 1
    return numeroDeLetras
def contarLineas(ruta):
    numeroLineas = 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            numeroLineas += 1
    return numeroLineas


if not os.path.isfile(ruta):
    print("Error, no es una ruta.")
elif extension != "txt":
    print("Error, o es un .txt")
else:
    print("Valido")
    print(f"numero de palabras: {contarPalabras(ruta)}")
    print(f"numero de letras: {contarLetras(ruta)}")
    print(f"numero de lineas: {contarLineas(ruta)}")    