from PIL import Image, ImageFilter
import os

def get_image():
    ruta = input('Ingresá la ruta de la imagen: ')
    if os.path.exists(ruta):
        return ruta
    else:
        print('El archivo no existe, intentá de nuevo')
        return get_image()


def filtro_gaussiano(imagen):
    return imagen.filter(ImageFilter.GaussianBlur(radius=2))


ruta_imagen = get_image()
imagen = Image.open(ruta_imagen) 

imagen_gaussiano = filtro_gaussiano(imagen)

if not os.path.exists('ImagenesFiltradas'):
    os.makedirs('ImagenesFiltradas')


nombre_original, extension = os.path.splitext(os.path.basename(ruta_imagen))
imagen_gaussiano.save(f'ImagenesFiltradas/{nombre_original}_Gaussiano{extension}')
print(f'Imagen guardada como ImagenesFiltradas/{nombre_original}_Gaussiano{extension}')
