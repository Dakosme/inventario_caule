# menu.py

from categorias import listar_categorias, crear_categoria
from productos import listar_productos, crear_producto, actualizar_producto, eliminar_producto

def menu_categorias():
    while True:
        print("\n📚 MENÚ DE CATEGORÍAS")
        print("1. Listar categorías")
        print("2. Crear nueva categoría")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_categorias()

        elif opcion == "2":
            nombre = input("Nombre de la nueva categoría: ")
            crear_categoria(nombre)

        elif opcion == "3":
            break

        else:
            print("❌ Opción no válida. Intenta nuevamente.")


def menu_productos():
    while True:
        print("\n📦 MENÚ DE PRODUCTOS")
        print("1. Listar productos")
        print("2. Crear nuevo producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_productos()

        elif opcion == "2":
            listar_categorias()
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción: ")
            categoria_id = int(input("ID de categoría: "))
            tipo_id = int(input("ID de tipo de producto (1 = Materia prima, 2 = Producto final): "))
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad en stock: "))
            crear_producto(nombre, descripcion, categoria_id, tipo_id, precio, cantidad)

        elif opcion == "3":
            listar_productos()
            id_producto = int(input("ID del producto a actualizar: "))
            listar_categorias()
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            categoria_id = int(input("Nuevo ID de categoría: "))
            tipo_id = int(input("Nuevo ID de tipo de producto: "))
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad en stock: "))
            actualizar_producto(id_producto, nombre, descripcion, categoria_id, tipo_id, precio, cantidad)

        elif opcion == "4":
            listar_productos()
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)

        elif opcion == "5":
            break

        else:
            print("❌ Opción no válida. Intenta nuevamente.")


def menu_principal():
    while True:
        print("\n🔧 MENÚ PRINCIPAL")
        print("1. Gestionar Categorías")
        print("2. Gestionar Productos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_categorias()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar menú principal
if __name__ == "__main__":
    menu_principal()
