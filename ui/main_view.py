import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title("Restaurante App - Principal")
        self.usuario = usuario

        # Frame principal
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Bienvenida
        tk.Label(frame, text=f"Bienvenido {self.usuario.nombre}", 
                 font=("Arial", 14, "bold")).pack(pady=10)

        # Botones de funcionalidades
        tk.Button(frame, text="Gestión de Productos", 
                  command=self.gestion_productos).pack(fill="x", pady=5)

        tk.Button(frame, text="Gestión de Ventas", 
                  command=self.gestion_ventas).pack(fill="x", pady=5)

        tk.Button(frame, text="Gestión de Usuarios", 
                  command=self.gestion_usuarios).pack(fill="x", pady=5)

        tk.Button(frame, text="Salir", 
                  command=self.root.quit).pack(fill="x", pady=5)

    # Métodos de ejemplo para cada funcionalidad
    def gestion_productos(self):
        messagebox.showinfo("Productos", "Aquí se gestionan los productos.")

    def gestion_ventas(self):
        messagebox.showinfo("Ventas", "Aquí se registran y consultan las ventas.")

    def gestion_usuarios(self):
        messagebox.showinfo("Usuarios", "Aquí se administran los usuarios.")