""" Módulo para gestionar la conexión a la base de datos y los productos"""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gestion import GestionInventario
from producto import Producto

# producto_nuevo = Producto(nombre="Cerveza IPA", cantidad=50, precio=2.99, categoria="Bebidas")
# GestionInventario.agregar_producto(producto_nuevo)

GestionInventario.mostrar_productos()