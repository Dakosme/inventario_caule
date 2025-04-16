import mysql.connector

print("🔌 Probando conexión manual...")

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",         # cambia si es necesario
        user="root",
        password="",
        database="inventario_botanica",
        port=3306,
        connection_timeout=5     # <- si no conecta en 5 segundos, lanza error
    )
    print("✅ ¡Conexión exitosa!")
    conexion.close()
except mysql.connector.Error as err:
    print("❌ Error al conectar con MySQL:")
    print(err)
