consumo_energia = {
 'Coca Codo Sinclair': {
 'Quito': {'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213), 'tarifa': 65},
 'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
 },
 'Sopladora': {
 'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
 'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
 'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}
'''
Empieza el desmadre!
'''
def totalMes(mes):
    acumulaValor=0
    acumulaConsumo=0
    total =0
    if mes<=12:
        for planta in consumo_energia:
            for ciudadDic in consumo_energia.get(planta):
                consumo = consumo_energia.get(planta).get(ciudadDic).get('consumos')[mes-1]
                tarifa = consumo_energia.get(planta).get(ciudadDic).get('tarifa')
                acumulaValor+=consumo*tarifa
                total+=consumo*tarifa 
                acumulaConsumo+=consumo
            print(f"Planta: {planta} : Consumo de Mes -> {acumulaConsumo} Valor-> {acumulaValor}")
            acumulaValor,acumulaConsumo =0, 0
        print(f"Total del mes #{mes}: {total}")

    else:
        print("Elija correctamente un numero de mes")

def totalConsumos(planta,ciudad):
    acumula = 0
    if planta in consumo_energia.keys() and ciudad in consumo_energia.get(planta).keys()  :
        consumos = consumo_energia.get(planta).get(ciudad).get('consumos')
        for consu in consumos:
            acumula += consu
        print(f"--- Total de consumo de {planta} en la ciudad {ciudad} : {acumula}MWh ---")
    else:
        return  print("\nNo existen los datos ingresados")
    return acumula

def buscarPlantasPorCiudad(ciudad):
    diccionario={}
    for planta in consumo_energia: 
        for ciudadDic in consumo_energia.get(planta):
            if ciudadDic==ciudad:
                diccionario[planta]=totalConsumos(planta,ciudad)
    if not diccionario:
        print("----Esta vacio----")
    return diccionario

def calcularTarifaPorRegion(region):
    acumula = 0
    if region in informacion:
        listaCiudades = informacion.get(region)
        for ciudad in listaCiudades:
            for planta in consumo_energia:
                for ciudadDic in consumo_energia.get(planta):
                    if ciudadDic==ciudad:
                        consumoplanta = consumo_energia.get(planta).get(ciudad).get('consumos')
                        tarifa = consumo_energia.get(planta).get(ciudad).get('tarifa')
                        total = sum(consumoplanta)*tarifa
                        acumula += total
    else:
        print("\nNo se encuentra esa Region")
    return acumula

