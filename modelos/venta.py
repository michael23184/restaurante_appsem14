from datetime import date

class Venta:
    def __init__(self, identificador, usuario_id, producto_id, fecha=None):
        self.identificador = identificador
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.fecha = fecha if fecha else date.today().isoformat()

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha
        }