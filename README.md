# Restaurante App

Aplicación de gestión para restaurante desarrollada en **Python**, organizada con arquitectura modular (Modelos, Servicios, UI y Datos).  
Este sistema permite iniciar sesión con **correo + clave** y acceder a una ventana principal con opciones de gestión.

---

## Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/michael23184/restaurante_appsem14.git
Entrar en la carpeta del proyecto:

bash
cd restaurante_appsem14
Ejecutar el sistema:

bash
python main.py
 Credenciales de prueba
Correo: michael@correo.com

Clave: 1234

 Estructura del proyecto
modelos/ → clases principales (usuario.py, producto.py, venta.py)

servicios/ → lógica de negocio (auth_service.py, restaurante.py, etc.)

ui/ → interfaces gráficas (login_view.py, main_view.py)

datos/ → archivos JSON (usuarios.json, productos.json, ventas.json)

Funcionalidades
Login con correo + clave.

Ventana principal con opciones:

Gestión de productos

Gestión de ventas

Gestión de usuarios

Arquitectura clara y modular, lista para ampliarse.

📌 Tecnologías utilizadas
Python 3.x

Tkinter (interfaz gráfica)

JSON (persistencia de datos)

Git/GitHub (control de versiones y repositorio)

📖 Notas
Este proyecto está diseñado como práctica académica para aplicar conceptos de:

Programación orientada a objetos (POO).

Manejo de archivos JSON.

Separación de capas: modelo, servicio, interfaz.

Código