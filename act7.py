from PIL import Image
import os


def get_ruta():
    ruta = input('Ingrese la ruta de la imagen: ')
    if os.path.exists(ruta):
        return ruta
    else:
        print('El archivo no existe. Intente nuevamente.')
        return get_ruta()


def filtro_bn(imagen):
    pixeles = imagen.load()
    for x in range(imagen.width):
        for y in range(imagen.height):
            r, g, b = pixeles[x, y][:3]  
            
            gris = int((r + g + b) / 3)
            pixeles[x, y] = (gris, gris, gris)  
    return imagen

ruta_imagen = get_ruta()
imagen = Image.open(ruta_imagen)


imagen_bn = filtro_bn(imagen)

if not os.path.exists('ImagenesFiltradas'):
    os.makedirs('ImagenesFiltradas')
nombre_original, extension = os.path.splitext(os.path.basename(ruta_imagen))   # basename extrae el nombre junto a la extensión 
imagen_bn.save(f'ImagenesFiltradas/{nombre_original}Blanco_Y_Negro{extension}')
print(f'Imagen guardada como ImagenesFiltradas/{nombre_original}Blanco_Y_Negro{extension}')
