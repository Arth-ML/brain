import requests
import json
import random

Dolar = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
Dolar = Dolar.json()


##Create second person for transition

##Financing
##buy action



#CREATE OF BANK
    #Register of people(name, age, bank balace)


class Bank():
    def __init__(self):
        self.registre = {}
        self.deposit = {} #keep the customer´s deposit
        self.exit = {} #Valu retied
        self.currency = {} #Currency Convertion
        self.financing = {} #financing




    #Register of people
    def add_register(self,name, age, bank_balance):
        self.registre[name] = {
            'Age': age,
            'balance': bank_balance
        }

    def deposited(self, name, value, bank_balance):
        self.deposit[name] = {
            'Balance': value + bank_balance
        }


##Dolar => currency Value; real_dolar => 1 real = 1 Dollar; c => convert; 
   
  
    def Converte(self, name, dolar, real_dolar, c):
        convert = str(input('You wannt convert yours currency? '))
        if convert == 'Yes':
            self.currency[name] = {
            'Dolar': float(dolar),
            'Real-Dolar': float(real_dolar),
            'Convert': float(c)
        }
        else:
            print('Thanks')

#Financing house and car, age limits == 40 age; not financing salary > 4%

    def finance(self, name, car, house, limits):
        question = str(input('What you want finance [HOUSE/CAR]? '))

        if question == 'House': 
            house_price = float(input('whicht price of house? '))

            if house_price > (4/100) * limits: #limits => value + balance
                ioan = random.uniform(100.000, 1000.0000)
                descont = house_price - ioan
                if  descont == 0:
                    print('paid of')
                else:
                    installments = int(input('In how many installments: '))
                    

        

    def __str__(self):
        info_people = '\n'.join(
            f'Sr(a) {name}, age: {info['Age']}, bank balance {info['balance']:.6}'
            for name, info in self.registre.items()
        )
        value_deposit = '\n'.join(
            f'Sr(a) {name} you have {info['Balance']:.3f}'
            for name, info in self.deposit.items()
        )
        info_convert = '\n'.join(
            f'Sir {name} you converted {info['Convert']:.3f} dollar'
            for name, info in self.currency.items()
        )
        return f'{info_people}\n\n{value_deposit}\n\n{info_convert}'
    
    

if __name__ == '__main__':
    bank = Bank()
    n = 1

    for i in range(n):
        #Create Register
        name = str(input('Enter your name: '))
        age = int(input('Enter your age: '))
        x = random.uniform(0.0, 100.00000)
        bank_balance = x
       
        


        #Deposit
        value = float(input('what amount do you want to deposit: '))
        


        #Currency
        dolar = float(Dolar['USDBRL']['bid'])
        real_dolar =  float(1/dolar)
        c =  float( real_dolar * (value + bank_balance))




        bank.add_register(name, age, bank_balance)
        bank.deposited(name, value, bank_balance)
        bank.Converte(name,dolar, real_dolar,c)
        
        

    print('yours info')
    print(bank)
