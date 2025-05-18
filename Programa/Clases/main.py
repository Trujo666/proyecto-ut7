from alumnos import Alumnos
from libro import Libros


class Main:
    def submenu_mostrar_datos(self):
        return (f"\n === Menú Principal ===               "
                "\n------------------------                "
                "\n1. Gestionar alumnos.                   "
                "\n2. Gestionar préstamos.                 "
                "\n3. Mostrar datos.                       "
                "\n           └- - - - - - - - - - - - - - "
                "\n            1. Mostrar libros.          "
                "\n            2. Mostrar cursos.          "
                "\n            3. Mostrar materias.        "
                "\n            - - - - - - - - - - - - - - ")

    def mostrar_datos(self):
        opcion_mostrar_datos: int = 0
        opcion_mostrar_libros: int = 0

        while True:
            print(self.submenu_mostrar_datos())

            opcion_mostrar_datos = int(input("Escoja una opción: "))

            match opcion_mostrar_datos:
                case 1:
                    opcion_mostrar_libros = int(input("1. Buscar libro"
                                                      "2. Mostrar todos los libros."
                                                      "3. Volver"))
                    if opcion_mostrar_libros == 1:
                        buscar_libro = input("Indique título o ISBN del libro.").strip().lower()
                        libros = Libros.cargar_libros()
                        encontrados = [libro for libro in libros if
                                       buscar_libro in libro.isbn.lower() or buscar_libro in libro.titulo.lower()]
                        if encontrados:
                            for libro in encontrados:
                                print(libro)
                        else:
                            print("Libro no encontrado.")
                    elif opcion_mostrar_libros == 2:
                        libros = Libros.cargar_libros()
                        if not libros:
                            print("No hay libros registrados.")
                        else:
                            for libro in libros:
                                print(libro)
                    elif opcion_mostrar_libros == 3:
                        continue
                    else:
                        print("Opción inválida.")

                case 2:
                    continue
                case 2:
                    continue

    def menu_crear_alumno(self):
        return ("\n === Menú Principal ==="
                "\n------------------------                "
                "\n1. Gestionar alumnos.                   "
                "\n           └- - - - - - - - - - - - - - "
                "\n            1. Crear alumno.            "
                "\n            - - - - - - - - - - - - - - "
                "\n                                        \n")

    def crear_alumno(self):
        bilingue_aux: str = ''

        print(self.menu_crear_alumno())

        print("------------------------")
        while True:
            dni = input("\nIntroduzca el DNI del alumno: ").strip().upper()
            if len(dni) == 9:
                break
            else:
                print("El DNI debe tener 9 caracteres.")

        while True:
            nombre = input("Introduzca el nombre del alumno: ").strip()
            if nombre:
                break
            else:
                print("El nombre no puede estar vacío.")

        while True:
            apellidos = input("Introduzca los apellidos del alumno: ").strip()
            if apellidos:
                break
            else:
                print("Los apellidos no pueden estar vacíos.")

        while True:
            bilingue_aux = input("Indique si el alumno es bilingüe (S/N): ").strip().upper()
            if bilingue_aux == 'S':
                bilingue = True
                break
            elif bilingue_aux == 'N':
                bilingue = False
                break
            else:
                print("Por favor, introduzca los valores 'S' o 'N'.")

        while True:
            tramo = input("Indique el tramo becado del alumno (0, I o II): ").strip().upper()
            if tramo in ["0", "I", "II"]:
                break
            else:
                print("El tramo debe ser '0', 'I' o 'II'.")
        print("------------------------\n")

        nuevo = Alumnos(dni, nombre, apellidos, bilingue, tramo)
        nuevo.guardar_en_archivo()
        print("Alumno creado con éxito.")

    def menu_modificar_alumno(self, alumno) -> str:
        return (f"\n === Menú Principal ===                           "
                "\n------------------------                           "
                "\n1. Gestionar alumnos.                              "
                "\n           └- - - - - - - - - - - - - - - - - - - -"
                "\n            1. Crear alumno.                       "
                "\n            2. Modificar alumno.                   "
                "\n                       └- - - - - - - - - - - - - -"
                "\n                        1. Modificar NIE.          "
                "\n                        2. Modificar nombre.       "
                "\n                        3. Modificar apellidos.    "
                "\n                        4. Modificar bilingüe.     "
                "\n                        5. Modificar tramo.        "
                "\n                        6. Volver al menú anterior."
                "\n                        - - - - - - - - - - - - - -")

    def modificar_alumno(self, alumno) -> None:

        opcion_modificar_alumno: int = 0

        while True:
            print(self.menu_crear_alumno())

            opcion_modificar_alumno = int(input("Escoja una opción: "))

            match opcion_modificar_alumno:
                case 1:
                    alumno.set_nie(input("Nuevo NIE: "))
                case 2:
                    alumno.set_nombre(input("Nuevo nombre: "))
                case 3:
                    alumno.set_apellidos(input("Nuevos apellidos: "))
                case 4:
                    bilingue_input = input("¿Es bilingüe? (S/N): ").strip().upper()
                    if bilingue_input == "S":
                        alumno.set_bilingue(True)
                    elif bilingue_input == "N":
                        alumno.set_bilingue(False)
                    else:
                        print("Por favor, introduzca 'S' o 'N'.")
                case 5:
                    nuevo_tramo = (input("Nuevo tramo (0, I o II): ")).strip().upper()
                    alumno.set_tramo(nuevo_tramo)
                case 6:
                    break
                case _:
                    print("Opción inválida.")

        alumnos = Alumnos.cargar_alumnos()
        with open("../Datos/alumnos.txt", "w", encoding="utf-8") as archivo:
            for alumno in alumnos:
                if alumno.nie == alumno.nie:
                    archivo.write(alumno.formato_linea() + "\n")
                else:
                    archivo.write(alumno.formato_linea() + "\n")
        print("Cambios guardados.")

    def submenu_gestionar_alumnos(self):
        return ("\n === Menú Principal ===                        "
                "\n------------------------                         "
                "\n1. Gestionar alumnos.                            "
                "\n           └- - - - - - - - - - - - - - - - - - -"
                "\n            1. Crear alumno.                     "
                "\n            2. Modificar alumno.                 "
                "\n            3. Mostrar información de alumno.    "
                "\n            4. Mostrar todos los alumnos.        "
                "\n            5. Volver al menú principal.         "
                "\n            - - - - - - - - - - - - - - - - - - -")

    def gestionar_alumnos(self):
        global alumno
        opcion_gestionar_alumnos: int = 0

        while True:
            print(self.submenu_gestionar_alumnos())

            opcion_gestionar_alumnos = int(input("Escoja una opción: "))

            match opcion_gestionar_alumnos:
                case 1:
                    self.crear_alumno()
                case 2:
                    self.modificar_alumno(alumno)
                case 3:
                    nie = input("Ingrese NIE: ")
                    alumno = Alumnos.buscar_por_nie(nie)
                    if alumno:
                        print(alumno)
                    else:
                        print("Alumno no encontrado.")
                case 4:
                    alumnos = Alumnos.cargar_alumnos()
                    if not alumnos:
                        print("No hay alumnos registrados.")
                    else:
                        for alumno in alumnos:
                            print(alumno)
                case 5:
                    break
                case _:
                    print("Opción inválida.")

    def menu_principal(self):
        return (f"\n === Menú Principal ==="
                "\n------------------------"
                "\n1. Gestionar alumnos."
                "\n2. Gestionar préstamos."
                "\n3. Mostrar datos."
                "\n4. Búsqueda avanzada."
                "\n5. Copia de seguridad."
                "\n6. Exportar datos."
                "\n7. Salir."
                "\n------------------------\n")

    def opciones_menu_principal(self):
        while True:
            print(self.menu_principal())

            opcion = int(input("Escoja una opción del menú: "))

            match opcion:
                case 1:
                    self.gestionar_alumnos()
                case 2:
                    print("Préstamos. (Pendiente)")
                case 3:
                    print("Mostrar datos. (Pendiente)")
                case 4:
                    print("Búsqueda avanzada. (Pendiente)")
                case 5:
                    print("Copia de seguridad. (Pendiente)")
                case 6:
                    print("Exportar datos. (Pendiente)")
                case 7:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción inválida, escoja una de las opciones indicadas en el menú.")


if __name__ == "__main__":
    programa = Main()
    programa.opciones_menu_principal()
