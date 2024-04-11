print('\tNÚMEROS PARES ATÉ O NÚMERO')
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
    print(f'Números pares de 0 até {numero}: ')
    if numero > 0:
        for n in range(0, numero + 1):
            if n % 2 == 0:
                print(n, end=' ')
    else:
        for n in range(numero, 0):
            if n % 2 == 0:
                print(n, end=' ')
