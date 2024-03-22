class Movie:
    def __init__ (self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    # metodo especial - sobrescreve    
    def __str__(self):
        return f'Filme: {self.name}'
          
        
# OBJETOS DA CLASS
movie = Movie("Super mario Bros", 2023, False, 5.0, 130)
movie2 = Movie('Avatar', 2023, False, 4.5, 250)
print(movie.name)
print(movie.note)
print(movie.yearLaunch)
print(movie.durationMinutes)
print('')

print(movie2.name)
print(movie2.note)
print(movie2.yearLaunch)
print(movie2.durationMinutes)



  