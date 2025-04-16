import mysql.connector

def get_db_connection():
    print("🔌 Intentando conectar a la base de datos...")
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventario_botanica",
            port=3306
        )
        print("✅ Conexión creada correctamente.")
        return conn
    except mysql.connector.Error as err:
        print("❌ Error al conectar con MySQL:")
        print(err)  # <- FORZAMOS que el error se imprima
        return None
