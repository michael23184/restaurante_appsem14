class Venta:
    def __init__(self, usuario, producto, cantidad: int):
        self.usuario_id = usuario.identificacion
        self.producto_codigo = producto.codigo
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "total": self.total
        }

    def __str__(self):
        return f"Venta: Usuario {self.usuario_id}, Producto {self.producto_codigo}, Cantidad {self.cantidad}, Total {self.total}"