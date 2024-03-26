'''
1- método de classe utilia parâmetro referente a classe
2- método de classe pode acessar ou modificar o estado da classe
3- método o decorator @classmethod para criar um método de classe

'''

class Console:
    # Método construtor
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @classmethod
    def from_text(cls, string):
        import re 
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    

wiiU = Console.from_text('Meu video game é wIIU e o preço é 1000 reias')
xboxOne = Console.from_text('Meu video game é xbox e o preço é 1500 reias')
print(wiiU.__dict__)
print(xboxOne.__dict__)