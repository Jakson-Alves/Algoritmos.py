import random

print("olá meu paladino")

#definindo um número a ser sorteado

numero_a_ser_descoberto = random.randrange(0,101)

#variaveis
n_tentativas = 0
tentativa = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1)Fácil , (2)Médio , (3)Difícil")

nivel_dificuldade = int(input("Defina o nível: "))

if(nivel_dificuldade == 1):
    n_tentativas = 10
elif(nivel_dificuldade == 2):
    n_tentativas = 5
else:
    n_tentativas = 3

for tentativa in range(1, n_tentativas + 1):
    print(f"Tentativa {tentativa} de {n_tentativas}")
    chute_str = input("Digite seu chute(1-100): ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você é um bocó, que não sabe ler")
        continue

    acertou = chute == numero_a_ser_descoberto
    maior = chute > numero_a_ser_descoberto
    menor = chute < numero_a_ser_descoberto

    print(f"O seu chute foi: {chute}")

    if(acertou):
        print(f"Você acertou! Você acertou o numero era {numero_a_ser_descoberto}, "
              f", seu placar foi: {pontos}")
        break
    else:
        if(maior):
            print("Você errooooou, seu palpite foi MAIOR do que o numero sorteado")
        elif(menor):
            print("Você errooooou, seu palpite foi MENOR do que o número sorteado")
        pontos_perdidos = abs(numero_a_ser_descoberto - n_tentativas)
        pontos -= pontos_perdidos

print("end game")


