#permite escrever uma condição em uma unica linha

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"  #atribui falha ou sucesso a variavel status
print(f"{status} ao realizar o saque!")