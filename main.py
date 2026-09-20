import tkinter as tk
from ui.login_view import LoginView

def main():
    root = tk.Tk()
    root.title("Restaurante App")
    root.geometry("400x300")  # tamano inicial recomendado
    app = LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()