import os
import globales
import valores_productos
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar montos aleatorios.")
            valores_productos.asignar_valor_producto()
        elif opcion == 2:
            print("2. Ver estadísticas.")
            menu_estadisticas()
        elif opcion == 3:
            print("3. Salir del programa.")
            return

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos.")
        print("5. Volver")
        opcion = globales.seleccionar_opcion(5) 

        if opcion == 1:
            print("1. Producto con valor más alto.")
        elif opcion == 2:
            ("2. Producto con valor del IVA más bajo.")
        elif opcion == 3:
            ("3. Promedio del valor de los productos.")
        elif opcion == 4:
            ("4. Media geométrica del valor de los productos.")
        elif opcion == 5:
            print("5. Volver")
            menu_general()

if __name__ == "__main__":
    menu_general()



