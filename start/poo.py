##Criando classes e objetos

##Encapsulamento
# é uma forma de juntar ou encapsular dados dentro de uma classe, onde estarem contidas todas as suas informações
# Todas as caracteristas são mantidas dentro da classe não alterando a forma exterior dela

        #####Herança#####
#As heranças são maneiras de alterar caracteristas de objetos e classes semelhante usando somente uma
# modelo de mudança. O modelo automovocel pode ser exemplo disso dentro do modelo automovel
# existe carros, motos, caminhões, todos eles tem o automovel como modelo de referencia.

# class Pessoa: #Usamos o class para criar uma classe
#     def __init__(self, nome: str, idade: int, altura: float):
#         self.nome = nome ##self guarda a referencia desse objeto
#         self.idade = idade
#         self.altura = altura
    
#     def dizer_ola(self):
#         print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}')
    
#     def cozinhar(self, receita: str):
#         print(f'Estou cozinhando um(a): {receita}')

# #__init__ construtor ele que inicia os objetos

# pessoa = Pessoa(nome='Arthur', idade=28, altura=1.82) ##o __init___ entrar em ação aqui, quando instanciamos a classe Pessoas

# pessoa.dizer_ola()
# pessoa.cozinhar('Arroz')


# class jogador:
#     def __init__(self, nome: str, idade: int, time: str):
#         self.nome = nome
#         self.idade = idade
#         self.time = time
    
#     def apresentacao(self): #O self nos permite acessar outros atributos dentro da class
#         print(f'Olá, meu nome é {self.nome}, e tenho {self.idade} anos, sou jogador do {self.time}')
    
# atleta = jogador(nome='Arthur,', idade = 18, time = 'Corinthians')
# atleta.apresentacao()


        #####Atributos#####

#Atributos de extancia: feito para a o objeto criado
#Atributos de classe: São compartilhados em todas as extancias

class pessoa:
    def __init__(self, v_contrutor):
        self.nome = 'Arthur'
        self.sobrenome = 'Rodrigues'
        self.lista = ['Joao', 'Ana']
        self.dicionario = {'Nome':'Marcos' ,'idade':18}
        self.aluno = v_contrutor

    def unir_nome(self):
        self.nome_completo = self.nome + self.sobrenome
        print(f'{self.lista}')
        print(f'{self.dicionario}')
        print(f'{self.aluno}')



v_construtor = 'nicolas'

Pessoa = pessoa()
pessoa.unir_nome()


























