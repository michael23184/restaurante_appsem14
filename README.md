# Restaurante App - Semana 14

## 📌 Contexto
Este proyecto corresponde a la Semana 14 de la asignatura **Programación Orientada a Objetos**.  
El objetivo es evolucionar la aplicación **restaurante_app** integrando **componentes y contenedores de Tkinter**, manteniendo la arquitectura modular y la persistencia en archivos JSON.

## 🎯 Objetivo de la Semana 14
- Mejorar la interfaz gráfica utilizando **Frames, formularios y tablas**.  
- Separar correctamente las zonas de navegación, formulario y visualización.  
- Implementar operaciones CRUD sobre productos (Registrar, Consultar, Actualizar, Eliminar).  
- Mantener la lógica de negocio en `RestauranteServicio` y no en la interfaz.  
- Conservar la persistencia en `productos.json`.  
- Mostrar resultados claros en la interfaz después de cada operación.  

## 🗂️ Estructura del proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

Código

## ⚙️ Flujo funcional esperado
1. Inicio de la aplicación (`main.py`).  
2. Login con usuario y clave (`login_view.py`).  
3. Validación mediante `RestauranteServicio`.  
4. Acceso a la interfaz principal (`main_view.py`).  
5. Sección **Usuarios** → consulta de información.  
6. Sección **Productos** → formulario + acciones CRUD.  
7. Persistencia en `productos.json`.  
8. Actualización de la interfaz después de cada operación.  

## ✅ Comprobación mínima
- La aplicación inicia sin errores.  
- El login funciona correctamente con usuario y clave.  
- La interfaz principal se muestra después del acceso.  
- La sección de Usuarios permite consultar información.  
- La sección de Productos permite registrar, consultar, actualizar y eliminar.  
- Los cambios se guardan en `productos.json` y se muestran en la interfaz.  

## 📌 Mejoras realizadas en Semana 14
- Se agregó el atributo **clave** al modelo `Usuario` y al archivo `usuarios.json`.  
- Se corrigió la validación de login.  
- Se configuró el tamaño inicial de la ventana.  
- Se implementaron **contenedores (Frames)** en `main_view.py` para separar navegación, formulario y visualización.  
- Se incorporó un **formulario de productos** con campos y botones.  
- Se agregó una **tabla (Treeview)** para mostrar productos.  
- Se implementaron las operaciones CRUD en `RestauranteServicio`.  
- Se actualizó `productos.json` con datos iniciales de prueba.  

## 🚀 Ejecución
1. Clonar el repositorio.  
2. Abrir la carpeta en VS Code.  
3. Ejecutar el archivo `main.py`:  
   ```bash
   python main.py
4. Ingresar con un usuario válido (ejemplo: ID U001, clave 1234).

5. Navegar por las secciones de Usuarios y Productos.