def crear_carrito():
    carrito = {}
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'fin' para finalizar la compra): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del artículo: "))
        carrito[articulo] = precio
    return carrito

def mostrar_carrito(carrito):
    print("\nLista de la compra:")
    total = 0
    for articulo, precio in carrito.items():
        print(f"{articulo}: ${precio:.2f}")
        total += precio
    print(f"Total a pagar: ${total:.2f}")

def main():
    print("¡Bienvenido al carrito de compras!")
    carrito = crear_carrito()
    mostrar_carrito(carrito)

if __name__ == "__main__":
    main()