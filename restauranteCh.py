from time import sleep
from os import system

platos={
    "Camaron Mandarin":11000,
    "Carne Mongoliana":10000,
    "Chapsui Pollo":9500,
    "Chapsui Carne":12000,
    "Parrillada China":15000
        }
descuentos={
    "Cliente Frecuente":0.15,
    "Tarjeta Vecino":0.1,
    "Carnet tercera edad":0.07,
    "No posee descuento":0
}

def menu():
    i=1
    system('cls')
    print("=== SHIN WE WHENSHA ===")
    for plato,precio in platos.items():
        print(f"{i}.{plato}.\t${precio}")
        i+=1
    print(f"{i}.Anular compra.")
    return (i)

def main():
    compra={}
    menuP=True
    while menuP == True:
        salir=menu()
        respuesta=0
        try:
            respuesta=int(input("> "))
        except:
            system('cls')
            print("No valido, intente nuevamente.")
            sleep(1)
            system('cls')
            continue
        
        if respuesta < 1 or respuesta > salir:
            system('cls')
            print("No valido, intente nuevamente.")
            sleep(1)
            system('cls')
            continue
        elif respuesta == salir:
            menuP=anularPedido()
            
            
        else:
            cantidad=0
            sec=True
            while sec:
                print(f"Cuantos platos de {list(platos.keys())[respuesta-1]} desea?")
                try:
                    cantidad=int(input("> "))
                except:
                    system('cls')
                    print("No valido, intente nuevamente.")
                    sleep(1)
                    system('cls')
                    continue
                eleccion=(list(platos.keys())[respuesta-1],list(platos.values())[respuesta-1])
                if eleccion in compra:
                    compra[eleccion]+=cantidad
                else:
                    compra[eleccion]=cantidad
                while True:
                    system('cls')
                    carrito(compra)
                    print("")
                    print("Seleccione una opcion:")
                    print("1.Continuar comprando.")
                    print("2.Pagar.")
                    print("3.Limpiar Carrito de compras.")
                    respsec=input("> ")
                    if respsec == '1':
                        sec=False
                        break
                    elif respsec == '2':
                        sec=False
                        menuP=False
                        break
                    elif respsec == '3':
                        compra={}
                        system('cls')
                        print("Carrito de compras limpio.")
                        sleep(1)
                        sec=False
                        break
                    else:
                        system('cls')
                        print("No valido, intente nuevamente.")
                        sleep(1)
                        system('cls')
                        continue
    if respuesta != salir:
        pagar(compra)
    else:
        print("Se fue sin comprar")

def pagar(compra):
    cantidadTotal=0
    subTotal=0
    sub=0
    i=0
    for obj,cant in compra.items():
        cantidadTotal+=cant
        sub=cant*obj[1]
        subTotal+=sub
    while True:
        system('cls')
        print("Seleccione la opcion correspondiente:")
        for tipo,desc in descuentos.items():
            i+=1
            print(f"{i}.{tipo}.\t%{int(desc*100)}")
        try:
            posDescuento=int(input("> "))
        except:
            system('cls')
            print("No valido, intente nuevamente.")
            sleep(1)
            system('cls')
            i=0
            continue
        if posDescuento > 0 and posDescuento < (i+1):
            break
        else:
            system('cls')
            print("No valido, intente nuevamente.")
            sleep(1)
            system('cls')
            i=0
            continue
            
    carrito(compra)
    print(f"TOTAL PRODUCTOS: {cantidadTotal}")
    print("==============================")
    print(f"SUBTOTAL:.\t${subTotal}")
    print("DESCUENTO:")
    descuento=int(list(descuentos.values())[posDescuento-1]*subTotal)
    print(f"{int(list(descuentos.values())[posDescuento-1]*100)}% {list(descuentos.keys())[posDescuento-1]}.\t${descuento}")
    print("==============================")
    print(f"TOTAL:.\t${subTotal-descuento}")    
    print("==============================")
    print(" GRACIAS POR SU COMPRA! :D")


def carrito(compra):

    system('cls')
    print("=== SHIN WE WHENSHA ===")
    for obj , cant in compra.items():
        print(f"{cant} {obj[0]}.\t${obj[1]}")
    print("==============================")
        
    
    

def anularPedido():
    r=''
    while True:
        system('cls')
        print("=== SHIN WE WHENSHA ===")
        print("¿En realidad desea anular su pedido?")
        print("1.Si.")
        print("2.No.")
        r=input("> ")
        if r == '1':
            return False
        elif r == '2':
            return True
        else:
            system('cls')
            print("No valido, intente nuevamente.")
            sleep(1)
            system('cls')
            continue

if __name__ == '__main__':
    main()