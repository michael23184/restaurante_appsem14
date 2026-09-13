class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} ({self.correo})"