import tkinter as tk
from tkinter import ttk
from servicios.restaurante import RestauranteServicio

class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.servicio = RestauranteServicio()
        self.pack(fill="both", expand=True)
        self.crear_componentes()

    def crear_componentes(self):
        # Contenedor principal dividido en secciones
        self.frame_navegacion = tk.Frame(self, bg="#f0f0f0", height=50)
        self.frame_navegacion.pack(fill="x")

        self.frame_formulario = tk.Frame(self, bg="#ffffff", height=150)
        self.frame_formulario.pack(fill="x", padx=10, pady=10)

        self.frame_visualizacion = tk.Frame(self, bg="#e0e0e0")
        self.frame_visualizacion.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Navegacion ---
        btn_usuarios = tk.Button(self.frame_navegacion, text="Usuarios", command=self.mostrar_usuarios)
        btn_usuarios.pack(side="left", padx=5, pady=5)

        btn_productos = tk.Button(self.frame_navegacion, text="Productos", command=self.mostrar_productos)
        btn_productos.pack(side="left", padx=5, pady=5)

        # --- Formulario de productos ---
        tk.Label(self.frame_formulario, text="ID Producto:").grid(row=0, column=0, sticky="w")
        self.entry_id = tk.Entry(self.frame_formulario)
        self.entry_id.grid(row=0, column=1)

        tk.Label(self.frame_formulario, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.entry_nombre = tk.Entry(self.frame_formulario)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(self.frame_formulario, text="Precio:").grid(row=2, column=0, sticky="w")
        self.entry_precio = tk.Entry(self.frame_formulario)
        self.entry_precio.grid(row=2, column=1)

        tk.Label(self.frame_formulario, text="Cantidad:").grid(row=3, column=0, sticky="w")
        self.entry_cantidad = tk.Entry(self.frame_formulario)
        self.entry_cantidad.grid(row=3, column=1)

        # Botones de accion
        btn_registrar = tk.Button(self.frame_formulario, text="Registrar", command=self.registrar_producto)
        btn_registrar.grid(row=4, column=0, pady=5)

        btn_consultar = tk.Button(self.frame_formulario, text="Consultar", command=self.consultar_producto)
        btn_consultar.grid(row=4, column=1, pady=5)

        btn_actualizar = tk.Button(self.frame_formulario, text="Actualizar", command=self.actualizar_producto)
        btn_actualizar.grid(row=5, column=0, pady=5)

        btn_eliminar = tk.Button(self.frame_formulario, text="Eliminar", command=self.eliminar_producto)
        btn_eliminar.grid(row=5, column=1, pady=5)

        # --- Visualizacion de productos ---
        self.tabla = ttk.Treeview(self.frame_visualizacion, columns=("id", "nombre", "precio", "cantidad"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.pack(fill="both", expand=True)

        self.cargar_productos()

    # --- Metodos de accion ---
    def registrar_producto(self):
        id_prod = self.entry_id.get()
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()
        self.servicio.registrar_producto(id_prod, nombre, precio, cantidad)
        self.cargar_productos()

    def consultar_producto(self):
        id_prod = self.entry_id.get()
        producto = self.servicio.consultar_producto(id_prod)
        if producto:
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, producto["nombre"])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, producto["precio"])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, producto["cantidad"])

    def actualizar_producto(self):
        id_prod = self.entry_id.get()
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()
        self.servicio.actualizar_producto(id_prod, nombre, precio, cantidad)
        self.cargar_productos()

    def eliminar_producto(self):
        id_prod = self.entry_id.get()
        self.servicio.eliminar_producto(id_prod)
        self.cargar_productos()

    def cargar_productos(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Cargar productos desde el servicio
        productos = self.servicio.cargar_productos()
        for prod in productos:
            self.tabla.insert("", "end", values=(prod["id"], prod["nombre"], prod["precio"], prod["cantidad"]))

    def mostrar_usuarios(self):
        # Aqui puedes mostrar la lista de usuarios en un popup o en la tabla
        usuarios = self.servicio.usuarios
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for u in usuarios:
            self.tabla.insert("", "end", values=(u.identificacion, u.nombre, u.correo, ""))
    
    def mostrar_productos(self):
        self.cargar_productos()