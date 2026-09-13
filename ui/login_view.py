import tkinter as tk
from ui.main_view import MainView

class LoginView:
    def __init__(self, root, restaurante, servicio):
        self.root = root
        self.restaurante = restaurante
        self.servicio = servicio

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Iniciar sesión", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.frame, text="Usuario (ID):").pack()
        self.usuario_entry = tk.Entry(self.frame)
        self.usuario_entry.pack()

        tk.Label(self.frame, text="Clave:").pack()
        self.clave_entry = tk.Entry(self.frame, show="*")
        self.clave_entry.pack()

        tk.Button(self.frame, text="Ingresar", command=self.login).pack(pady=10)

        self.error_label = tk.Label(self.frame, text="", fg="red")
        self.error_label.pack()

    def login(self):
        usuario = self.usuario_entry.get().strip()
        clave = self.clave_entry.get().strip()

        if self.restaurante.validar_acceso(usuario, clave):
            self.frame.destroy()
            MainView(self.root, self.restaurante, self.servicio)
        else:
            self.error_label.config(text="Usuario o clave incorrectos")