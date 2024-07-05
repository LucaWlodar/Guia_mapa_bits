from PIL import Image
import os


def get_image():
    nombre_imagen = input('Ingrese el nombre de la imagen (con extensión): ')
    if os.path.exists(nombre_imagen):
        return nombre_imagen
    else:
        print('El archivo no existe. Intentá nuevamente.')
        return get_image()

def get_coords():
    x = input('Ingrese la coordenada X: ')
    y = input('Ingrese la coordenada Y: ')
    width = input('Ingrese el ancho del recorte: ')
    height = input('Ingrese la altura del recorte: ')
    
    if x.isdigit() and y.isdigit() and width.isdigit() and height.isdigit():
        return (int(x), int(y), int(width), int(height))
    else:
        print('Ingrese un número entero e intente nuevamente')
        return get_coords()

nombre_imagen = get_image()
img = Image.open(nombre_imagen)

x, y, width, height = get_coords()

if x + width <= img.width and y + height <= img.height:
    if not os.path.exists('recortes'):
        os.makedirs('recortes')

    recorte = img.crop((x, y, x + width, y + height))
    
    num_recortes = len(os.listdir('recortes'))
    recorte.save(f'recortes/recorte{num_recortes + 1}.png')
    print(f'Recorte guardado como recortes/recorte{num_recortes + 1}.png')
else:
    print('Recorte no válido')
