

from funciones import *

while True:
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opc = input("Ingrese opción: ")
    

    if opc=='1':
        sueldos_aleatorios()


    elif opc=='2':
       
        Clasificar_sueldos()

    elif opc=='3':
        estadistica()
    elif opc=='4':  
        reporte_sueldos()
    else:
        salir()
        




