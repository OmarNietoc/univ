
def menu():
    flag=False
  
    while flag==False:
        respuesta =[]
        try:
            respuesta[0]=int(input(f"Indique la entrada deseada: \n 1.Platea\n2.Tribuna.\n3.Cancha\n"))
            if respuesta[0] > 0 and respuesta[0] < 4:
                flag= True
            else:
                print("No valido, intente nuevamente")
                flag=False
        except:
            print("No valido, intente nuevamente")
            flag=False



    return respuesta

def compra(respuesta):
    tipo_Entrada={1:{"Platea":10000},2:{"Tribuna":8200},3:{"Cancha":6000}}
    tipo_usuario={1:"Estudiante",2:"3era edad",3:"General"}
    for i in tipo_Entrada:
        if respuesta == i:
            tipo=list(tipo_Entrada[i].keys())[0]
            #usuario=list(tipo_usuario[i].key()[0])
            print(f"La opcion fue= {i} y el tipo es: {tipo}")
            print("-----")
            break
    



if __name__=="__main__":

    

    compra(menu())
    
    
