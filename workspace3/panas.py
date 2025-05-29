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
# del ratings['timestampsource env/bin/activate']
# del tags['timestamp']

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
# ratings.hist(column='rating',figsize=(15,10))
# plt.show()


print(tags.head(3))

tagstworvaribles = tags[['movieId', 'tag']]
print(tagstworvaribles.head(5))

print(ratings.shape)

simplestaken=ratings[1000:1020]
print(simplestaken.shape)
print(simplestaken.head(2))

print(tags.head(3))
tags_counts=tags['tag'].value_counts()
print(tags_counts.shape)
print(tags_counts[:10])

# tags_counts[:10].plot(kind='bar', figsize=(15, 10), color='skyblue', edgecolor='black')
# plt.show()


print(ratings.head(2))
print(ratings.head(4))
is_highly_rated=ratings['rating']>=4
is_highly_rated=ratings[is_highly_rated]
print(is_highly_rated.shape)

print(movies.shape)
print(movies.columns)
print(movies.head(10))


print('----------------------------------------------')
animation_movies = movies['genres'].str.contains('Animation')
animation_movies=movies[animation_movies]
print(movies.shape)
print('Total de películas con el género Animation:')
print(animation_movies.shape)
print(animation_movies.head(5))

print('----------------------------------------------')

ratings_counts=ratings[['movieId','rating']].groupby('rating').count()
print(ratings_counts.shape)
print(ratings_counts)

print('----------------------------------------------')

averge_rating=ratings[['movieId','rating']].groupby('movieId').mean()
print(averge_rating.shape)
print(averge_rating)

print('----------------------------------------------')

contar=ratings[['movieId']].groupby('movieId').count()
print(contar.shape)
print(contar)