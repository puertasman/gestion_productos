""" Gestión de conexiones a la base de datos
con un pool de conexiones"""

import os
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv

load_dotenv()  # Carga las variables desde un archivo .env

class Conexion:
    """Clase para gestionar la conexión a la base de datos con pool de conexiones"""

    DATABASE = os.getenv('DB_NAME')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = int(os.getenv('DB_PORT', '3306'))  # Este sí puede tener valor por defecto
    HOST = os.getenv('DB_HOST')
    POOLSIZE = int(os.getenv('DB_POOLSIZE', '5'))
    POOL_NAME = os.getenv('DB_POOL_NAME', 'inventario_pool')
    pool = None

    @classmethod
    def iniciar_pool(cls):
        if cls.pool is None:
            cls.pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=cls.POOL_NAME,
                pool_size=cls.POOLSIZE,
                host=cls.HOST,
                database=cls.DATABASE,
                user=cls.USERNAME,
                password=cls.PASSWORD,
                port=cls.DB_PORT
            )

    @classmethod
    def obtener_conexion(cls):
        if cls.pool is None:
            cls.iniciar_pool()
        return cls.pool.get_connection()