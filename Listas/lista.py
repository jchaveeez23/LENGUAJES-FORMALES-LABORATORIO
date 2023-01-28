lista1 =        ['a','b','c','d','e','f','g']
#Posiciones      0    1   2   3   4   5   6
#Inverso        -7   -6  -5  -4  -3  -2  -1

#Append: Agrega un item a la lista en la ultima posición
lista1.append('h')
print(lista1[:])

#Clear: Limpia la lista
#lista1.clear()
#print(lista1[:])


#Extend: Agrega el contenido de una lista a otra
lista2 = ['Medio Metro', 'b','Chupapimuñaño']
lista2.extend(lista1)
print(lista2[:])

#Count: Cuenta los datos repetidos
print('count: ',lista2.count('b'))

#Index: Encuentra la posicion en donde se ecuentra el item
print('index: ',lista2.index('Medio Metro'))

#Insert: Agrega un item a la lista en una posicion especifica
lista2.insert(1,'A correr los lakers')
print('insert: ',lista2[:])

#Pop: Extrae y elimna un dato de la lista
aux = lista2.pop(2)
print('pop: ',lista2[:])
print('pop: ',aux)

#Reverse: Da la vuelta a la lista
lista2.reverse()
print('reverse: ',lista2[:])

#Sort: Ordena ascendentemente los items
lista2.sort()
print('sort :',lista2[:])