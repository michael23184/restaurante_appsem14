import json
from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

class ArchivoServicio:
    # ------------------ USUARIOS ------------------
    def leer_usuarios(self) -> list[Usuario]:
        try:
            with open("datos/usuarios.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Usuario(u["identificacion"], u["nombre"], u["correo"]) for u in data]
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        with open("datos/usuarios.json", "w", encoding="utf-8") as f:
            json.dump([u.__dict__ for u in usuarios], f, indent=4)

    # ------------------ PRODUCTOS ------------------
    def leer_productos(self) -> list[Producto]:
        try:
            with open("datos/productos.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Producto(p["codigo"], p["nombre"], p["precio"], p["stock"]) for p in data]
        except FileNotFoundError:
            return []

    def guardar_productos(self, productos: list[Producto]) -> None:
        with open("datos/productos.json", "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in productos], f, indent=4)

    # ------------------ VENTAS ------------------
    def leer_ventas(self) -> list[Venta]:
        try:
            with open("datos/ventas.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                ventas = []
                for v in data:
                    dummy = VentaDummy(v["usuario_id"], v["producto_codigo"], v["cantidad"], v["total"])
                    ventas.append(dummy)
                return ventas
        except FileNotFoundError:
            return []

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        with open("datos/ventas.json", "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in ventas], f, indent=4)

# Clase auxiliar para reconstruir ventas desde JSON
class VentaDummy(Venta):
    def __init__(self, usuario_id, producto_codigo, cantidad, total):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        self.total = total

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "total": self.total
        }