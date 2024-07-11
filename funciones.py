import random, os, msvcrt, time, csv

trabajadores = ["Juan Pérez","”María García”","”Carlos López”","”Ana Martínez”","”Pedro Rodríguez”","”Laura Hernández”","”Miguel Sánchez”","”Isabel Gómez”","”Francisco Díaz”","”Elena Fernández”"]
sueldos_asignados = []
sueldos_random = []
def sueldos_aleatorios():
    sueldo_trabajadores = 0
    sueldo_trabajadores = random.randint(300000,2500000)
    nombre_trabajadores = random.choice(trabajadores)

    print(nombre_trabajadores)
    print(sueldo_trabajadores)
    sueldo = [nombre_trabajadores, sueldo_trabajadores]
    sueldos_asignados.append(sueldo)
    sueldos_random.append(sueldo_trabajadores)
    print("Sueldo asignado!")

    
    os.system('cls')

def Clasificar_sueldos():
    print("SUELDOS")    
    for s in sueldos_asignados:
             print("----------------------------")
             print("Nombre:",s[0])
             print("Sueldo:",s[1])   
             print("----------------------------")

    print("...Presione alguna tecla para continuar...")
    msvcrt.getch()


    
def estadistica():
   
    for sueldo_alto in sueldos_asignados:
        if sueldo_alto==sueldos_asignados[1]:
            print("Sueldo más alto:", sueldo_alto)
            break
        
    for sueldo_bajo in sueldos_random:
        if sueldo_bajo==sueldos_asignados[1]:
            sueldos_asignados.sort==sueldo_bajo
            print("Sueldo bajo:", sueldo_bajo)
            break

       
    for promedio_sueldos in sueldos_random:
        promedio_sueldos == sueldos_random
        acu = promedio_sueldos+promedio_sueldos
        acu=acu/10
        acu = acu+acu
        print("Promedio:",acu)
        acu/10
        break
   
    for media_geometrica in sueldos_asignados:
        if media_geometrica == sueldos_asignados[1]:
            acum= sueldos_asignados[1^1/10]
            acum= acum*acum
            print("media geométrica:",media_geometrica)


def reporte_sueldos():
    print("Nombre del empleado")
    print(sueldos_asignados[2])
    print("Sueldo base")
    print(sueldos_asignados[1])
    print("Descuento salud")

    for desc_salud in sueldos_random:
        desc_salud == sueldos_random
        acumu = desc_salud+desc_salud
        acumu=acumu+7/100
        acumu = acumu+acumu
        print("descuento de salud: ",acumu)
        break
        

   
    for desc_afp in sueldos_random:
        desc_afp == sueldos_random
        acumul = desc_afp+desc_afp
        acumul=acumul+7/100
        acumul = acumul+acumul
        print("descuento de salud: ",acumul)
        break

  
    for sueldo_liquido in sueldos_asignados:
        print("Sueldo liquido")
        sueldo_liquido = sueldos_asignados
        sueldo_liquido == sueldos_random
        acumu = sueldo_liquido + sueldo_liquido
        acumu = sueldos_random[1-1]+12/100
        acumu=acumu+acumu
 
        print(acumu)
        
    print("1. Crear archivo csv.\2. Salir")
    
    opc2 = input("Escriba nombre del archivo: ")
    
    if opc2=='1':
        with open ("archivo", "x", ".csv",newline=" ") as File:
            escritor=csv.writer(File)
            File=escritor.writerow(File)
        
    else:
        print("Adios!")
        salir()


    
        




def salir():
    os.system('cls')
    print("FINALIZANDO PROGRAMA...\nDesarrollado por: Giovanni Orellana\nrut: 21874476-1\nADIOS!")
    time.sleep(3)
    exit()