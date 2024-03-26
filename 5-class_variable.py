class Movie:
    platform = 'OneBitFilmes'
    def __init__ (self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
        
        
    # metodo especial - sobrescreve    
    def __str__(self):
        return f'Filme: {self.name}'
    
    # estanciando uma classe
    def techinal_sheet(self):
        print('##Dados do filme##')
        print(f'Plataforma: {Movie.platform}')
        print(f'Nome do Filme: {self.name}')
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Está no plano: {self.includedPlan}')
        print(f'Avaliação do Filme: {self.totalEvaluation}')
        print(f'Duração  do Filme: {self.durationMinutes}\n')
        print(f'Avaliadores dos Filmes: {self.evaluators}\n')
        
    def evaluate(self, note):
         self.totalEvaluation += note
         self.evaluators += 1
         
    def average(self):
        print(f'Média do filme {self.name}: {self.totalEvaluation / self.evaluators}')
         

mario = Movie('Super Mario Bros', 2023, False, 125)
avatar = Movie('Avatar', 2023, False, 180)


mario.evaluate(9.5) 
mario.evaluate(10)
mario.techinal_sheet()
mario.average()
 
# modificando a plataforma 
Movie.platform = 'OneBitCode Pro'

avatar.evaluate(9.5) 
avatar.evaluate(10)
avatar.techinal_sheet()
avatar.average()
        