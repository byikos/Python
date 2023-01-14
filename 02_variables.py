# Variable string
my_string_varible = "My String Variable"
print(my_string_varible)


# Variable int
my_int_variable = 22
print(my_int_variable)
# Pasar de varible int a string
print(str(my_int_variable))


# Variable tipo bool
my_bool_varible = False or True
print(my_bool_varible)


# concatenacion de varibles en un print
print(my_string_varible,my_int_variable,my_bool_varible)


# Funcion del sistema * cuenta la cantidad de caracteres
print(len(my_string_varible))
# Se puede definir o especificar con str el print 
print(f'Esta es la cantidad de caracteres de:',len(my_string_varible))


# Variables en una sola linea
name, surname, alias, edad = "Gianfranco", "Gioia", "byikos", 22
print(f'Me llamo:',name, surname,f'Mi alias es:', alias,f'Mi edad es:', edad) #Puede cambiar el orden en que se imprime (¡no se recomienda esta sintaxis!)


'''
Esto es un comentario

# Input como variable 
first_name = input("What is your name?:")
age = input('How old are you?:')

print(first_name)
print(age)


# forzar el tipo de dato de una variable
first_name = input("What is your name?:")
age = input(str('How old are you?:'))

print(first_name)
print(age)
print(type(age))
'''


# Las varibles pueden cambiar su valor a la vez que su tipo de dato
first_name = 22
age = "Gianfranco"
print(first_name)
print(age)


