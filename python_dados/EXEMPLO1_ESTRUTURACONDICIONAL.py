MAIOR_IDADE = 18
IDADE_ESPECIAL = 16
idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
   print("Voce ja pode tirar sua CNH!")
if idade < MAIOR_IDADE:
   print("Voce não pode tirar a CNH!")


if idade >= MAIOR_IDADE:
   print("Voce ja pode tirar a CNH")
else:
   print("Voce não pode tirar a CNH")

if idade >= MAIOR_IDADE:
   print("Voce ja pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Voce pode iniciar suas aulas teoricas ")
else:
   print("Voce nao pode tirar a CNH")

   


