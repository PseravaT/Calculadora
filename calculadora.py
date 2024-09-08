def menu():
    print("Bem vindo à Calculadora")
    print("Qual a operação que você deseja fazer?")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Digitar outros números")
    print("6 - Finalizar")

num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))

selecao = 0

while selecao != 6:
    menu()
    selecao = int(input("Digite sua opção: "))

    match selecao:
        case 1:
            resp = num1 + num2
            print(f"A soma de {num1} com {num2} é {resp}")
        case 2:
            resp = num1 - num2
            print(f"A subtração de {num1} por {num2} é {resp}")
        case 3:
            if num2 != 0:
                resp = num1 / num2
                print(f"A divisão de {num1} por {num2} é {resp}")
            else:
                print("Divisão por zero não é permitida")
        case 4:
            resp = num1 * num2
            print(f"A multiplicação de {num1} por {num2} é {resp}")
        case 5:
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))
        case 6:
            print("Finalizando...")
        case _:
            print("Opção inválida, tente novamente.")
