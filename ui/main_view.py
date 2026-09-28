import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from servicios.restaurante import RestauranteServicio

class MainView:
    def __init__(self, root, usuario):
        self.root = root
        self.servicio = RestauranteServicio()
        self.usuario = usuario
        self.root.title("Restaurante App - Principal")

        # Logo desde assets
        try:
            self.logo = PhotoImage(file="assets/logo.png")
            logo_label = tk.Label(self.root, image=self.logo)
            logo_label.pack(pady=10)
        except Exception:
            tk.Label(self.root, text="Restaurante App", font=("Arial", 16, "bold")).pack(pady=10)

        # Crear Notebook (pestañas)
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        # -------------------- Usuarios --------------------
        frame_usuarios = ttk.Frame(notebook)
        notebook.add(frame_usuarios, text="Usuarios")

        ttk.Label(frame_usuarios, text="Lista de usuarios registrados").pack(pady=10)
        self.tabla_usuarios = ttk.Treeview(frame_usuarios, columns=("id", "nombre"), show="headings")
        self.tabla_usuarios.heading("id", text="Identificación")
        self.tabla_usuarios.heading("nombre", text="Nombre")
        self.tabla_usuarios.pack(fill="x", pady=10)
        self.cargar_usuarios()

        # -------------------- Productos --------------------
        frame_productos = ttk.Frame(notebook)
        notebook.add(frame_productos, text="Productos")

        ttk.Label(frame_productos, text="Lista de productos").pack(pady=10)
        self.tabla_productos = ttk.Treeview(frame_productos, columns=("id", "nombre", "precio", "cantidad"), show="headings")
        self.tabla_productos.heading("id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre")
        self.tabla_productos.heading("precio", text="Precio")
        self.tabla_productos.heading("cantidad", text="Cantidad")
        self.tabla_productos.pack(fill="x", pady=10)
        self.cargar_productos()

        # -------------------- Ventas --------------------
        frame_ventas = ttk.Frame(notebook)
        notebook.add(frame_ventas, text="Ventas")

        # Combobox usuario
        usuarios_ids = [u.identificacion for u in self.servicio.usuarios]
        self.usuario_combo = ttk.Combobox(frame_ventas, values=usuarios_ids, state="readonly")
        self.usuario_combo.pack(pady=5)

        # Combobox producto
        productos_ids = [p["id"] for p in self.servicio.productos]
        self.producto_combo = ttk.Combobox(frame_ventas, values=productos_ids, state="readonly")
        self.producto_combo.pack(pady=5)

        # Botón registrar venta
        boton_registrar = ttk.Button(frame_ventas, text="Registrar venta", command=self.registrar_venta)
        boton_registrar.pack(pady=10)

        # Tabla ventas
        self.tabla_ventas = ttk.Treeview(frame_ventas, columns=("id", "usuario", "producto", "fecha"), show="headings")
        self.tabla_ventas.heading("id", text="ID Venta")
        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Producto")
        self.tabla_ventas.heading("fecha", text="Fecha")
        self.tabla_ventas.pack(fill="x", pady=10)
        self.refrescar_tabla()

    # -------------------- Métodos auxiliares --------------------
    def cargar_usuarios(self):
        for u in self.servicio.usuarios:
            self.tabla_usuarios.insert("", "end", values=(u.identificacion, u.nombre))

    def cargar_productos(self):
        for p in self.servicio.productos:
            self.tabla_productos.insert("", "end", values=(p["id"], p["nombre"], p["precio"], p["cantidad"]))

    def registrar_venta(self):
        usuario_id = self.usuario_combo.get()
        producto_id = self.producto_combo.get()
        try:
            nueva = self.servicio.registrar_venta(usuario_id, producto_id)
            messagebox.showinfo("Ventas", f"Venta {nueva.identificador} registrada correctamente")
            self.refrescar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def refrescar_tabla(self):
        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)
        for v in self.servicio.listar_ventas():
            self.tabla_ventas.insert("", "end", values=(v.identificador, v.usuario_id, v.producto_id, v.fecha))