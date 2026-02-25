#Implementar una aplicación que permita copiar el contenido de un archivo hacia otro archivo destino indicado por el usuario.
#  El programa deberá funcionar con archivos de texto y archivos binarios (por ejemplo, imágenes o PDFs).
import os
rutaOriginal = input("Ingresa el archivo orignal: ").replace('"', '' )
rutaDestino = input("Ingresa la ruta destino: ").replace('"', '' )
rutaDestino = os.path.join(rutaDestino, os.path.basename(rutaOriginal)) #agrega a la carpeta el nombre de el archivo
with open (rutaOriginal, "rb") as archivoOriginal, open (rutaDestino, "wb") as archivoDestino: #abre las dos rutas para poder trabajar con ellas (wb y rb significan que lean el binario, no el texto)
    archivoDestino.write(archivoOriginal.read()) #que cree el archivo con el contenido binario que lea
    print("¡Archivo copiado!")