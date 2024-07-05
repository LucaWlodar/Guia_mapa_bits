from PIL import Image
import os


def get_image(prompt):
    ruta = input(prompt)
    if os.path.exists(ruta):
        return ruta
    else:
        print('El archivo no existe, probá de nuevo')
        return get_image(prompt)


def get_watermark():
    print('Seleccioná la posición para la marca de agua:')
    print('1. Superior izquierda')
    print('2. Superior derecha')
    print('3. Inferior izquierda')
    print('4. Inferior derecha')
    posicion = input('Ingresá el número correspondiente a la posición: ')
    
    if posicion in ['1', '2', '3', '4']:
        return int(posicion)
    else:
        print('Entrada no válida. Intente nuevamente.')
        return get_watermark()


ruta_imagen = get_image('Ingresá la ruta de la imagen para poner la marca de agua: ')
ruta_watermark = get_image('Ingresá la ruta de la imagen de la marca de agua: ')

img = Image.open(ruta_imagen)
watermark = Image.open(ruta_watermark)

posicion = get_watermark()


img_width, img_height = img.size
watermark_width, watermark_height = watermark.size


margen = 50
if posicion == 1:
    x = margen
    y = margen
elif posicion == 2:
    x = img_width - watermark_width - margen
    y = margen
elif posicion == 3:
    x = margen
    y = img_height - watermark_height - margen
elif posicion == 4:
    x = img_width - watermark_width - margen
    y = img_height - watermark_height - margen


img.paste(watermark, (x, y), watermark)


nombre_original, extension = os.path.splitext(ruta_imagen)
img.save(f'{nombre_original}_watermarked{extension}')
print(f'Imagen guardada como {nombre_original}_watermark{extension}')
