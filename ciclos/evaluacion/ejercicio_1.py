lista_placas = []
lista_marcas = []
lista_anios = []

opcion = "0"

while True:
    print("------------- MENU --------------")
    print("1. Registrar vehículo")
    print("2. Mostrar vehículos")
    print("3. Buscar vehículo")
    print("4. Mostrar vehículo más antiguo")
    print("5. Mostrar año promedio de fabricación")
    print("6. Salir")
    print("---------------------------------")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        placa = input("Ingrese placa: ")
        marca = input("Ingrese marca: ")
        anio = int(input("Ingrese año fabricación: "))
        
     
        lista_placas.append(placa)
        lista_marcas.append(marca)
        lista_anios.append(anio)
        print("Vehículo registrado con éxito.")
           
    elif opcion == "2":
       
        if len(lista_placas) == 0:
            print("No existen vehículos registrados.")
        else:
            print("--- LISTA DE VEHÍCULOS ---")
          
            for i in range(len(lista_placas)):
                print("Placa:", lista_placas[i], "| Marca:", lista_marcas[i], "| Año:", lista_anios[i])
                
  
    elif opcion == "3":
        if len(lista_placas) == 0:
            print("No existen vehículos registrados.")
        else:
            placa_buscar = input("Ingrese la placa del vehículo a buscar: ")
            
           
            if placa_buscar in lista_placas:
               
                posicion = lista_placas.index(placa_buscar)
                print("--- VEHÍCULO ENCONTRADO ---")
                print("Placa:", lista_placas[posicion])
                print("Marca:", lista_marcas[posicion])
                print("Año:", lista_anios[posicion])
            else:
                print("El vehículo no fue encontrado.")

    elif opcion == "4":
     if len(lista_placas) == 0:
            print("No existen vehículos registrados.")
    else:
            menor_anio = min(lista_anios)
            posicion_antiguo = lista_anios.index(menor_anio)
            
            print("--- VEHÍCULO MÁS ANTIGUO ---")
            print("Placa:", lista_placas[posicion_antiguo])
            print("Marca:", lista_marcas[posicion_antiguo])
            print("Año:", lista_anios[posicion_antiguo])
