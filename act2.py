# Para cargar se utiliza el open creo  y utilizar el show para lo ultimo creo
from PIL import Image
import os, webbrowser
ruta = "C:/Users/lucaw/Desktop/Programasao/Carpetas/Imagenes/programacion/perry.png"
img = Image.open(ruta)
img.show()
img.save("perry2.png")
