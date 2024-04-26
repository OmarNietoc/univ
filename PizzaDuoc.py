from os import system
from time import sleep

opciones={
    1:{"Tradicional":12000},
    2:{"Peperoni":14000},
    3:{"All Carnes": 17000}
}

descuentos= {
    1:{"Estudiante Diurna":0.12},
    2:{"Estudiante Vespertino":0.12},
    3:{"Administrativo":0}
}


def menu_Rapid():
    system('cls')
    print("== RAPID MENU ==")
    print("")
    print("Elige una opción:")
    print("")
    for num, pizzas in opciones.items():
        for pizza,precio in pizzas.items():
            print(f"{num}. {pizza} ${precio}")
    print(f"{num+1}. Salir")
    return (num+1)
        
def main():
    carrito={}
    flag='S'
    while flag == 'S':
        opc_pizza=0
        salir=menu_Rapid()
        try:
            opc_pizza=int(input("> "))
        except:
            system('cls')
            print("No valido, intente nuevamente")
            sleep(1)
            system('cls')
            continue
        
        if opc_pizza > salir or opc_pizza < 1:
            system('cls')
            print("No valido, intente nuevamente")
            sleep(1)
            system('cls')
            continue
        elif opc_pizza == salir:
            flag='N'
        
        else:
            seleccionado=(list(opciones[opc_pizza].keys())[0],list(opciones[opc_pizza].values())[0])
            if  seleccionado in carrito:
                carrito[seleccionado]+=1
            else:
                carrito[seleccionado]=1
            system('cls')
            print("Se a añadido a tu carrito de compras!")
            sleep(1)
            system('cls')
            flag_carr=True
            while flag_carr == True:
            
                rapid_Carrito(carrito)
                print("Elige una opción:")
                print("1.Seguir comprando")
                print("2.Pagar")
                print("3.Anular compra.")
                opc_compra=input("> ")
                if opc_compra == '3':
                    carrito={}
                    system('cls')
                    print("Tu compra ha sido anulada exitosamente.")
                    sleep(1)
                    system('cls')
                    flag_carr=False
                elif opc_compra == "2":
                    flag_carr=False
                    flag='N'

                elif opc_compra == '1':
                    break
                else:
                    system('cls')
                    print("No valido, intente nuevamente")
                    sleep(1)
                    system('cls')
                    continue
    if opc_pizza != 4:

        rapid_pago(carrito)




def rapid_pago(carrito):
    subtotal=0
    while True:
        system('cls')
        print("Seleccione una opcion para aplicar descuentos a su compra:")
        print("1.Estudiante de Diurno")
        print("2.Estudiante de Vespertino")
        print("3.Administrativo")
        try:
            opc_descuento= int(input("> "))
        except:
            system('cls')
            print("No valido, intente nuevamente")
            sleep(1)
            system('cls')
            continue

        if opc_descuento >= 1 and opc_descuento <=3:
            system('cls')
            print("PizzasDuoc")
            print("-----------------------------------------------------")
            for pizza,cont in carrito.items():
                print(f"{cont} {"Pizzas"if cont > 1 else "Pizza"} {pizza[0]} ${pizza[1]}")
                subtotal+=pizza[1]
            print("-----------------------------------------------------")
            print(f"Subtotal\t {subtotal}")
            descuento=int(list(descuentos[opc_descuento].values())[0] * subtotal)
            print(f"Descuento {int(list(descuentos[opc_descuento].values())[0]*100)}%\t {descuento}")
            print(f"Total a pagar: {subtotal - descuento}")
            break
        else:
            system('cls')
            print("No valido, intente nuevamente")
            sleep(1)
            system('cls')
            continue

def rapid_Carrito(carrito):
    system('cls')
    print("== RAPID CARRITO==")
    for pizza,cont in carrito.items():
        print(f"{cont} {"Pizzas"if cont > 1 else "Pizza"} {pizza[0]}", end="\t|\n")
    print("========================|")
    print("")

if __name__=="__main__":
    main()