def main():

    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]


    notas = {}

    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas[asignatura] = nota

    print("\nNotas del curso:")
    for asignatura, nota in notas.items():
        print(f"En {asignatura} has sacado {nota}")


if __name__ == "__main__":
    main()