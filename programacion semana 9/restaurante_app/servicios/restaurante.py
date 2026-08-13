from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    # --- Productos ---
    def registrar_producto(self, producto: Producto) -> bool:
        if any(p.codigo == producto.codigo for p in self.productos):
            print("⚠️ Código duplicado. No se puede registrar.")
            return False
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> None:
        for p in self.productos:
            print(p)

    def mostrar_categorias(self) -> None:
        categorias = {p.categoria for p in self.productos}  # uso de set
        print("Categorías únicas:", categorias)

    # --- Usuarios ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(u.identificacion == usuario.identificacion for u in self.usuarios):
            print("⚠️ Identificación duplicada. No se puede registrar.")
            return False
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> None:
        for u in self.usuarios:
            print(u)
