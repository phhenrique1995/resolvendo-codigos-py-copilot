#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")