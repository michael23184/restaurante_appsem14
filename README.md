# Restaurante App - Semana 15

Este proyecto corresponde al sistema de gestión de restaurante desarrollado en el curso de TIC.  
En esta versión (Semana 15) se implementan las funcionalidades completas de **usuarios, productos y ventas**, con interfaz gráfica en Tkinter y persistencia en archivos JSON.

---

## 🚀 Funcionalidades principales

- **Gestión de usuarios**  
  - Registro y autenticación por correo y clave.  
  - Identificación única de cada usuario.

- **Gestión de productos**  
  - Visualización de lista de productos con ID, nombre, precio y cantidad.  
  - Actualización automática de stock al registrar ventas.

- **Gestión de ventas**  
  - Registro de ventas seleccionando usuario y producto desde combobox.  
  - Generación automática de identificador de venta (`V001`, `V002`, …).  
  - Almacenamiento en `ventas.json`.  
  - Tabla de ventas con ID, usuario, producto y fecha.  
  - Mensajes de confirmación y validación de errores.

---

## 📂 Estructura del proyecto

restaurante_appsem15/
│
├── assets/          # Archivos gráficos (logo, íconos)
├── datos/           # Archivos JSON (usuarios.json, productos.json, ventas.json)
├── modelos/         # Clases Usuario, Producto, Venta
├── servicios/       # Lógica de negocio (RestauranteServicio)
├── ui/              # Interfaces gráficas (login_view.py, main_view.py)
└── main.py          # Punto de entrada de la aplicación

Código

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**  
- **Tkinter** (interfaz gráfica)  
- **JSON** (persistencia de datos)  
- **Git & GitHub** (control de versiones)

---

## ▶️ Ejecución del proyecto

1. Clonar el repositorio:
git clone https://github.com/TU_USUARIO/restaurante_appsem15.git


2. Entrar a la carpeta:
cd restaurante_appsem15


3. Ejecutar la aplicación:
python main.py


📌 Notas finales
Esta versión corresponde a la Semana 15, con el sistema funcionando correctamente.

Se probó el registro de ventas con distintos usuarios y productos, confirmando que se guardan en ventas.json y se muestran en la tabla de la interfaz.

El proyecto está listo para entrega como deber académico.