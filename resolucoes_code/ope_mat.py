# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita dois números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe o menu de operações
print("\nEscolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Solicita a operação desejada
opcao = input("Digite o número da operação: ")

# Realiza a operação escolhida
if opcao == "1":
    resultado = num1 + num2
    operacao = "Soma"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "Subtração"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "Multiplicação"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "Divisão"
    else:
        resultado = "Erro: divisão por zero não é permitida."
        operacao = "Divisão"
else:
    resultado = "Operação inválida."
    operacao = "Desconhecida"

# Exibe o resultado
print(f"\nResultado da {operacao}: {resultado}")