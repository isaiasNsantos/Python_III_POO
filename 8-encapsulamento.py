class Employee:
    def __init__(self, name, salary):
        self.name = name # esta publico - pode ser alterado 
        self.__salary = salary # como o __  na frente ativamos o modficador privado  
        
    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')
        
fulano = Employee('Fulano', 4000)
sicrano = Employee('Sicrano', 5000)

fulano.show()
sicrano.show()

# alteração manual
fulano.__salary = 40000
fulano.show()

