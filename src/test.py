from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

print("DEBUG -> DB_USER:", os.getenv('DB_USER'))
print("DEBUG -> DB_NAME:", os.getenv('DB_NAME'))
print("DEBUG -> DB_HOST:", os.getenv('DB_HOST'))

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        charset=os.getenv("DB_CHARSET", "utf8mb4")
    )
    print("✅ Conexión exitosa a la base de datos")
    conn.close()
except mysql.connector.Error as err:
    print("❌ Error al conectar:", err)
