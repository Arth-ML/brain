

    # print(alunos[i])for i in range(2):
 #colocando o nome da estrutura de dados e a variavel de iteração podemos acessar ela

# for idx in range(len(alunos)):
#     print(alunos[idx])


disciplinas = ('portugues', 'matematica', 
               'filosofia', 'historia',
               'fisica', 'geografia',
               'quimica', 'biologia')
notas = [
            8.0,4.6,4.5,9.3,
            6.4,7.8,4.5,9.5
]

for i in range(len(notas)):

    print(f'A nota da {disciplinas[i]} foi {notas[i]}')
#Utilizando a variavel de iteração i conseguimos passar por todos os elementos das suas listas
#e agrupando eles