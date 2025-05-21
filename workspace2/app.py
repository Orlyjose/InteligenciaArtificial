import numpy as np




# a=np.array([1,2,3,4,5])

# print(a.shape)


# b=np.array([[1,2,3],[11,22,33]])

# print(b.shape)
# print('Extraer elemento de la fila 1 y columna 2: ',b[1,2])


# print(b)

# print('ok...')




# import numpy as np

# print('MATRIZ COMPLETA')

# # Crear la matriz 7x5 con números aleatorios del 1 al 100
# f = np.random.randint(1, 100, size=(7, 5))
# print(f)

# # Extraer los 4 elementos de las esquinas
# m = np.array([
#     [f[0, 0], f[0, -1]],       # Primera fila: esquina superior izquierda y derecha
#     [f[-1, 0], f[-1, -1]]      # Última fila: esquina inferior izquierda y derecha
# ])

# # Imprimir la submatriz de esquinas
# print('\nSubmatriz seleccionada (esquinas):')
# print(m)




# print('---------------------------------------')
# p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(p)
# filter=(p>5)
# print(filter)
# print(filter.ndim)
# print(filter.shape)
# z=p[filter]
# print(z.shape)
# print(z.ndim)

# print(z)


# print('------------------------------------------')


# # Crear matriz 30x50 con valores entre 1 y 100
# matriz = np.random.randint(1, 101, size=(30, 50))
# print('MATRIZ ORIGINAL:')
# print(matriz)

# # Filtrar SOLO los números entre 40 y 60 (inclusive)
# filtro = (matriz >= 40) & (matriz <= 60)
# valores_filtrados = matriz[filtro]

# print('\nVALORES ENTRE 40 Y 60:')
# print(valores_filtrados)


# valores_filtrados = matriz[(matriz >= 40) & (matriz <= 60)]
# valores_con_cero = np.append(valores_filtrados, 0)

# print('\nVALORES ENTRE 40 Y 60 + CERO AL FINAL:')
# print(valores_con_cero)

# print('------------------------------------------')

# f=np.random.randint(1,101,size=(20,30))
# print(f)
# filter1=(f>40)
# print('filter1')
# print(filter1)
# filter2=(f<60)
# rint('filter2')
# print(filter2)
# f[filter1 & filter2]=0
# print(f)
# print(f.shape)
# print(type(f))



#_______________________________________________________________________________



# f = np.random.randint(1, 101, size=(20, 30))
# print('MATRIZ ORIGINAL:')
# print(f)

# # Filtro 1: valores mayores a 40
# filter1 = (f > 40)
# print('\nFILTER 1 (f > 40):')
# print(filter1)

# # Filtro 2: valores menores a 60
# filter2 = (f < 60)
# print('\nFILTER 2 (f < 60):')
# print(filter2)

# # Aplicar ambos filtros: (valores entre 41 y 59 inclusive) y reemplazarlos por 0
# f[filter1 & filter2] = 0

# # Mostrar matriz resultante
# print('\nMATRIZ CON VALORES ENTRE 41 Y 59 REEMPLAZADOS POR 0:')
# print(f)

# # Mostrar forma y tipo de la matriz
# print('\nFORMA DE LA MATRIZ:', f.shape)
# print('TIPO DE OBJETO:', type(f))


# f[f == 51] = 999

# print('\nMATRIZ CON 51 REEMPLAZADOS POR 999:')
# print(f)

# print("_________________________________")
# print('impares')
# x=np.random.randint(1,101,size=(5,10))
# print("Matriz original:\n", x)
# print('filtro 1')
# impares=(x%2==1)
# print(x)
# print('elevado al cuadrado')
# f[impares]**2
# print(f)



# print('________________________________________')

# a=np.random.ramdin(1,10,size=[2,2])
# b=np.random.ramdin(1,10,size=[2,2])
# print('MATRIX A')

# print(a)
# print('MATRIX B')
# print(b)

# print('adding matrices')
# adding_matrices=np.add(a,b)
# print(adding_matrices)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)




# aux1=np.subtract[a,b]
# aux2=np.multiply[a,b]
# aux3=np.divide[a,b]
# aux4=np.sqrt[a,b]


# print(aux3)


# print('________________________________________')
# a=np.random.randint(1,10,size=(3,3))
# b=np.random.randint(1,10,size=(3,3))


# c=a.dot(b)f = np.random.randint(1, 101, size=(20, 30))
# print('MATRIZ ORIGINAL:')
# print(f)

# # Filtro 1: valores mayores a 40
# filter1 = (f > 40)
# print('\nFILTER 1 (f > 40):')
# print(filter1)

# # Filtro 2: valores menores a 60
# filter2 = (f < 60)
# print('\nFILTER 2 (f < 60):')
# print(filter2)

# # Aplicar ambos filtros: (valores entre 41 y 59 inclusive) y reemplazarlos por 0
# f[filter1 & filter2] = 0

# # Mostrar matriz resultante
# print('\nMATRIZ CON VALORES ENTRE 41 Y 59 REEMPLAZADOS POR 0:')
# print(f)

# # Mostrar forma y tipo de la matriz
# print('\nFORMA DE LA MATRIZ:', f.shape)
# print('TIPO DE OBJETO:', type(f))


# f[f == 51] = 999

# print('\nMATRIZ CON 51 REEMPLAZADOS POR 999:')
# print(f)

# print("_________________________________")
# print('impares')
# x=np.random.randint(1,101,size=(5,10))
# print("Matriz original:\n", x)
# print('filtro 1')
# impares=(x%2==1)
# print(x)
# print('elevado al cuadrado')
# f[impares]**2
# print(f)



# print('________________________________________')

# a=np.random.ramdin(1,10,size=[2,2])
# b=np.random.ramdin(1,10,size=[2,2])
# print('MATRIX A')

# print(a)
# print('MATRIX B')
# print(b)

# print('adding matrices')
# adding_matrices=np.add(a,b)
# print(adding_matrices)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)




# aux1=np.subtract[a,b]
# aux2=np.multiply[a,b]
# aux3=np.divide[a,b]
# aux4=np.sqrt[a,b]


# print(aux3)


# print('________________________________________')
# a=np.random.randint(1,10,size=(3,3))
# b=np.random.randint(1,10,size=(3,3))


# c=a.dot(b)
# print(c)
# print(c.shape)
# print(c.ndim)
# print(c)
# print(c.shape)
# print(c.ndim)



# # 1) Generar matriz de 20×30 con valores aleatorios de 1 a 100
# f = np.random.randint(1, 101, size=(20, 30))
# print('MATRIZ ORIGINAL:')
# print(f)

# # 2) Filtrar valores mayores que 40 y menores que 60 (i.e. 41–59)
# mask_gt40 = (f > 40)
# mask_lt60 = (f < 60)
# mask_between = mask_gt40 & mask_lt60

# print('\nMÁSCARA (valores entre 41 y 59):')
# print(mask_between.astype(int))  # 1 donde está entre 41 y 59, 0 en otro caso

# # 3) Reemplazar esos valores por 0
# f[mask_between] = 0
# print('\nMATRIZ CON VALORES 41–59 REEMPLAZADOS POR 0:')
# print(f)

# print('\nFORMA DE LA MATRIZ:', f.shape)
# print('TIPO DE OBJETO:', type(f))

# # 4) Reemplazar cualquier 51 (si quedara alguno) por 999
# f[f == 51] = 999
# print('\nMATRIZ CON 51 REEMPLAZADOS POR 999:')
# print(f)

# print('\n' + '_'*40)
# # 5) Trabajar con números impares de otra matriz 5×10
# x = np.random.randint(1, 101, size=(5, 10))
# print("Matriz x original:\n", x)

# # Máscara de impares
# mask_impares = (x % 2 == 1)
# print('\nMÁSCARA impares en x:')
# print(mask_impares.astype(int))
# 1) Generar matriz de 20×30 con valores aleatorios de 1 a 100
# f = np.random.randint(1, 101, size=(20, 30))
# print('MATRIZ ORIGINAL:')
# print(f)

# # 2) Filtrar valores mayores que 40 y menores que 60 (i.e. 41–59)
# mask_gt40 = (f > 40)
# mask_lt60 = (f < 60)
# mask_between = mask_gt40 & mask_lt60

# print('\nMÁSCARA (valores entre 41 y 59):')
# print(mask_between.astype(int))  # 1 donde está entre 41 y 59, 0 en otro caso

# # 3) Reemplazar esos valores por 0
# f[mask_between] = 0
# print('\nMATRIZ CON VALORES 41–59 REEMPLAZADOS POR 0:')
# print(f)

# print('\nFORMA DE LA MATRIZ:', f.shape)
# print('TIPO DE OBJETO:', type(f))

# # 4) Reemplazar cualquier 51 (si quedara alguno) por 999
# f[f == 51] = 999
# print('\nMATRIZ CON 51 REEMPLAZADOS POR 999:')
# print(f)

# print('\n' + '_'*40)
# # 5) Trabajar con números impares de otra matriz 5×10
# x = np.random.randint(1, 101, size=(5, 10))
# print("Matriz x original:\n", x)

# # Máscara de impares
# mask_impares = (x % 2 == 1)
# print('\nMÁSCARA impares en x:')
# print(mask_impares.astype(int))

# # Elevar al cuadrado sólo los impares y guardarlos en una nueva matriz y2
# y2 = x.copy()
# y2[mask_impares] = y2[mask_impares]**2
# print('\nx (original) sigue igual):\n', x)
# print('\ny2 (impares al cuadrado):\n', y2)

# print('\n' + '_'*40)
# # 6) Operaciones básicas con matrices 2×2
# # Usar randint, no "ramdin"
# a = np.random.randint(1, 10, size=(2, 2))
# b = np.random.randint(1, 10, size=(2, 2))
# print('MATRIZ A:\n', a)
# print('MATRIZ B:\n', b)

# print('\nSuma (A + B):\n', a + b)
# print('Resta (A - B):\n', a - b)
# print('Multiplicación elemento a elemento (A * B):\n', a * b)
# print('División elemento a elemento (A / B):\n', a / b)

# # También se pueden usar las funciones de numpy
# print('\nSuma con np.add:\n', np.add(a, b))
# print('Resta con np.subtract:\n', np.subtract(a, b))
# print('Multiplicación con np.multiply:\n', np.multiply(a, b))
# print('División con np.divide:\n', np.divide(a, b))

# # Raíz cuadrada de A (elemento a elemento)
# print('\nRaíz cuadrada de A con np.sqrt:\n', np.sqrt(a))

# print('\n' + '_'*40)
# # 7) Producto matricial (dot) de matrices 3×3
# p = np.random.randint(1, 10, size=(3, 3))
# q = np.random.randint(1, 10, size=(3, 3))
# print('MATRIZ P:\n', p)
# print('MATRIZ Q:\n', q)

# c = p.dot(q)  # o bien c = p @ q
# print('\nPRODUCTO MATRICIAL C = P·Q:\n', c)
# print('Forma de C:', c.shape)
# print('Dimensiones de C (ndim):', c.ndim)


# # Elevar al cuadrado sólo los impares y guardarlos en una nueva matriz y2
# y2 = x.copy()
# y2[mask_impares] = y2[mask_impares]**2
# print('\nx (original) sigue igual):\n', x)
# print('\ny2 (impares al cuadrado):\n', y2)

# print('\n' + '_'*40)
# # 6) Operaciones básicas con matrices 2×2
# # Usar randint, no "ramdin"
# a = np.random.randint(1, 10, size=(2, 2))
# b = np.random.randint(1, 10, size=(2, 2))
# print('MATRIZ A:\n', a)
# print('MATRIZ B:\n', b)

# print('\nSuma (A + B):\n', a + b)
# print('Resta (A - B):\n', a - b)
# print('Multiplicación elemento a elemento (A * B):\n', a * b)
# print('División elemento a elemento (A / B):\n', a / b)

# # También se pueden usar las funciones de numpy
# print('\nSuma con np.add:\n', np.add(a, b))
# print('Resta con np.subtract:\n', np.subtract(a, b))
# print('Multiplicación con np.multiply:\n', np.multiply(a, b))
# print('División con np.divide:\n', np.divide(a, b))

# # Raíz cuadrada de A (elemento a elemento)
# print('\nRaíz cuadrada de A con np.sqrt:\n', np.sqrt(a))

# print('\n' + '_'*40)
# # 7) Producto matricial (dot) de matrices 3×3
# p = np.random.randint(1, 10, size=(3, 3))
# q = np.random.randint(1, 10, size=(3, 3))
# print('MATRIZ P:\n', p)
# print('MATRIZ Q:\n', q)

# c = p.dot(q)  # o bien c = p @ q
# print('\nPRODUCTO MATRICIAL C = P·Q:\n', c)
# print('Forma de C:', c.shape)
# print('Dimensiones de C (ndim):', c.ndim)



print('------------------------------------------------------------')
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])

print(a)
print(b)

w=np.array([9,10])
v=np.array([11,12])


tmp1=np.dot(w,v)
tmp2=w.dot(v)


print(tmp1)
print(tmp2)
print(type[tmp1])
print(type[tmp2])

print(tmp1.shape)
print(tmp2.ndim)

tmp3=a.dot(v)
tmp4=np.dot(a,v)

print(type[tmp3])
print(tmp3.ndim)
print(tmp4.shape)



x=np.array([[1,2],[3,4]])

print(x)
result=np.sum(x)
print('el resultado de toda la suma es: ', result)


print('**************Matriz aleatoria y suma por columnas****************')

f = np.random.randint(1, 21, size=(15, 20))
print(f)
columns_sum=np.sum(f,axis=0)
print('la suma de los elemntos es: ',columns_sum)
print(columns_sum.shape)
print('el total de las coluna es:' ,len(columns_sum))
print(columns_sum.ndim)

print('**************Promedios por columna****************')

print('the average of eacha=np.array([[1,2],[3,4]]) comunn are: ', np.sum(f,axis=0)/len(np.sum(f,axis=0)))

print('the average of each comunn are: ', np.mean(f,axis=0))

print('the average of each comunn are: ', np.average(f,axis=0))


print('**************MATRIZ TRANSPOSE****************')

f=np.random.randint(1, 21,size=(4,4))
print(f)
print(f.T)

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
emptyMatrix=np.empty_like(x)
print('________________________________________________________')
result = x + v  
print(result)
print('________________________________________________________')

print(x)
print(v)
print(x.shape)
print('rows: ',x.shape[0])
print('columns: ',x.shape[1])
for i in range(x.shape[0]):
    emptyMatrix[i,:]=x[i,:]+v
    #print(i)
print(emptyMatrix)
print('________________________________________________________')

vv=np.tile(v,(4,1))
print(vv)
print(x+vv)

print('----------------hstack-----------------------')
print('----------------1D-----------------------')
a = np.random.randint(1, 10, size=(5, 7))
b = np.random.randint(10, 20, size=(5, 7))

result = np.hstack((a, b))
print(result)
print('----------------2D-----------------------')

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.hstack((a, b))
print(result)

print('----------------vstack-----------------------')
print('----------------1D-----------------------')
a = np.random.randint(1, 10, size=(5, 7))
b = np.random.randint(10, 20, size=(5, 7))

result = np.vstack((a, b))
print(result)

print('----------------2D-----------------------')

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

result = np.vstack((a, b))
print(result)

print('-----------------------------------------')
# Matriz de 5x7
matriz = np.random.randint(1, 10, size=(5, 7))

# Vector de 5 elementos
vector_columna = np.array([100, 101, 102, 103, 104])

# Vector de 7 elementos
vector_fila = np.array([200, 201, 202, 203, 204, 205, 206])

print('-----------------------------------------')