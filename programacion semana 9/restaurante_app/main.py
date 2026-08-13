from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

def main():
    restaurante = Restaurante()

    # Tupla con opciones fijas del menú
    opciones = (
        "Registrar producto",
        "Buscar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Listar productos",
        "Registrar usuario",
        "Listar usuarios",
        "Mostrar categorías",
        "Salir"
    )

    # Diccionario que relaciona opción → función
    acciones = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante),
        "4": lambda: eliminar_producto(restaurante),
        "5": restaurante.listar_productos,
        "6": lambda: registrar_usuario(restaurante),
        "7": restaurante.listar_usuarios,
        "8": restaurante.mostrar_categorias,
        "9": exit
    }

    while True:
        print("\n=== SISTEMA DE RESTAURANTE ===")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")
        eleccion = input("Seleccione una opción: ")

        accion = acciones.get(eleccion)
        if accion:
            accion()
        else:
            print("⚠️ Opción inválida.")

# --- Funciones auxiliares ---
def registrar_producto(restaurante: Restaurante):
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    producto = Producto(codigo, nombre, categoria, precio)
    restaurante.registrar_producto(producto)

def buscar_producto(restaurante: Restaurante):
    codigo = input("Código a buscar: ")
    producto = restaurante.buscar_producto(codigo)
    print(producto if producto else "Producto no encontrado.")

def actualizar_producto(restaurante: Restaurante):
    codigo = input("Código: ")
    nombre = input("Nuevo nombre: ")
    categoria = input("Nueva categoría: ")
    precio = float(input("Nuevo precio: "))
    if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(restaurante: Restaurante):
    codigo = input("Código a eliminar: ")
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def registrar_usuario(restaurante: Restaurante):
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    usuario = Usuario(identificacion, nombre, correo)
    restaurante.registrar_usuario(usuario)

if __name__ == "__main__":
    main()
