nome = input('Qual é o seu nome? ')
nome2 = input('Qual é o seu segundo nome? ')
sobrenome = input('Qual é o seu sobrenome? ')
idade = input('Sua idade? ')
ano_nascimento = 2024 - int(idade)
altura_metros = input('Quantos metros de altura você tem? ')
maior_idade = int(idade) >= 18

print(f'Nome: {nome}')
print(f'Segundo nome: {nome2}')
print(f'Sobrenome: {sobrenome}')
print(f'Seu nome completo é {nome} {nome2} {sobrenome}.')
print(f'Idade: {idade}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'É maior de idade? {maior_idade}')
print(f'Altura em metros: {float(altura_metros)}')

# Feito em 22/12/24