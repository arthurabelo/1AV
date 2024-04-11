print('\tSOMA DOS NÚMEROS ÍMPARES')
while True:
    numero = input('\nDigite um número inteiro: ')
    try:
        numero = int(numero)
        if numero < 0:
            print('O número deve ser positivo')
            continue
    except:
        print(f'{numero} não é inteiro')
        continue
    soma = 0
    for n in range(1, numero + 1):
        if n % 2 != 0:
            soma += n
    print(f'A soma dos números ímpares de 0 até {numero} é: {soma}')