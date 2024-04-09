def busqueda_secuencial(lista, cedula):
    """
    Realiza una búsqueda secuencial en una lista de cédulas para determinar si la cédula dada está presente.
    Devuelve True si la cédula está en la lista, False en caso contrario.
    """
    for ced in lista:
        if ced == cedula:
            return True
    return False


cedulas_validas = [1005674582, 43786945, 44657892, 1033468523]


cedula_ingresada = int(input("Ingrese su número de cédula: "))


if busqueda_secuencial(cedulas_validas, cedula_ingresada):
    print("Puede votar en las elecciones presidenciales.")
else:
    print("No puede votar en las elecciones presidenciales.")



