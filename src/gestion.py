""" Gestión del inventario de productos """

from conexion import Conexion
from producto import Producto
import mysql.connector

class GestionInventario:
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
    #     try:
    #     conexion = Conexion.obtener_conexion()
    #     cursor = conexion.cursor()
    #     cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
    #     resultados = cursor.fetchall()

    #     if resultados:
    #         print("\n📦 Lista de productos:")
    #         for fila in resultados:
    #             id, nombre, cantidad, precio, categoria = fila
    #             print(f"[{id}] {nombre} - {cantidad} uds - {precio} € - Categoría: {categoria}")
    #     else:
    #         print("⚠️ No hay productos en el inventario.")
    # except mysql.connector.Error as err:
    #     print("❌ Error al mostrar productos:", err)
    # finally:
    #     if 'cursor' in locals():
    #         cursor.close()
    #     if 'conexion' in locals():
    #         conexion.close()
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
            resultados = cursor.fetchall()
            print(resultados)
        except mysql.connector.Error as e:
            print("❌ Error al agregar producto:", err)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
