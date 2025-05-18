
class Libros:
    def __init__(self, isbn: str, titulo: str, autor: str, n_ejemplares: int, estado: bool, id_materia: int,
                 id_curso: int) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.n_ejemplares = n_ejemplares
        self.estado = estado
        self.id_materia = id_materia
        self.id_curso = id_curso


    def __str__(self):
        return (f"ISBN: {self.isbn} | "
                f"Titulo: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"Estado: {self.estado} | "
                f"ID: {self.id_materia} | "
                f"Curso: {self.id_curso}")




# cambiar_objeto_a_linea()
#
# crear_desde_linea()
#
# guardar_en_archivo()
#
# cargar_libros()


