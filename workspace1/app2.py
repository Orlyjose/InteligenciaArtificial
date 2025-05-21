

#pairis key and the other value

# Pairs: key and the other value
myDictionary = {'cat': 'cute', 'dog': 'friend', 'Donkey': 'hard-working'}

# Imprimir valor asociado a la clave 'Donkey'
print(myDictionary['Donkey'])

# Verificar si 'cat' está en el diccionario
print('cat' in myDictionary)

# Agregar una nueva clave 'fist'
myDictionary['fist'] = 'wet'

# Recorrer usando solo las claves
for key in myDictionary:
    animal = myDictionary[key]
    print('The %s is %s' % (key, animal))

print('ANOTHER WAY TO PRINT DICTIONARIES')

# Recorrer usando key y value directamente
for key, value in myDictionary.items():
    print('The %s is %s' % (key, value))


#DICTIONARY={'1':1,'2':4.............}
print('-------------------------------------------------------------------------')

myDictionary1 = {i: i**2 for i in range(20)}
print(myDictionary1)


print('-------------------------------------------------------------------------')

print('SET CONTAINER')
animals = {'cat', 'dog', 'chicken', 'hen', 'monkey'}  # Usar set, no tupla

print('fish' in animals)  # Verifica si 'fish' está en el set

animals.add('fish')  # Agrega 'fish' al set
print(animals)       # Muestra el set actualizado
animals.add('mouse')
print(animals)

number0fElements=len(animals)
print(animals)

animals.remove('fish')  # Elimina 'fish'
print(animals)
print(type(animals))
print(len(animals))

print('-------------------------------------------------------------------------')

print('TUPLES')

tupleData = (10, 5, 8)

# Verificar el tipo de la tupla
print(type(tupleData))

# Convertir tupla en lista
listData = list(tupleData)
print(type(listData))  # Verificar el tipo de la lista
print(listData)        # Mostrar la lista convertida


listData.remove(5)  # Elimina el primer '5' encontrado
print(listData)     # Muestra la lista actualizada

listData.pop(0)  # Elimina el elemento en el índice 0 (primer elemento)
print(listData)  # Muestra la lista actualizada



