""" Gestión del inventario de productos """

from src.conexion import Conexion
from src.producto import Producto
import mysql.connector

class GestionInventario:
    """" Clase para gestionar el inventario de productos"""
    @staticmethod
    def agregar_producto(producto: Producto):
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
            return True
        except mysql.connector.IntegrityError as e:
            print(e)
            return False
        except mysql.connector.Error as err:
            print("❌ Error al agregar producto:", err)
            return False
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

    @staticmethod
    def obtener_todos():
        productos = []
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
            filas = cursor.fetchall()
            for fila in filas:
                productos.append({
                    'id': fila[0],
                    'nombre': fila[1],
                    'cantidad': fila[2],
                    'precio': fila[3],
                    'categoria': fila[4]
                })
        except mysql.connector.Error as err:
            print("❌ Error al obtener productos:", err)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
        return productos

    @staticmethod
    def eliminar_producto(id_producto):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
            conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print("❌ Error al eliminar producto:", err)
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()

