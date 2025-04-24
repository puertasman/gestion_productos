""" productos para meter en la base de datos """

class Producto:
    """ Estructura de un producto para la base de datos"""
    def __init__(self, nombre, cantidad, precio, categoria, id=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        """ Devuelve la representación del producto como cadena para el print """
        return f"[{self.id}] {self.nombre} - {self.cantidad} uds - {self.precio} € - Categoría: {self.categoria}"
