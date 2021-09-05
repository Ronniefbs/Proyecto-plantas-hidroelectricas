import funciones as fun


if __name__ == "__main__":
    print("--------------  PROYECTO  -------------------")
    while(True):
        print("\n\nElija una de estas 3 opciones\n 1) Calcular Total de Consumo \n 2) Buscar Plantas por ciudad \n 3) Calcular Tarifa por Region \n 4) Calcular Consumo del mes \n 5) Salir")
        opcion = input("Escribe un numero-> ")
        if opcion == "1":
           planta = input("Escriba una planta: ")
           ciudad = input("Escriba una ciudad: ").capitalize()      
           fun.totalConsumos(planta,ciudad)
        elif opcion =="2":
           ciudad = input("Escriba una ciudad: ").capitalize()
           print(f" Diccionario -> {fun.buscarPlantasPorCiudad(ciudad)} ")

        elif opcion =="3":
           region = input("Escriba una region: ").lower()
           print(f"---- Total de la region {region} : ${fun.calcularTarifaPorRegion(region)} ----")
        elif opcion =="4":
            mes = input("Escriba un numero del mes: ")
            if mes.isdigit():
               fun.totalMes(int(mes))
            else:
               print("Escriba un numero válido")   
        elif opcion =="5":
            break
        else: 
            print("Escoja entre las opciones disponibles\n")

    print("--------------  FIN  -------------------")
