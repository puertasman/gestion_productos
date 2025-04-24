""" Gestión del inventario de productos """

from conexion import Conexion
from producto import Producto
import mysql.connector

class GestionInventario:
    """" Clase para gestionar el inventario de productos"""
    @staticmethod
    def agregar_producto(producto: Producto):
        """ Agrega un producto a la base de datos"""
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            query = """
                INSERT INTO productos (nombre, cantidad, precio, categoria)
                VALUES (%s, %s, %s, %s)
            """
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(query, valores)
            conexion.commit()
            print("✅ Producto agregado correctamente")
        except mysql.connector.IntegrityError as e:
            if "Duplicate entry" in str(e):
                print("❌ Error: Ya existe un producto con ese nombre.")
            else:
                print("❌ Error de integridad:", e)
        except mysql.connector.Error as err:
            print("❌ Error al agregar producto:", err)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()


    @staticmethod
    def mostrar_productos():
        """ Muestra todos los productos de la base de datos """
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
            resultados = cursor.fetchall()
            print(resultados)
        except mysql.connector.Error as e:
            print("❌ Error al agregar producto:", e)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
