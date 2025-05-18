class Alumnos:
    def __init__(self, nie, nombre, apellidos, bilingue, tramo):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.bilingue = bilingue
        self.tramo = tramo

    def __str__(self):
        return (
            f"DNI: {self.nie} | "
            f"Nombre: {self.nombre} {self.apellidos} | "
            f"Bilingüe: {'Sí' if self.bilingue else 'No'} | "
            f"Tramo: {self.tramo}"
        )

    def cambiar_objeto_a_linea(self):
        return f"{self.nie}|{self.nombre}|{self.apellidos}|{int(self.bilingue)}|{self.tramo}"

    @staticmethod
    def crear_desde_linea(linea):
        nie, nombre, apellidos, bilingue_str, tramo = linea.strip().split("|")
        bilingue = bool(int(bilingue_str))
        return Alumnos(nie, nombre, apellidos, bilingue, tramo)

    def guardar_en_archivo(self, ruta="../Datos/alumnos.txt"):
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(self.cambiar_objeto_a_linea() + "\n")

    @staticmethod
    def cargar_alumnos(ruta="../Datos/alumnos.txt"):
        alumnos = []

        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                alumnos.append(Alumnos.crear_desde_linea(linea))
        return alumnos

    @staticmethod
    def buscar_por_nie(nie_buscado, ruta="../Datos/alumnos.txt"):
        alumnos = Alumnos.cargar_alumnos(ruta)
        for alumno in alumnos:
            if alumno.nie == nie_buscado:
                return alumno
        return None

