import json
from datetime import date
from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self, archivo_usuarios="datos/usuarios.json", archivo_productos="datos/productos.json", archivo_ventas="datos/ventas.json"):
        self.archivo_usuarios = archivo_usuarios
        self.archivo_productos = archivo_productos
        self.archivo_ventas = archivo_ventas
        self.usuarios = self.cargar_usuarios()
        self.productos = self.cargar_productos()
        self.ventas = self.cargar_ventas()

    # -------------------- USUARIOS --------------------
    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario(**usuario) for usuario in datos]
        except FileNotFoundError:
            return []

    def validar_acceso(self, identificacion, clave):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion and usuario.clave == clave:
                return usuario
        return None

    # -------------------- PRODUCTOS --------------------
    def cargar_productos(self):
        try:
            with open(self.archivo_productos, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_productos(self, productos):
        with open(self.archivo_productos, "w", encoding="utf-8") as f:
            json.dump(productos, f, indent=4, ensure_ascii=False)

    def registrar_producto(self, id_prod, nombre, precio, cantidad):
        productos = self.cargar_productos()
        nuevo = {"id": id_prod, "nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(nuevo)
        self.guardar_productos(productos)

    def consultar_producto(self, id_prod):
        productos = self.cargar_productos()
        for prod in productos:
            if prod["id"] == id_prod:
                return prod
        return None

    def actualizar_producto(self, id_prod, nombre, precio, cantidad):
        productos = self.cargar_productos()
        for prod in productos:
            if prod["id"] == id_prod:
                prod["nombre"] = nombre
                prod["precio"] = precio
                prod["cantidad"] = cantidad
                break
        self.guardar_productos(productos)

    def eliminar_producto(self, id_prod):
        productos = self.cargar_productos()
        productos = [prod for prod in productos if prod["id"] != id_prod]
        self.guardar_productos(productos)

    # -------------------- VENTAS --------------------
    def cargar_ventas(self):
        try:
            with open(self.archivo_ventas, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta(**venta) for venta in datos]
        except FileNotFoundError:
            return []

    def guardar_ventas(self):
        datos = [v.to_dict() for v in self.ventas]
        with open(self.archivo_ventas, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def generar_id_venta(self):
        return f"V{len(self.ventas)+1:03d}"

    def registrar_venta(self, usuario_id, producto_id):
        if not usuario_id or not producto_id:
            raise ValueError("Debe seleccionar usuario y producto")

        if not any(u.identificacion == usuario_id for u in self.usuarios):
            raise ValueError("Usuario no existe")

        if not any(p["id"] == producto_id for p in self.productos):
            raise ValueError("Producto no existe")

        nueva = Venta(
            identificador=self.generar_id_venta(),
            usuario_id=usuario_id,
            producto_id=producto_id,
            fecha=date.today().isoformat()
        )
        self.ventas.append(nueva)
        self.guardar_ventas()
        return nueva

    def listar_ventas(self):
        return self.ventas