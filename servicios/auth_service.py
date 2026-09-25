import json
from modelos.usuario import Usuario

class AuthService:
    def __init__(self, ruta_usuarios="datos/usuarios.json"):
        self.ruta_usuarios = ruta_usuarios

    def validar_acceso(self, correo, clave):
        try:
            with open(self.ruta_usuarios, "r") as f:
                usuarios = json.load(f)
            for u in usuarios:
                usuario = Usuario(
                    identificacion=u["identificacion"],
                    nombre=u["nombre"],
                    correo=u["correo"],
                    clave=u["clave"]
                )
                if usuario.correo == correo and usuario.validar_clave(clave):
                    return True, usuario
            return False, None
        except Exception as e:
            print("Error al validar acceso:", e)
            return False, None