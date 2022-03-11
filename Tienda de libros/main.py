nombreLibro = input('Proporciona el nombre del libro: ')
idLibro = int(input('Proporciona el id del libro: '))
precioLibro = float(input('Precio del libro: '))
envioGratuito = input('¿Envío gratuito? (si/no): ')

print(f'''Nombre: {nombreLibro}
Id:  {idLibro}
Precio: {precioLibro} 
¿Envio gratuito?: {envioGratuito}''')