miVariable = "Hola desde python"
print(miVariable)


x = 10
y = 2 
z = x + y
print(z)

# De esta manera averiguamos la direccion de memoria de una variable
print( id(x) )

# De esta manera preguntamos el tipo de dato al que pertenece la variable
print( type(x) )

# Variable de tipo float
m = 10.3

# Variable de tipo integer
f = 10

# Variables de tipo boolean
si = True
no = False

comparacion = 3 > 2
print(comparacion)

if comparacion:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")
print(si)

# Manejo de cadenas tipo string
miGrupoFavorito = "Los locarios"
print(miGrupoFavorito)

# Concatenación de cadenas
print("Mi grupo favorito es: " + miGrupoFavorito)
print("Mi grupo favorito es:", miGrupoFavorito) # la coma agrega un espacio

# Conversion de tipos 
numero1 = "10"
numero2 = "3"
print("suma:", int(numero1) + int(numero2))

# La funcion int() nos permite convertir un string a entero siempre y cuando este sea un número