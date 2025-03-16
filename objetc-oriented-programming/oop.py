# new data type: currrency
# number value

## the class thery are terms abstract where can we idealize them.
## Objects are concrete terms that we can see

from data import CURRENCY_NAME, EXCHANGE_RATES

class Currency:
    def __init__(self, value, code):  
        self.value = value  #The self represents the objete we can going to creat
        self.code = code.upper()

    
    def __str__(self): #return some string, represents yours objects
        return f'{self.value:.2f} {self.code}'
    
    def __eq__(self, rhs): #Equality comparation
        if self.code == rhs.code:
            return 'Equality Currency' or True
        else:
            return 'The currency is not equal' or False
        
    def __gt__(self, rhs): #The method __gt__ compare bigger and smaller 
        if self.code == rhs.code:
            return self.value > rhs.value
        return self > rhs.convert(self.code)
    
    # raise ValueError('Coins must be from the some country')
    
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
    
    def convert(self, to_code):
        to_code == to_code.upper()
        rate = EXCHANGE_RATES[self.code][to_code]
        return Currency(rate * self.value, to_code)

        
    
if __name__ == '__main__':
    moeda1 = Currency(10, 'USD')
    moeda2 = Currency(50, 'BRL')
    print(moeda1)
    print(moeda1.convert('BRL'))

    print(moeda1 > moeda2)
