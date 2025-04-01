
import requests
import json

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = cotacao.json()
dolar = cotacao
print(dolar)


class Bank():
    def __init__(self):
        self.Registre = {} 
        self.balance  = {}
        self.convert = {}
        self.Buy = {}
    

    def registre(self, name, age): #Function responsible of register
        self.Registre[name] = age

    def Balance(self,name,  balance_bank): #Function responsible of balance bank
        self.balance[name] = {
            'Deposit': balance_bank
        }

    def Convert(self,name, dolar, euro, bitcoin): #Function responsible of convert currency other country
        self.convert[name] = {
            'Name': name,
            'dolar': dolar,
            'Euro': euro, 
            'btc': bitcoin
        }

    def buy(self, name, dolar_buy, euro_buy, bitcoin_buy, buy): #Function responsible of buy currency 
        self.Buy[name] = {
            'Name': name,
            'dollar_buy': dolar_buy,
            'Euro_buy': euro_buy,
            'btc_buy': bitcoin_buy,
            'buy': buy
        }

    def __str__(self):
        info_registre = '\n'.join(
            f'Your name is {name}, age: {age}'
            for name, age in self.Registre.items()
        )
        info_babank = '\n'.join(
            f'Sir {name} your balance bank is {info['Deposit']}'
            for name, info in self.balance.items()

        )
        info_convert = '\n'.join(
            f'Sir {name} the dollar this {value['dolar']}, Euro: {value['Euro']}, Bitcoin: {value['btc']}'
            for name, value in self.convert.items()
        )
        info_buy = '\n'.join(
            f'Sir {name} you buy {info['buy']:.4f}'
            for name, info in self.Buy.items()
        )
        return f'{info_registre}\n\n{info_babank}\n\n{info_convert}\n\n{info_buy}'

        
        

if __name__ == '__main__':
    bank = Bank()

    for i in range(1):
        name = str(input('Enter your name: '))
        age = int(input('Whicht your age: '))

        balance_bank = float(input('Enter balance to deposit: '))

        dolar =  cotacao['USDBRL']['bid']
        euro =  cotacao['EURBRL']['bid']
        bitcoin = cotacao['BTCBRL']['bid']

        d = float(cotacao['USDBRL']['bid'])
        e = float(cotacao['EURBRL']['bid'])
        b = float(cotacao['BTCBRL']['bid'])


        dolar_buy = float(1/d)
        euro_buy = float(1/e)
        bitcoin_buy =float(1/b)

        question = str(input('You desire buy currency? '))
        if question == 'Yes':
            type_currency = str(input('Whicht currency? '))
            if type_currency == 'Dollar':
                buy = balance_bank * dolar_buy
            elif type_currency == 'Euro':
                buy = balance_bank * euro_buy
            elif type_currency == 'Bitcoin':
                buy = balance_bank * bitcoin_buy


        bank.registre(name, age)
        bank.Balance(name,balance_bank)
        bank.Convert(name, dolar,euro, bitcoin)
        bank.buy(name, dolar_buy, euro_buy, bitcoin_buy, buy)



    
    print('Your info')
    print(bank)



