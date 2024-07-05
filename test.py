import os
import globales
import random


def asignar_valor_producto():
    todos_productos = globales.leer_archivo_json('valores_productos.json')
    
    productos = []
    for producto in todos_productos:
        valor = random.randint(20,100) * 100
        # input(valor)
        v_iva = valor - (valor * 0.19) 

        nuevo = {
            'nombre': producto['nombre'],
            'valor': valor,
            'iva': v_iva
        }

        productos.append(nuevo)
    
    globales.guardar_archivo_json('valores_productos.json', productos)
    input("Valores asignados")


asignar_valor_producto()