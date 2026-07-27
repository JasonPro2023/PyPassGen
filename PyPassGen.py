# PyPassGen: Un sencillo generador de contraseñas en Python, hecho originalmente en 2023, ahora mejorado y con comentarios para explicar su funcionamiento.
# Este generador permite al usuario especificar la longitud de la contraseña y genera una combinación aleatoria de caracteres alfabéticos, numéricos y especiales.

import random
import math

alfabeto = "abcdefghijklmnopqrstuvwxyz"
numero = "0123456789"
car_especial = "@#$%&*"

# El usuario escribe la longitud de la contraseña, puede ser cualquier longitud
while True:
    try:
        lon_con = int(input("Ingresa la longitud de la contraseña: "))
        if lon_con <= 0:
            raise ValueError
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
    except EOFError:
        print("Por favor, ingresa un valor válido.")

# calcular la cantidad de caracteres alfabéticos, numéricos y especiales según la longitud de la contraseña.
lon_alfabeto = lon_con//2 #dividir la longitud de la contraseña entre 2
lon_num = math.ceil(lon_con*30/100) #30% de la longitud de la contraseña
lon_especial = lon_con-(lon_alfabeto+lon_num) #la longitud de la contraseña menos la longitud de los caracteres alfabéticos y numéricos


contrasena = []

# función para generar la contraseña, recibe la longitud, el array de caracteres y un booleano para saber si es alfabético o no
# se utiliza un for para recorrer la longitud de la contraseña
# después se utiliza un random para seleccionar un caracter del array y se agrega a la contraseña
# luego se utiliza un if para saber si es alfabético o no
# luego se utiliza un random para seleccionar si es mayúscula o minúscula
# finalmente se agrega el caracter a la contraseña
def generar_contrasena(length, array, is_alpha=False):
    for i in range(length):
        indice = random.randint(0, len(array) - 1)
        caracter = array[indice]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                caracter = caracter.upper()
        contrasena.append(caracter)


# contraseña alfabética
generar_contrasena(lon_alfabeto, alfabeto, True)
# contraseña numérica
generar_contrasena(lon_num, numero)
# contrasena caracter especial
generar_contrasena(lon_especial, car_especial)
# realizar un shuffle de la contraseña para que no se vea el patrón de los caracteres
random.shuffle(contrasena)
# convertir la contrasena a string
gen_con = ""
# imprimir la contrasena
for i in contrasena:
    gen_con = gen_con + str(i)
print("Contraseña generada: " + gen_con)
input("Presiona Enter para salir...")