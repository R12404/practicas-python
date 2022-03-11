# Calculando la estación del año segun el mes proporcionado 

mesAnio = int(input('Proporciona el mes del año (1-12): '))

estacion = None

if (mesAnio == 1 or mesAnio == 2 or mesAnio == 12):
    estacion = 'Invierno'
elif (mesAnio == 3 or mesAnio == 4 or mesAnio == 5):
    estacion = 'Primavera'
elif (mesAnio == 6 or mesAnio == 7 or mesAnio == 8):
    estacion = 'Verano'
elif (mesAnio == 9 or mesAnio == 10 or mesAnio == 11):
    estacion = 'Otoño'
else: 
    estacion = 'Debe proporcionar un valor entre 1 y 12'


print(f'Para el mes {mesAnio} la estación es {estacion}')

