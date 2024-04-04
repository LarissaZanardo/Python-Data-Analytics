#Estrutura condicional que permite o fluxo de controle quando determinadas expressoes logicas sao necessarias
#IF condicional simples, se verdadeiro o bloco é executado
#IF
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque autorizado!")
if saldo < saque:
    print("Saldo insuficiente!")

#IF E ELSE
if saldo >= saque:
    print("Saque autorizado")
else:
    print("Saldo insuficiente!")

# caso não é atendida utiliza o else para continuar
    
#ELIF nova expressão logica para testar
