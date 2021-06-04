def lista_de_numeros():

    numeros = [[], []] #duas listas, para separar os numeros
    valor = 0
    resposta = 'S'

    for i in range(1, 11): #A lista aceita 10 números
        valor = int(input(f"Digite o {i}º número inteiro: "))
        if valor % 2 == 0:
            numeros[0].append(valor)
        else:
            numeros[1].append(valor)

    print('-' * 50)
    numeros[0].sort()
    numeros[1].sort()
    print(f"O números ímpares são: {numeros[1]}")
    print(f"O números pares são: {numeros[0]}")

if __name__ == "__main__":
    lista_de_numeros()

