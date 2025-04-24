""" productos para meter en la base de datos """

class Producto:
    def __init__(self, nombre, cantidad, precio, categoria, id=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.cantidad} uds - {self.precio} € - Categoría: {self.categoria}"
