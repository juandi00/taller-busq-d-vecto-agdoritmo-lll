def main():

    precios_productos = {
        "shampoo": 10,
        "bloqueador": 28,
        "mascarilla": 15,
        "lima": 25,
        "esmalte": 30
    }

    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese el número de productos: "))

    if producto in precios_productos:

        precio_total = precios_productos[producto] * cantidad
        print(f"El precio de {cantidad} {producto}(s) es: {precio_total}")
    else:
        print("El producto no está en el diccionario de precios.")

if __name__ == "__main__":
    main()