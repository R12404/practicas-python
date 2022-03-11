# Preguntando si dos valores son iguales
a = 4
b = 5

resultado = (a == b)
print(f'Resultado == : {resultado}')

# Preguntando si dos valores son distintos

resultado = (a != b)
print(f'resultado de != : {resultado}')

# Operador de mayor que
resultado = (a > b)
print(f'resultado de > : {resultado}')

# Determinando si un número es par
entrada = int(input('Proporciona un número: '))

if (entrada % 2 == 0):
    print('El número es par')
else:
    print('El número es impar')

# Determinando si es mayor de edad

edad = int(input('Proporciona tu edad: '))

if (edad >= 18):
    print(f'Eres mayor de edad')
else:
    print(f'Eres menor de edad')

