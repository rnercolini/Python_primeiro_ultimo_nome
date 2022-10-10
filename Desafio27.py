# Retorna o primeiro e último nome.
nome = str(input('Digite um nome completo: ')).strip()
#Exibir o primeiro e o último nome:
divide = nome.split()
print('O primeiro nome é: {}'.format(divide[0]))
print('O último nome é: {}'.format(divide[-1]))

#Outra forma de encontar o último nome:
print('O último nome é: {}'.format(divide[len(divide)-1]))
