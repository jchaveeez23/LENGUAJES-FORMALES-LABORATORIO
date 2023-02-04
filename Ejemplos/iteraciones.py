#Iteracion de lista Con for
lista1 = ['a','e','i','o','u']
for i in lista1:
    print(i)
print('------------------------')
#Imprimiendo solo una clave
form = [
    {"Carnet":202100033,"Nombre":"Josue Chavez"},
    {"Carnet":202100039,"Nombre":"Juan Perez"},
    {"Carnet":20224559,"Nombre":"Evan Franco"},
    {"Carnet":202300023,"Nombre":"Ninette Gomez"}
]
for k in form:
    print(k["Nombre"])


print('------------------------')
#Iteracion con while
count = 0           #Variable Contadora
while count < len(lista1):
    print(lista1[count])
    count +=1
print('------------------------')
#Iterar Accediendo a las claves
diccionario = {1:'Perro',2:'Gato',3:'Pez'}
for key in diccionario:
    print(key)
print('------------------------')
#Iterar Accediendo a los valores
diccionario = {1:'Perro',2:'Gato',3:'Pez'}
for value in diccionario:
    print(value)