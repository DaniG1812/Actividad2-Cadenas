#Punto1
name = "Daniel Cuaran"
age = 20
favouriteFood = "Atun y Arroz"
text = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(text)
#Punto2
FullName = input("Ingrese su nombre completo: ")
lengthUsuario = len(FullName.strip())
print(f"Hola, {FullName}! Tu nombre tiene {lengthUsuario} letras, excluyendo los espacios")
#Punto3
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print(
f"Las ventas de la empresa lactea aumentaron un {round(increaseSalesPercent,2)}% y los ingresos crecieron un {round(revenueGrowthPercent,2)}%")

#Punto4
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"

modifiedMessage = secretMessage[3:]
decodedMessage = modifiedMessage[::2]

print(decodedMessage)

#Punto5
text = "El nombre Python viene dado por la afición de Van Rossum al grupo Monty Python"
palabras = text.split()
num_palabras = len(palabras)
print(f"Numero de palabras en la frase: {num_palabras}")

#Punto6
word = "Camila"
nueva = word.replace('a','e')
print(nueva)
#Punto7
sentence = "La historia del lenguaje de programación Python"

palabras = sentence.split()

inversa = palabras[::-1]

frase_invertida = " ".join(inversa)

print(frase_invertida)


