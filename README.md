# Restaurante App - Semana 13

Proyecto académico de la carrera TIC.  
Aplicación en **Python** que gestiona productos, usuarios y ventas de un restaurante, ahora con **interfaz gráfica (Tkinter)**.

---

## 📂 Estructura del proyecto

restaurante_appsem13/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── init.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

Código

---

## ⚙️ Requisitos

- Python 3.10 o superior  
- Librería estándar `tkinter` (incluida en Python)  

---

## ▶️ Ejecución

1. Clonar el repositorio o descargar la carpeta del proyecto.  
2. Asegurarse de que los archivos JSON estén en la carpeta `datos/`.  
3. Ejecutar el archivo principal:

```bash
python main.py
🖥️ Funcionamiento
LoginView: Pantalla inicial de acceso.

MainView: Muestra usuarios y productos registrados.

Servicios: Manejan lectura/escritura de datos en JSON.

Modelos: Definen las clases Producto, Usuario y Venta.

📌 Notas
Los datos se guardan en formato JSON dentro de la carpeta datos/.

El sistema permite registrar productos, usuarios y ventas.

La interfaz gráfica reemplaza el menú por consola de semanas anteriores.

👨‍💻 Autor
Michael Heras  
Segundo semestre - Carrera TIC