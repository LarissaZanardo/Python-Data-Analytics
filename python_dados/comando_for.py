#comando for, quando sabemos o numero exato de vezes
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


for letra in texto:   #letra é a variavel voce escolhe o nome e texto é o que o for vai percorre
    if letra.upper() in VOGAIS: #letra.upper transforma em maiuscula 
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Executa bo final do laço")