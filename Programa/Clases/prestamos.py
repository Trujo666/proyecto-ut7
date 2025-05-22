class Prestamos:
    def __init__(self, fecha_prestamo, fecha_devolucion, estado):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str_(self):
        return (f"Fecha de prestamo: {self.fecha_prestamo} | "
                f"Fecha de devolucion: {self.fecha_devolucion} | "
                f"Estado de prestamo: {self.estado}")
