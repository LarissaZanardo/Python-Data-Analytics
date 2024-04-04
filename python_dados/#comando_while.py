#comando_while
#usado para repetir o bloco quando nao sabe o numero exato de vezes que o bloco precisa ser executado

opcao = -1
while opcao != 0:
    opcao = int(input("Informe a opcao desejada \n [1]Sacar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacando ..")
    elif opcao == 2:
        print("Exibindo o extrato ..")
print("Saindo ..")