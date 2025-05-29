import pandas as pd

print('------------------------------------------------')
print('Case Study: Movies Data Analysis')

# Leer archivos CSV
movies = pd.read_csv('movies.csv')
print(movies.head(2))
print(movies.columns)
print(movies.index)
print(movies.shape)

print('---------------------------------------')

tags = pd.read_csv('tags.csv')
print(tags.head(2))
print(tags.columns)
print(tags.index)
print(tags.shape)

print('---------------------------------------')

ratings = pd.read_csv('ratings.csv')
print(ratings.head(2))
print(ratings.columns)
print(ratings.index)
print(ratings.shape)

print('----------------------------------------')
print('Timestamp variables were deleted')
del ratings['timestamp']
del tags['timestamp']

print(ratings.head(2))
print(tags.head(2))

print('----------------------------------------')
# Corregir iloc con lista de índices
print(tags.iloc[[1, 11, 2000]])

print(ratings.head())
print(ratings.tail())

print('------------------------------------------')

# Estadísticas descriptivas
statistics = ratings['rating'].describe()
print(statistics)

# Cálculos adicionales
print('Media:', ratings['rating'].mean())
print('Máximo:', ratings['rating'].max())
print('Moda:', ratings['rating'].mode())  # Devuelve una serie con uno o más valores



filter=ratings['rating']>0
print(filter.any())




print('-------------------movies---------------------------------')

print(movies.shape)

print(movies.isnull().any())

print('-------------------ratings null---------------------------------')

print(ratings.shape)

print(ratings.isnull().any())

print('-------------------tags--------------------------------')

print(tags.shape)

print(tags.isnull().any())

tags=tags.dropna()

print('---------------------Data visualization------------------')

import matplotlib.pyplot as plt
ratings.hist(column='rating',figsize=(15,10))
plt.show()


