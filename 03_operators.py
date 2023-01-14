### Operadores ###

'''
Aritmeticos: + , - , * , / , % , ** , //
Comapracion: == , != , > , < , >= , <= 
Asignacion: = , += , -=, *= , /= , %= , **=
Logicos: "and", "or", "not"
Miembros: "in", "not in"
Identidad: "is", "is not"
Manejo de bits: "&", "|", "^", "~", "<<", ">>"
'''

### Ejemplos operadores aritmeticos ###
print(3 + 4) #suma
print(3 - 4) #resta
print(3 * 4) #multiplicacion
print(3 / 4) #division
print(3 // 4) #division entera
print(3 % 4) #resto de la division
print(3 ** 4) #elevado
# Estos operadores tambien se pueden mezclar
print(3 + 4 * 5 / 4 ** 9 //5)
 
# Algunos operadores tambien funcionan con strings
print("Hola" + " " + "Mundo" + "," + " " + "Que tal?")
print("Hola " + str(5))
print("hola " * 5)
print("hola " * (2 ** 3)) 
print("hola" * int(3 + 4 * 5 / 4 ** 9 //5)) #Si el resultado es tipo float hay que forzarlo a tipo int


### Ejemplos operadores comparativos ###
print(3 > 4) #Mayor que
print(3 < 4) #Menor que
print(3 >= 4) #Mayo igual que
print(3 <= 4) #Menor igual que
print(3 == 4) #Igual que
print(3 != 4) #Distinto que
# Los resultados generalmente seran tipo bool 
#Ordenacion alfabetico por ASCII
print("Hola" > "HolaMundo") #Tipo de orden alfabetico
#### Para comparar el lenght de un str ###
print(len("Hola") > len("HolaMundo"))


### Operadores Logicos ### True and/or True = True, False and/or False = False, True and/or False = True
#False
print(3 > 4 and "Hola" > "HolaMundo")
print(3 > 4 or "Hola" > "HolaMundo")
#True
print(3 < 4 and "Hola" < "HolaMundo")
print(3 < 4 or "Hola" < "HolaMundo")
print(3 < 4 or "Hola" < "HolaMundo" and 3 == 3) 
print(3 < 4 or ("Hola" < "HolaMundo" and 3 == 3))
#not
print(not(3 > 4)) #Contradice o no la condicion 