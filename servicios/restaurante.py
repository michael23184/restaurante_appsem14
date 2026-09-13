from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    def __init__(self) -> None:
        self.usuarios: list[Usuario] = []
        self.productos: list[Producto] = []
        self.ventas: list[Venta] = []

    # ------------------ CARGA DE DATOS ------------------
    def cargar_datos(self, archivo_servicio) -> None:
        self.usuarios = archivo_servicio.leer_usuarios()
        self.productos = archivo_servicio.leer_productos()
        self.ventas = archivo_servicio.leer_ventas()

    # ------------------ USUARIOS ------------------
    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(u.identificacion == usuario.identificacion for u in self.usuarios):
            raise ValueError("Ya existe un usuario con esa identificacion.")
        self.usuarios.append(usuario)

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    # ------------------ PRODUCTOS ------------------
    def registrar_producto(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self.productos):
            raise ValueError("Ya existe un producto con ese codigo.")
        self.productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> None:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            producto.stock = stock
        else:
            raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
        else:
            raise ValueError("Producto no encontrado.")

    # ------------------ VENTAS ------------------
    def registrar_venta(self, venta: Venta, archivo_servicio=None) -> None:
        producto = self.buscar_producto(venta.producto_codigo)
        if producto and producto.stock >= venta.cantidad:
            producto.stock -= venta.cantidad
            self.ventas.append(venta)
            if archivo_servicio:
                archivo_servicio.guardar_ventas(self.ventas)
                archivo_servicio.guardar_productos(self.productos)
        else:
            raise ValueError("Stock insuficiente o producto no encontrado.")

    def listar_ventas(self) -> list[Venta]:
        return self.ventas

    # ------------------ LOGIN ------------------
    def validar_acceso(self, identificacion: str, clave: str) -> bool:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return True
        return False