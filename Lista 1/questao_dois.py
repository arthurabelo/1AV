def soma(num1,num2):
  soma = num1+num2
  return soma

def produto(num1,num2):
  produto = num1*num2
  return produto

def diferenca(num1,num2):
  diferenca = num1-num2
  return diferenca

def divisao(num1,num2):
  divisao = num1//num2
  resto = 0
  if num1%num2 != 0:
    resto = num1%num2
  return divisao, resto

if __name__ == '__main__':
  while True:
    print('\tSOMA, PRODUTO, DIFERENÇA E DIVISÃO')
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("A soma dos números é: ",soma(num1,num2))
    print("O produto dos números é: ",produto(num1,num2))
    print("A diferença dos números é: ",diferenca(num1,num2))
    resultado_divisao = divisao(num1,num2)
    print("A divisão dos números é: ", resultado_divisao[0])

    if resultado_divisao[1] != 0:
      print("O resto da divisão é: ",resultado_divisao[1])