# classe PAI
class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand # "_" atributo protegido
        self._model_name = model_name
        self._price = price
        
    def __str__(self):
        return f'{self._brand}{self._model_name}'
    
    # metodo estatico
    @staticmethod
    def make_a_call(phone_num):
        print(f'Ligando para {phone_num}')
        
# CLASS FILHA
class SmarPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)  # super, vc invoca os valores da CLASS PAI
        
        self.ram = ram 
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        

# instanciando a classe PAI
moto = Phone('Moto', 'G7', 1000)
print(moto) 
moto.make_a_call(1234554)
print(f'O valor do {moto._brand} {moto._model_name} é {moto._price}')
print(vars(moto))
print(30*"-")

Iphone = SmarPhone('Iphone', '13', 5000, '4gb', '128gb', '25mp')
print(Iphone)
Iphone.make_a_call(122345564)
print(f'O valor do {Iphone._brand}{Iphone._model_name} é {Iphone._price}')
print(vars(Iphone))

