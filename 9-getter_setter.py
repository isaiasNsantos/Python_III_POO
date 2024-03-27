class Employee:
    def __init__(self, name, salary):
        self.name = name # esta publico - pode ser alterado 
        self.__salary = salary # como o __  na frente ativamos o modficador privado  
        
    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')
        
# método de Buscar dados

def get_salary(self):
    return self.__salary

# método para modificar  atributo privado 
def set_salary(self, salary):
    self.__salary = salary
    
fulano =  Employee('Fulano', 4000)
sicrano =  Employee('Sicrano', 7000)
fulano.name = 'Fulano 2'
fulano.show()
sicrano.show()
fulano.show()
fulano.set_salary(12)