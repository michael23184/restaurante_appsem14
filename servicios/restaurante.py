import json
from modelos.usuario import Usuario
from modelos.producto import Producto

class RestauranteServicio:
    def __init__(self, archivo_usuarios="datos/usuarios.json", archivo_productos="datos/productos.json"):
        self.archivo_usuarios = archivo_usuarios
        self.archivo_productos = archivo_productos
        self.usuarios = self.cargar_usuarios()
        self.productos = self.cargar_productos()

    # ------------------- USUARIOS -------------------
    def cargar_usuarios(self):
        """Carga los usuarios desde el archivo JSON"""
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario(**usuario) for usuario in datos]
        except FileNotFoundError:
            return []

    def validar_acceso(self, identificacion, clave):
        """Valida el acceso comparando identificacion y clave"""
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion and usuario.validar_clave(clave):
                return True
        return False

    # ------------------- PRODUCTOS -------------------
    def cargar_productos(self):
        """Carga los productos desde el archivo JSON"""
        try:
            with open(self.archivo_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return datos
        except FileNotFoundError:
            return []

    def guardar_productos(self, productos):
        """Guarda la lista de productos en el archivo JSON"""
        with open(self.archivo_productos, "w", encoding="utf-8") as f:
            json.dump(productos, f, indent=4, ensure_ascii=False)

    def registrar_producto(self, id_prod, nombre, precio, cantidad):
        """Registra un nuevo producto"""
        productos = self.cargar_productos()
        nuevo = {
            "id": id_prod,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(nuevo)
        self.guardar_productos(productos)

    def consultar_producto(self, id_prod):
        """Consulta un producto por su ID"""
        productos = self.cargar_productos()
        for prod in productos:
            if prod["id"] == id_prod:
                return prod
        return None

    def actualizar_producto(self, id_prod, nombre, precio, cantidad):
        """Actualiza la información de un producto"""
        productos = self.cargar_productos()
        for prod in productos:
            if prod["id"] == id_prod:
                prod["nombre"] = nombre
                prod["precio"] = precio
                prod["cantidad"] = cantidad
                break
        self.guardar_productos(productos)

    def eliminar_producto(self, id_prod):
        """Elimina un producto por su ID"""
        productos = self.cargar_productos()
        productos = [prod for prod in productos if prod["id"] != id_prod]
        self.guardar_productos(productos)