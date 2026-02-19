import os
import shutil
path = input("Ingrese la ruta del archivo: ")
formatos = {
    "pdf": "PDFs",
    "jpg": "Imagenes",
    "jpeg": "Imagenes",
    "png": "Imagenes",
    "doc": "Documentos",
    "docx": "Documentos",  
    "gif": "Imagenes",
    "txt": "Documentos",
    "exe": "Ejecutables",
    "zip": "Comprimidos",
    "rar": "Comprimidos",
    "mp4": "Videos",
    "avi": "Videos",
    "mp3": "Audio",
    "wav": "Audio",
}

def verificarFormatos(path):
    if os.path.isdir(path):
        for archivo in os.listdir(path):
            rutaDeElArchivo = os.path.join(path, archivo) #extrae la ruta de el archivo verificandose
            if os.path.isfile(rutaDeElArchivo):
                extension = archivo.split('.')[-1].lower() #extrae la extension dividiendo los puntos y sacando el ultimo indice -1 siempre es el ultimo
                categoria = formatos.get(extension, "Otros") #la categoria es igual a la clave de la extension, si no esta agregada sera "Otros"
                print(f"{archivo}  -->  {categoria}")
                try:
                    rutaCarpeta = os.path.join(path, categoria)
                    os.makedirs(rutaCarpeta, exist_ok=True)
                    shutil.move(rutaDeElArchivo, rutaCarpeta)
                except OSError as e: #try catch
                    print("Error creando carpeta")


verificarFormatos(path)
