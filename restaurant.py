import funciones as fn

print("""Menú:
1. Ver restaurant
2. Reservar mesa
3. Carta
4. Pagar
5. Cancelar
6. Salir""")

opcion = fn.validar_opcion()

while True:
    if opcion==1:
        mesas = fn.mostrar_mesas()
    elif opcion==2:
        rut = fn.validar_rut()
        nombre = fn.validar_nombre()
        correo = fn.validar_correo()
    elif opcion==3:
        rut = fn.validar_rut()
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        print("Gracias, adios")
        break

