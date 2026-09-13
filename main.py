import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from ui.login_view import LoginView

def main():
    root = tk.Tk()
    root.title("Restaurante App")

    # Crear servicio y restaurante
    servicio = ArchivoServicio()
    restaurante = Restaurante()
    restaurante.cargar_datos(servicio)

    # Pasar servicio y restaurante a la vista de login
    LoginView(root, restaurante, servicio)

    root.mainloop()

if __name__ == "__main__":
    main()