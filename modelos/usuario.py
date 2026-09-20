class Usuario:
    def __init__(self, identificacion, nombre, correo, clave):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.clave = clave

    def validar_clave(self, clave_ingresada):
        """Verifica si la clave ingresada coincide con la clave del usuario"""
        return self.clave == clave_ingresada

    def __str__(self):
        return f"{self.identificacion} - {self.nombre} - {self.correo}"