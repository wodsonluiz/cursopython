# lista (tipo mutavel)
lista_convidados = ['Wodson', 'simone', 'maria','joao']

print(lista_convidados)

lista_convidados.append('sophia')

print(lista_convidados)

lista_convidados.remove('Wodson')

print(lista_convidados)

print(lista_convidados[0])

print(lista_convidados[3])
print(lista_convidados[-1])

lista_convidados.append(29)
print(lista_convidados)

# tuple (tipo imutavel)
tupla1 = (1, 2, 3, 4)
tupla2 = (5,6,7)

print(tupla1)

tupla3 = tupla1 + tupla2

print(tupla3)

# dicionario Chave -> Valor

dados_pessoais = {'nome': 'batman', 'cidade':'Gothan'}

print(dados_pessoais)

dados_pessoais['veiculo'] = 'batmovel'

print(dados_pessoais)

del dados_pessoais['cidade']

print(dados_pessoais)