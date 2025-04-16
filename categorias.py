# categorias.py

from database import get_db_connection

print("📂 Archivo categorias.py se ha importado correctamente.")

def crear_categoria(nombre):
    print("🛠️ Ejecutando crear_categoria")
    if not nombre.strip():
        print("⚠️ El nombre de la categoría no puede estar vacío.")
        return

    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", (nombre,))
            conexion.commit()
            print("✅ Categoría creada correctamente.")
        except Exception as e:
            print("❌ Error al crear la categoría:", e)
        finally:
            cursor.close()
            conexion.close()

def listar_categorias():
    print("📚 Listando categorías...")
    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM categorias")
            categorias = cursor.fetchall()

            if not categorias:
                print("⚠️ No hay categorías registradas.")
            else:
                print("📦 Categorías disponibles:")
                for cat in categorias:
                    print(f"ID: {cat[0]} - Nombre: {cat[1]}")
        except Exception as e:
            print("❌ Error al listar categorías:", e)
        finally:
            cursor.close()
            conexion.close()
