from PIL import Image
import os

imagen = input("Ingresá la ruta de la imagen: ")
angulo = int(input("Ingresá el ángulo: "))
image = Image.open(imagen)

rotated_image = image.rotate(angulo)
rotated_image.save('paisaje_rot.jpeg')

print(type(rotated_image))
rotated_image.show()