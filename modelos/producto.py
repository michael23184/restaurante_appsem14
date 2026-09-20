class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario para guardar en JSON"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    def __str__(self):
        return f"{self.id} - {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"
