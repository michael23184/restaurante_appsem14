import json
from modelos.usuario import Usuario

class AuthService:
    def __init__(self, ruta_usuarios="datos/usuarios.json"):
        self.ruta_usuarios = ruta_usuarios

    def validar_acceso(self, correo, clave):
        try:
            # Abrimos el archivo en UTF-8 para evitar problemas de lectura
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                usuarios = json.load(f)

            # Recorremos cada usuario en el JSON
            for u in usuarios:
                usuario = Usuario(
                    identificacion=u["identificacion"],
                    nombre=u["nombre"],
                    correo=u["correo"],
                    clave=u["clave"]
                )
                # Validamos correo y clave
                if usuario.correo == correo and usuario.validar_clave(clave):
                    return True, usuario

            # Si no coincide ninguno
            return False, None

        except Exception as e:
            print("Error al validar acceso:", e)
            return False, None