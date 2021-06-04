def lista_de_numeros():
    resposta = 'S'
    numeros = []
    while resposta in 'Ss':
        numeros.append(int(input("Digite um numero inteiro: ")))
        resposta = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

    print('-' * 50)
    print(f"Sua lista de números é: {numeros}")
    print(f"O primeiro número digitado é: {numeros[0]}")
    ultimo = numeros[-1]
    print(f"O último número digitado é: {ultimo}")

if __name__ == "__main__":
    lista_de_numeros()


