idade = 29

print('minha idade é ' + str(idade))

print('minha idade é: {}'.format(idade))

print(f'minha idade é: {idade}')

nome = 'wodson luiz '
nome2 = 'wodson luiz asdfasd fasd fasd fasd fadsf asdf asd fasdf asd fasdf asd fadsf'

print(f'meu nome é {nome} e eu tenho {idade} anos')

# formatando a quantidade de caracteres
print(f'meu nome é {nome2:.17} eu tenho {idade:03} anos')

dinheiro = 2.776

print(f'eu tenho {dinheiro:.2f}')

lista_itens =['garfo', 'prato', 'copo', 'refri']

print(f'eu almoço com {lista_itens[0]} e {lista_itens[1]} tomando {lista_itens[-1]}')

print(f'eu terei {idade + 30} anos daqui a 30 anos')