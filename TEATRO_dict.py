import os
import time
opciones= { "1":{"tipo":"Platea General","precio":10000},
            "2":{"tipo":"Tribuna General","precio":8200},
            "3":{"tipo":"Cancha General","precio":7000},
            "4":{"tipo":"Platea Vecino","precio":8000},
            "5":{"tipo":"Tribuna Vecino","precio":6200},
            "6":{"tipo":"Cancha Vecino","precio":5000},
             }
tipo_descuento = {
    "1":{"tipo":"Estudiante","descuento":0.1},
    "2":{"tipo":"Adulto mayor","descuento":0.3},
    "3":{"tipo":"Publico General","descuento":0}
    }

def menu():
    respuesta=["",""]
    while True:
        print("---------- TEATRO MORO ----------")

        for key,value in opciones.items():
            print(f"{key}. {value["tipo"]} ${value['precio']}")

    
        respuesta[0]=input(f"Seleccione el area deseada.\n")
        if respuesta[0] not in opciones:
            os.system('cls')
            print("Respuesta no valdia, intente nuevamente")
            time.sleep(3)
            os.system('cls')
        else:
            time.sleep(0.5)
            os.system('cls')
            break
    while True:
        print("---------- TEATRO MORO ----------")
        print(f"\nIndique su tipo de cliente:")
        for key,value in tipo_descuento.items():
            print(f"{key}. {value["tipo"]}")
        respuesta[1]=input(f"Por favor elija una opcion\n")
        if respuesta[1] not in tipo_descuento:
            os.system('cls')
            print("Respuesta no valdia, intente nuevamente")
            time.sleep(3)
            os.system('cls')
        else:
            break
    return respuesta


def compra(respuesta):
    descuento=int(opciones[respuesta[0]]["precio"]*tipo_descuento[respuesta[1]]["descuento"])
    time.sleep(0.5)
    os.system('cls')
    print("--- Boleta ---")
    print(f"Area: {opciones[respuesta[0]]["tipo"]} \nTipo de cliente: {tipo_descuento[respuesta[1]]["tipo"]}\nSub Total: {opciones[respuesta[0]]["precio"]} \nDescuento: {descuento}\nTotal a pagar: {int(opciones[respuesta[0]]["precio"] - descuento)}")
    print("Gracias por su compra!")
    
    

if __name__=="__main__":
    compra(menu())
    
    
