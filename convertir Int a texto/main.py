numero = int(input('proporciona un valor entre 1 y 3: '))
numeroTexto = ''

if (numero == 1):
    numeroTexto = 'uno'
elif (numero == 2):
    numeroTexto = 'dos'
elif (numero == 3):
    numeroTexto = 'tres'
else: 
    numeroTexto = 'Fuera de rango'

print(f'Número proporcioando: {numeroTexto}')