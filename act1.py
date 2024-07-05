from PIL import Image
import os, webbrowser
#Ingresar la ruta completa de una imagen, si es valida hacer los procedimientos y sino indicar que la ruta no es valida, luego devolver los siguientes datos de imagen: Nombre, Res, Extension, Ubicacion(la que le pasamos)
def getImage():
    ruta = input('Por favor ingrese la ruta que debe ser completa y local de una imagen ')
    # print(ruta)
    if os.path.exists(ruta):
        return ruta
    else:
        return getImage()
ruta = getImage()
img = Image.open(ruta)
format = img.format.lower()
#Format te devuelve el formato en mayuscula entonces lo paso a minuscula
nombre = str(img.filename.split('\\')[-1].lower())
#El .split lo hace una lista
nombre = nombre.replace(f'.{format}', '')
size = img.size
img.save("perry.png")
print(nombre)
print(img.format)
print(img.size)
# print(img.width, img.height)
print(size[0] * size[1])
print(ruta)
    