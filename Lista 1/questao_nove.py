print('\tSEQUÊNCIA DE FIBONACCI')
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

  fib = [1, 1]
  while numero > fib[-1]:
      if (fib[-1] + fib[-2]) > numero:
         print(f'{numero} não pertence à sequência de Fibonacci')
         break
      fib.append(fib[-1] + fib[-2])

  for n in fib:
    print(f'{n}', end = ' ')