from os import system
from time import sleep

pantalones={1:{"Pantalones Largos":9},2:{"Pantalones Cortos":7},3:{"Blue Jeans":6}}
camisas={1:{"Camisa sin mangas":8},2:{"Camisa Manga larga":5},3:{"Franelilla":3},4:{"Sueter":12}}
zapatos={1:{"Deportivos":8},2:{"De gala":15}}
compra={}

def menu():
    prim='S'
    while prim=='S':
        resp=0
        print("==MENU PRINCIPAL==")
        print("1.Pantalones")
        print("2.Camisas")
        print("3.Zapatos")
        print("4.Salir")

        try:
            resp= int(input())
        except ValueError or KeyError:
            system('cls')
            print("No valido, elija una opcion")
            sleep(1)
            system('cls')
            continue

        if resp < 1 or resp > 4:
            system('cls')
            print("Numero no valido, elija una opcion")
            sleep(1)
            system('cls')
            continue

        elif resp == 1:
            prim=menuSec(pantalones)
        elif resp == 2:
            prim=menuSec(camisas)
        elif resp == 3:
            prim=menuSec(zapatos)
        elif resp == 4:
            prim=False

        
    mostrarBoleta()      

def menuSec(seleccion):
    respSec=0
    multi=1
    sec=True
    prim='S'
    
    while sec==True:
        print("== MENU ==")
        for fila,item in seleccion.items():
            for j,precio in item.items():
                print(f"{fila}.{j} ${precio}.")
        salir=fila+1
        print(f"{salir}.Volver a menu principal")
        
        try:
            respSec=int(input())
        except ValueError:
            system('cls')
            print("No valido, elija una opcion")
            sleep(1)
            system('cls')
            continue

        if respSec < 1 or respSec > salir:
            system('cls')
            print("No valido, elija una opcion")
            sleep(1)
            system('cls')
            continue

        elif respSec == salir:
            sec=False
            return prim
        else:
            try:
                multi=int(input("Indique cuantos desea > "))
            except:
                system('cls')
                print("No valido, elija una opcion")
                sleep(1)
                system('cls')
                continue
            if multi <1:
                system('cls')
                print("No valido, elija una opcion")
                sleep(1)
                system('cls')
            else:
                seleccionado = (list(seleccion[respSec].keys())[0], list(seleccion[respSec].values())[0])
                if seleccionado in compra:
                    compra[seleccionado]+= multi
                else:
                    compra[seleccionado]=multi

                print(f"Se eligió: {compra}")
                prim=input("Desea seguir comprando? S/N\n> ").upper()
                sec=False
                return prim
                
def mostrarBoleta():
    i=1
    total=0
    print("\t\t\t== BOLETA ==")
    for seleccion,cantidad in compra.items():
        precioU=seleccion[1]
        precio=int(precioU*cantidad)
        print(f"-{i}. {seleccion[0]} ${precioU}         \tX \t{cantidad} \t-> \t${precio}")
        total=precio+total
        i+=1
    print(f"Total a pagar: ${total}")
if __name__=="__main__":
    menu()
