from csv import reader
from csv import DictReader
from csv import DictWriter


def lendo_csv_reader():
    print("[+] Lendo ManipulandoCSV usando CSV_READER")

    with open("exemplo.csv") as arquivo: #abrindo o arquivo exemplo.csv e atribuindo para arquivo
        leitor = reader(arquivo, delimiter=",") #lendo o arquivo e definindo o demilimitador ,

        # print(type(leitor))
        next(leitor) #retornar o próximo valor da interação
        #strip remove espaço
        for linha in leitor: #para cada linha do vetor, quero que me mostre
            print(f"O {linha[0].strip()} {linha[1].strip()}, tem {linha[2].strip()}"
                  f"anos e mora na rua: {linha[3].strip()}.") #o .strip retira os espaços em branco do inicio e fim da linha

def lendo_csv_dict():
    print("[+] Lendo DICT_READER")
    with open("exemplo.csv") as arquivo_dict:
        leitor_csv_dict = DictReader(arquivo_dict, delimiter=",")
        for linha in leitor_csv_dict:
            print(f"O {linha['nome'].strip()} {linha['sobrenome'].strip()}, tem {linha['idade'].strip()}, e mora na rua: {linha['endereco'].strip()}.")

def escrever_csv():
    #write é para comecar a escrever
    with open("filmes.csv", "w") as arquivo_escrita:
        cabecalho = ["titulo" , "duracao", "genero", "ano"] #cria uma lista para o cabecalho
        escrita = DictWriter(arquivo_escrita, fieldnames=cabecalho) #atribui ao fildname do arquivo o cabecalho
        escrita.writeheader()#escrever o cabecalho

        filme = None #variavel de parada do while, e recebe o tipo do filme

        while filme != "sair": #se filme diferente de sair, execute
            filme = input("Digite o nome do filme: ") #input recebe do usuário o que é digitado
            if filme != "sair": #se filme diferente de sair, execute
                duracao = input("Informe a duracao do filme em minutos: ")
                genero = input("Informe o genero do filme: ")
                ano = int(input("Informe o ano de lancamento deste filme: "))
                escrita.writerow({"titulo":filme, "duracao":duracao, "genero":genero, "ano":ano}) #escreve uma linha no arquivo


if __name__ == "__main__":
    lendo_csv_reader()
    # lendo_csv_dict()
    # escrever_csv()