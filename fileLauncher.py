import os
path = os.path.dirname(os.path.abspath(__file__))
startName = os.path.join(path, "start.bat")
archivosArray = []
rutaArchivos = []
print(path)
def verificarArchivos(path):
    for archivos in os.listdir(path):
        pathActual = os.path.join(path, archivos)
        if os.path.isdir(pathActual):
            verificarArchivos(pathActual)
        elif os.path.isfile(pathActual):
            extension = pathActual.split('.')[-1]
            if extension == "py":
                archivosArray.append(archivos)
                rutaArchivos.append(pathActual)
def ejecutarArchivos(indice):
     os.startfile(rutaArchivos[indice])
def printearArchivos():
    for i in range(len(archivosArray)):
        print(f"{i+1}.{archivosArray[i]}")
def pedirOpcion():
    opcion = input("¿Que programa quieres ejecutar?: ")
    try:
        numero = int(opcion)
        ejecutarArchivos(numero-1)
    except Exception:
        input("error en dar el numero")
    
verificarArchivos(path)
printearArchivos()
pedirOpcion()

