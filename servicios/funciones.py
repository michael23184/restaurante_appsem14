import json
import os
from modelos.venta import Venta

# Guardar ventas en JSON
def guardar_venta(venta, archivo="datos/ventas.json"):
    ventas = []
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            ventas = json.load(f)

    ventas.append(venta.to_dict())

    with open(archivo, "w") as f:
        json.dump(ventas, f, indent=4)
def vender_producto(usuario, producto, cantidad):
    if producto.stock >= cantidad:
        producto.stock -= cantidad
        venta = Venta(usuario, producto, cantidad)
        guardar_venta(venta)
        print(f"✅ Venta realizada: {cantidad} {producto.nombre} a {usuario.nombre}")
    else:
        print("❌ No hay suficiente stock para realizar la venta.")
def consultar_ventas_por_usuario(nombre_usuario, archivo="datos/ventas.json"):
    if not os.path.exists(archivo):
        print("No hay ventas registradas.")
        return

    with open(archivo, "r") as f:
        ventas = json.load(f)

    ventas_usuario = [v for v in ventas if v["usuario"] == nombre_usuario]

    if ventas_usuario:
        print(f"📊 Ventas de {nombre_usuario}:")
        for v in ventas_usuario:
            print(v)
    else:
        print(f"No se encontraron ventas para el usuario {nombre_usuario}.")
