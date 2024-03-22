class Movie:
    name = ''
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0
    
    
# 1 primeiro Filme
movie = Movie()
movie.name = 'Super Mario Bros'
movie.yearLaunch = 2023
movie.includePlan = False
movie.note = 5.0
movie.durationMinutes = 130
print('##Dados do Filme 1 ##')
print(f'Nome do filme: {movie.name} \nAno de Lançamento: {movie.yearLaunch}\n')

# 2 Filme 

movie2 = Movie()
movie.name = 'Gladiador'
movie.yearLaunch = 1999
movie.includePlan = True
movie.note = 6.0
movie.durationMinutes = 160
print('##Dados do filme 2 ##')
print(f'Nome do Filme: {movie.name} \nAno de Lançamento: {movie.yearLaunch}')