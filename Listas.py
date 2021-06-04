"""

#1 - funcao para listas em python

"""

#função de lista
#type é bastante utilizado
def listas():
    #colchetes está ligado ao conceito de lista, se tem colchete, é uma lista
    professores = ["Douglas", "Maicon", "Fabiano", "Anderson", "Ivania"]

    print(type(professores)) #mostra o tipo do objeto
    print(len(professores)) #ao aplicar em uma str, retorna o número de caracteres
    print(professores[2])

    professores.append("Andrieli") #inclui um novo valor, ao final da lista
    professores.insert(2,"Carraro") #espera o indice, espera o valor
    print(professores)

    #remover da lista, por valor ou indice
    professores.remove("Ivania")
    professores.pop(3)
    print(professores)

    #aceita vários valores
    aleatorio = ["Douglas", 90.00, 45, False, True]
    print(aleatorio)

#função tupla
def tupla():

    #usamos colchetes
    doenca = ("covid")
    #uma lista que nunca vai mudar
    # quando eu preciso de mais itens, vai continuar sendo uma tuple
    doencas = ("covid","sars", "tuberculone" ,89, False)

    vogais = ("A", "E", "I", "O", "U")
    print(vogais[2]) #mostra o que está no indice 2, sendo o I
    print(type(doencas))

    #tuplas não suportam associação de itens, ou seja, não suportam alteração dos itens que nela estão
    #Tuplas sao listas que nunca vao mudar

#Dicionários
#grandes colecoes de dados. Assinatura de indices e valores
def dicionarios():

    #As chaves indicam dicionário no python
    #colecoes malucas que você faz o que quiser
    dados_de_professor = {
        "nome":"douglas",
        "telefone":"46 9 8836 18370",
        "endereco":"rua do douglas"
    }
    #criando mais uma chave, e associando um valor a ela
    dados_de_professor["idade"] = "24"

    #quando associo um valor nulo, a uma chave dentro de um dicionário, ele não faz nada
    dados_de_professor.pop("idade", None)

    #limpa todos os valores que tem no telefone, inclusive ele
    del dados_de_professor["telefone"]

    print(dados_de_professor)

def funcoes_prontas():
    lista_numeros = [1,2,3,4,5.4]
    lista_nomes = ["douglasbzzzz", "Maicon", "Liborio junior", "fabiano luiz", "xvania"]

    print(min(lista_nomes))
    print(min(lista_numeros))
    print(max(lista_numeros))
    print(max(lista_nomes))

    print(sum(lista_numeros))#soma os valores da biblioteca


#serve para saber qual função o terminal irá executar
#como se fosse nosso método main
if __name__ == "__main__":
    # listas()
    # tupla()
    # dicionarios()
    funcoes_prontas()