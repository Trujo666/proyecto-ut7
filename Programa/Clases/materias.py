class Materias:
    def __init__(self, id_materia, nombre_materia, departamento):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.departamento = departamento

    def __str__(self):
        return (f"--------------------------------"
                f"ID: {self.id_materia}"
                f"Nombre: {self.nombre_materia} "
                f"Departamento: {self.departamento}"
                f"--------------------------------")
