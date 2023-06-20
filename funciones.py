import numpy
arreglo_restaurant = numpy.zeros((3,3),int)

lista_rut = []
lista_nombre = []
lista_correo = []


def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! debe ingresar una opcion entre 1 y 6!")
           
        except:
            print("ERROR! debe ingresar un número entero")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut (sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! debe ingresar el rut sin puntos sin dígito verificador!")
        except:
            print("ERROR! debe ingresar un número entero")
        lista_rut.append(rut)
        
def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! debe ingresar un nombre que tenga como minimo 3 caracteres!")
        lista_nombre.append(nombre)
def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! debe ingresar su correo con @")
        lista_correo.append(correo)

def mostrar_mesas():
    for x in range(3):
        for y in range(3):
            print(arreglo_restaurant[x][y], end=" ")
    print()
    
        