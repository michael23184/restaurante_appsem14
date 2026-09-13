import tkinter as tk
from modelos.venta import Venta

class MainView:
    def __init__(self, root, restaurante, servicio=None):
        self.root = root
        self.restaurante = restaurante
        self.servicio = servicio

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # Titulo principal
        tk.Label(self.frame, text="Usuarios registrados", font=("Arial", 14, "bold")).pack(pady=10)

        for u in self.restaurante.listar_usuarios():
            tk.Label(self.frame, text=f"{u.identificacion} - {u.nombre} - {u.correo}").pack()

        tk.Label(self.frame, text="").pack()

        tk.Label(self.frame, text="Productos disponibles", font=("Arial", 14, "bold")).pack(pady=10)

        for p in self.restaurante.listar_productos():
            tk.Label(self.frame, text=f"{p.codigo} - {p.nombre} - Precio: {p.precio} - Stock: {p.stock}").pack()

        # ------------------ FORMULARIO DE VENTA ------------------
        tk.Label(self.frame, text="Registrar nueva venta", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.frame, text="Usuario ID:").pack()
        self.usuario_entry = tk.Entry(self.frame)
        self.usuario_entry.pack()

        tk.Label(self.frame, text="Producto codigo:").pack()
        self.producto_entry = tk.Entry(self.frame)
        self.producto_entry.pack()

        tk.Label(self.frame, text="Cantidad:").pack()
        self.cantidad_entry = tk.Entry(self.frame)
        self.cantidad_entry.pack()

        tk.Button(self.frame, text="Registrar venta", command=self.registrar_venta).pack(pady=10)

        self.mensaje_label = tk.Label(self.frame, text="", fg="green")
        self.mensaje_label.pack()

        # Boton salir
        tk.Button(self.frame, text="Cerrar sesion", command=self.root.destroy).pack(pady=20)

    def registrar_venta(self):
        usuario_id = self.usuario_entry.get().strip()
        producto_codigo = self.producto_entry.get().strip()
        try:
            cantidad = int(self.cantidad_entry.get().strip())
        except ValueError:
            self.mensaje_label.config(text="Error: la cantidad debe ser un numero", fg="red")
            return

        usuario = self.restaurante.buscar_usuario(usuario_id)
        producto = self.restaurante.buscar_producto(producto_codigo)

        if usuario and producto:
            try:
                nueva_venta = Venta(usuario, producto, cantidad)
                self.restaurante.registrar_venta(nueva_venta, self.servicio)
                self.mensaje_label.config(text="Venta registrada con exito", fg="green")
            except ValueError as e:
                self.mensaje_label.config(text=f"Error: {str(e)}", fg="red")
        else:
            self.mensaje_label.config(text="Error: usuario o producto no encontrado", fg="red")