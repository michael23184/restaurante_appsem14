import tkinter as tk
from tkinter import messagebox
from servicios.restaurante import RestauranteServicio
from ui.main_view import MainView

class LoginView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.servicio = RestauranteServicio()
        self.pack(fill="both", expand=True)
        self.crear_componentes()

    def crear_componentes(self):
        # Etiquetas y entradas
        tk.Label(self, text="Usuario (ID):").grid(row=0, column=0, pady=5, sticky="w")
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.grid(row=0, column=1, pady=5)

        tk.Label(self, text="Clave:").grid(row=1, column=0, pady=5, sticky="w")
        self.entry_clave = tk.Entry(self, show="*")
        self.entry_clave.grid(row=1, column=1, pady=5)

        # Boton de ingreso
        btn_ingresar = tk.Button(self, text="Ingresar", command=self.validar_login)
        btn_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

    def validar_login(self):
        identificacion = self.entry_usuario.get()
        clave = self.entry_clave.get()

        if self.servicio.validar_acceso(identificacion, clave):
            # Si el login es correcto, abrir MainView
            self.destroy()
            MainView(self.master)
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")