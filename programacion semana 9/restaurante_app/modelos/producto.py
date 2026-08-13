from typing import Any

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio:.2f}"
