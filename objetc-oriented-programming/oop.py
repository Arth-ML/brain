# new data type: currrency
# number value

## the class thery are terms abstract where can we idealize them.
## Objects are concrete terms that we can see

CURRENCY_NAME = {
    'dolar': 'Dollar of United States',
    'BRL': 'Real'
}


class Currency:
    def __init__(self, value, code):  
        self.value = value  #The self represents the objete we can going to creat
        self.code = code.upper()

    
    def __str__(self): #return some string, represents yours objects
        return f'{self.value:.2f} {self.code}'
    
    def __eq__(self, rhs): #Equality comparation
        if self.code == rhs.code and self.value == rhs.value:
            return 'Equality Currency' or True
        else:
            return 'The currency is not equal' or False
        
    def __gt__(self, rhs): #The method __gt__ compare bigger and smaller 
        if self.code == rhs.code:
            return self.value > rhs.value
        raise ValueError('Coins must be from the some country')
    
    def __ge__(self, rhs): #The method __ge__ compare less than or equal 
        if self.code == self.code:
            return self.value >= rhs.value
        
    def __add__(self, rhs): #The method __add__ add value
        if self.code == rhs.code:
            return Currency(self.value + rhs.value,
                            self.code)
    
    def __sub__(self, rhs):
        if self.code == rhs.code:
            return Currency(self.value - rhs.value, 
                            self.code)
    
    def __mul__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Currency(rhs * self.value, self.value)
        raise ValueError(f'{rhs} deve ser um NUMERO')
        
    
if __name__ == '__main__':
    moeda = Currency(54, "BRL") #Atributed value on value and code  
    moeda_two = Currency(51, 'BRL')
    print(moeda)
    print(moeda_two)
    print(moeda == moeda_two)
    print(moeda <= moeda_two )
    print(moeda + moeda_two)
    print(moeda - moeda_two)









# print(moeda.value)
# print(moeda.code)
# print('Name of currency:', CURRENCY_NAME[moeda.code])