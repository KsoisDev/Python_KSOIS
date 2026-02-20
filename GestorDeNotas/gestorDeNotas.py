#Gestor de notas en archivos de texto
#Desarrollar una aplicación en Python que permita 
#al usuario crear, visualizar, buscar y eliminar notas
#almacenadas en archivos de texto plano.
#El programa deberá mostrar un menú interactivo en consola
#y garantizar que la información se conserve entre ejecuciones 
#mediante el uso de archivos.
import os
notas = []
pathCWD = os.path.dirname(os.path.abspath(__file__))
def verNota():
    print("¿Que archivo quieres ver?")
    archivo = os.path.join(pathCWD, input("Archivo: ") + ".txt")
    with open(archivo, 'r', encoding='utf-8') as texto:
        for linea in texto:
            print(linea.strip()) #lo lee limpiamente
def crearNota():
    titulo = input("¿Cual sera el titulo de tu nota?")
    titulo = f"{titulo}.txt"
    with open(os.path.join(pathCWD, titulo), "w", encoding="utf-8") as archivoCreado:
        textoDelUsuario = ""
        contador = 1
        print("Escribe cada linea de tu nota, para terminas, solo escribe fin")
        while(textoDelUsuario != "fin"):
            textoDelUsuario = input(f"{contador}. ")
            if textoDelUsuario != "fin":
                archivoCreado.write(f"{contador}. {textoDelUsuario}\n")
                contador += 1
        return archivoCreado.name
def eliminarNotas():
    print("¿Que nota quieres borrar?")
    notaParaEliminar = os.path.join(pathCWD, input("Ingresa el nombre: ")+".txt")
    if (os.path.exists(notaParaEliminar)):
        os.remove(notaParaEliminar)
        print("¡Nota elminada exitosamente!")
    else:
        print("La nota no existe, asegurate de no poner la extension de el archivo.")
def buscarNotas():
    print("Para buscar la nota que quieras, ingresa una palabra dentro de la nota")
    palabraInput = input("palabra: ")
    for archivo in os.listdir(pathCWD):
        extension = archivo.split('.')[-1].lower()
        archivosEncontrados = []
        if extension == "txt":
            with open(os.path.join(pathCWD, archivo), 'r', encoding='utf-8') as texto:
                for linea in texto:
                    palabras = linea.strip().split() #lo divide en palabras
                    for palabra in palabras:
                        if palabra == palabraInput:
                            archivosEncontrados.append(archivo)
                indice = 1
                for i in archivosEncontrados:
                    print(f"{indice}. {i}")
                    indice += 1
while True:
    print("¿Que quieres hacer?\n1. crear nota\n2. ver nota\n3. eliminar nota\n4.buscar nota")
    match int(input("Elige: ")):
        case 1: archivo = crearNota()
        case 2: verNota()
        case 3: eliminarNotas()
        case 4: buscarNotas()
        case _: print("Error")
        
    
    
     
    