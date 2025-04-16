# productos.py

from database import get_db_connection

def listar_productos():
    """Muestra todos los productos registrados."""
    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.id, p.nombre, p.precio, p.cantidad, c.nombre AS categoria, t.nombre AS tipo
                FROM productos p
                LEFT JOIN categorias c ON p.categoria_id = c.id
                LEFT JOIN tipos_producto t ON p.tipo_id = t.id
            """)
            productos = cursor.fetchall()

            print("\n📦 Lista de productos:")
            for prod in productos:
                print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: {prod[2]} | Cantidad: {prod[3]} | Categoría: {prod[4]} | Tipo: {prod[5]}")

        except Exception as e:
            print("❌ Error al listar productos:", e)
        finally:
            cursor.close()
            conexion.close()


def crear_producto(nombre, descripcion, categoria_id, tipo_id, precio, cantidad):
    """Crea un nuevo producto con los datos ingresados."""
    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO productos (nombre, descripcion, categoria_id, tipo_id, precio, cantidad)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, descripcion, categoria_id, tipo_id, precio, cantidad)
            cursor.execute(sql, valores)
            conexion.commit()
            print("✅ Producto creado exitosamente.")
        except Exception as e:
            print("❌ Error al crear producto:", e)
        finally:
            cursor.close()
            conexion.close()


def actualizar_producto(id_producto, nombre, descripcion, categoria_id, tipo_id, precio, cantidad):
    """Actualiza un producto existente."""
    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """
                UPDATE productos
                SET nombre = %s, descripcion = %s, categoria_id = %s, tipo_id = %s, precio = %s, cantidad = %s
                WHERE id = %s
            """
            valores = (nombre, descripcion, categoria_id, tipo_id, precio, cantidad, id_producto)
            cursor.execute(sql, valores)
            conexion.commit()
            print("✅ Producto actualizado correctamente.")
        except Exception as e:
            print("❌ Error al actualizar producto:", e)
        finally:
            cursor.close()
            conexion.close()


def eliminar_producto(id_producto):
    """Elimina un producto por su ID."""
    conexion = get_db_connection()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
            conexion.commit()
            print("🗑️ Producto eliminado correctamente.")
        except Exception as e:
            print("❌ Error al eliminar producto:", e)
        finally:
            cursor.close()
            conexion.close()
