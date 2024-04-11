print('\tFATORIAL')
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
  fatorial = 1
  for n in range(1, numero + 1):
    fatorial *= n
  print(f'{numero}! = {fatorial}')