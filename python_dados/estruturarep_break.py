#break
""""
opcao = -1

 while True:
    opcao = int(input("informe um numero: ")) #fica sempre perguntando um numero e mostrando

    if opcao == 10: #quando digitar 10 ele para.
        break
    print(opcao)
 
"""
#range com break para contar e parar no break
""""
for numero in range(100): # irira contar ate 100
    if numero == 12: #condicao quando chegar no 12
        break #break no 12 só exibe ate o 11
    print(numero, end=" ")
"""
#continue ele pula o numero do continua e prossegue
"""""
for numero in range(100): # contar ate 10
    if numero == 12: #condicao quando chegar no 12
        continue #pula o 12 e continua exibindo o resto
    print(numero, end=" ")

"""""


#mostrar só os impares com range
"""""
for numero in range(100):
    if numero % 2 == 0: #verifica numeros pares
        continue #pular os pares
    print(numero, end=" ")
"""


while True:
    numero = int(input("informe um numero: ")) #fica sempre perguntando um numero e mostrando

    if numero == 10: #quando for 10 ele corta execução
        break
    
    if numero %2 == 0: #se o numero for par ele nao mosta, só mostra impar
        continue
  

    print(numero)

    
