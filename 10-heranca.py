class Animal:
    name = ''
    size = ''
    color = ''
    
    
    def eat(self):
        print('Animal se alimentando')
        
class Horse(Animal):
    race = ''
    
    def escape(self):
        print('Cavalo fugindo')
        


class Lion(Animal):
    mane = True
    
    def hunt(self):
        print('Leão caçando')
        
h = Horse() 
h.name = 'Carpiado'
h.color = 'branco'
h.escape() 
h.eat()

l = Lion()
l.name = 'Simba'
l.colro = 'marron'
l.hunt()
l.eat()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    