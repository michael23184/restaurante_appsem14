class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        self._precio = valor

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def to_dict(self) -> dict:
        """Convierte el producto a diccionario para JSON"""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} (${self.precio}) Stock: {self.stock}"
