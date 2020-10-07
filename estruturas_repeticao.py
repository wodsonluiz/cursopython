for i in range(10):
    print(i)

convidados = ['wodon','simone', 'joao', 'maria', 'sophia']

for i in convidados:
    print(i + ' esta convidado')

for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + ' esta convidado')

saida = True
contador = 0

while contador < 5:
    contador = contador + 1
        
    print('while contador: ' +  str(contador))
