# Consegui implementar apenas com números :(

def lista_de_elementos():
    resposta = 'S'
    lista_um = []
    lista_dois = []
    lista_final = []
    while resposta in 'Ss':
        lista_um.append(int(input("Digite os elementos da lista 1: ")))
        resposta = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

    resposta_dois = 'S'
    print('-' * 50)
    while resposta_dois in 'Ss':
        lista_dois.append(int(input("Digite os elementos da lista 2: ")))
        resposta_dois = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

    lista_final = list(set(lista_um) - set(lista_dois))

    print('-' * 50)
    print(f"Os elementos da lista 1 são: {lista_um}")
    print(f"Os elementos da lista 2 são: {lista_dois}")
    print(f"A diferença entre as listas é {lista_final}")


if __name__ == "__main__":
    lista_de_elementos()