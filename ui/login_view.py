import tkinter as tk
from tkinter import messagebox
from servicios.auth_service import AuthService
from ui.main_view import MainView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Login")
        self.auth_service = AuthService()

        # Etiquetas y campos
        tk.Label(root, text="Correo:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_correo = tk.Entry(root)
        self.entry_correo.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Clave:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_clave = tk.Entry(root, show="*")
        self.entry_clave.grid(row=1, column=1, padx=10, pady=10)

        # Botón ingresar
        tk.Button(root, text="Ingresar", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        correo = self.entry_correo.get()
        clave = self.entry_clave.get()
        valido, usuario = self.auth_service.validar_acceso(correo, clave)

        if valido:
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario.nombre}")
            self.root.destroy()  # Cierra la ventana de login

            # Abre la ventana principal
            main_root = tk.Tk()
            MainView(main_root, usuario)
            main_root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")

# Punto de entrada para pruebas rápidas
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()