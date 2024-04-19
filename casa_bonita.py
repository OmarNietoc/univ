from os import system, path
from time import sleep
import json

pisos=10
edificio=[['A','B','C']]
for i in range(pisos):
    edificio.append(['_','_','_'])

archivo_ocupados="ocupados.json"
if path.exists(archivo_ocupados):
    with open(archivo_ocupados , "r") as f:
        ocupados=json.load(f)
    for pisos_torre in ocupados:
        piso_ocupado , torre_ocupada= pisos_torre
        edificio[piso_ocupado][edificio[0].index(torre_ocupada)]='X'
    
else:
    ocupados=[]

def menu():
    while True:
        try:
            print("=== CASA FELIZ ===")
            print("1.Ver deptos disponibles")
            print("2.Ver listado de precios.")
            print("3.Salir")
            resp=int(input())
            if resp < 1 or resp > 3:
                system('cls')
                print("Opcion no valida, intente nuevamente.")
                sleep(1)
                system('cls')
            elif resp == 1:
                elegir_depto()
            else:
                break
        except:
            system('cls')
            print("Opcion no valida, intente nuevamente.")
            sleep(1)
            system('cls')

def mostrar_edificio():
    cont=pisos + 1

    for i in edificio:
        if cont < (pisos+1):
            print(cont, end= " \t")
        else:
            print("",end=" \t")
        for j in i:
            
            print(j, end=" \t")
            
        cont-=1
        print("")

def elegir_depto():
    r=1
    while r==1:
        mostrar_edificio()
        piso_e = int(input("Indique el piso a elegir > "))-1
        piso_e= pisos-piso_e
        while piso_e > pisos or piso_e < 1:
            system('cls')
            print("Opcion no valida, intente nuevamente.")
            sleep(1)
            system('cls')
            mostrar_edificio()
            piso_e = pisos - int(input("Indique el piso a elegir > "))-1
        
        torre=input("Ingrese la torre deseada A / B / C > ").upper()
        while torre not in edificio[0]:
            system('cls')
            print("Opcion no valida, intente nuevamente.")
            sleep(1)
            system('cls')
            mostrar_edificio()
            torre=input("Ingrese la torre deseada A / B / C > ").upper()
            
        if [piso_e,torre] in ocupados:
            system('cls')
            print("DEPTO OCUPADO, INTENTE NUEVAMENTE.")
            sleep(1)
            system('cls')
            mostrar_edificio()
        
        else:
                columna_e=edificio[0].index(torre)
                edificio[piso_e][columna_e]='X'
                ocupados.append([piso_e,torre])
                with open(archivo_ocupados, "w") as f:
                    json.dump(ocupados, f)

                mostrar_edificio()
                r=int(input("Desea apartar otro depto?\n1.Si\n2.No\n> "))

                while r < 1 or r > 2:
                    system('cls')
                    print("NO VALIDO, INTENTE NUEVAMENTE.")
                    sleep(1)
                    system('cls')
                    r = int(input("Desea apartar otro depto?\n1.Si\n2.No\n> "))          

if __name__=='__main__':
    menu()