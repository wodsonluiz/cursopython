idade = 30
if idade < 20:
    print("Você é jovem!")
else:
    print("maior de idade")

veiculo = {'tipo': 'moto', 'marca': 'Honda', 'potencia_motor': 140}

if veiculo['tipo'] == 'moto' and veiculo['marca'] == 'Honda':
    print('o veiculo é uma moto')
else:
    print( 'o veiculo é um carro')
    
resultado = veiculo['tipo'] == 'moto'

print(resultado)

if veiculo['tipo'] == 'wodson' or veiculo['potencia_motor'] < 120:
    print('vc tem um veiculo mto rapido')
else:
    print('seu veiculo não é rapido')


if (veiculo['tipo'] == 'moto2' and veiculo['potencia_motor'] > 120) or veiculo['marca'] == 'Honda':
    print('o seu veiculo é mto bom')

if veiculo['tipo'] == 'moto':
    print('moto')
elif veiculo['tipo'] == 'carro':
    print('carro')
elif veiculo['tipo'] == 'navio':
    print('navio')
  
condicao = 1

if condicao:
    print('verdadeiro')
else:
    print('falso')

condicao2 = True

if condicao2:
    print('verdadeiro')
else:
    print('falso')

condicao3 = []

if condicao3:
    print('verdadeiro')
else:
    print('falso')

condicao4 = {'chave': 'valor'}

if condicao4:
    print('verdadeiro')
else:
    print('falso')

# O None sempre vai se resolver como False
condicao5 = None

if condicao5:
    print('verdadeiro')
else:
    print('falso')

condicao6 = [1,2,3]

if len(condicao6):
    print('verdadeiro')
else:
    print('falso')

print(len(condicao6))