'''
1- método estático não  utilia parâmetro referente a classe
2- método estático pode acessar mas não pode modificar  o estado da classe
3- método o decorator @classmethod para criar um método de stático
'''

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
        
    # método estático
    @staticmethod # decoreitor
    def courses_trail(trail):
        if trail == 'Python Fundamentos':
            courses = ['Dominando o Python', 'Módulos e Pip', 'Orientação a Objeto']
        elif trail == 'Automação com o Python':
            courses = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual em Python']
        else:
            courses = ['A definir']
        return courses            
    
print(Course.courses_trail('Python Fundamentos'))
print(Course.courses_trail('Análise de Dados'))
print(Course.courses_trail('Automação com o Python'))