class Cursos:
    def __init__(self, curso: str, nivel: str):
        self.curso = curso
        self.nivel = nivel

    def __str__(self, *args, **kwargs):
        return f"Curso: {self.curso}| Nivel: {self.nivel}"
