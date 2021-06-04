from csv import DictWriter

with open("Campeonato.csv", "w") as arquivo_escrita:

    cabecalho = ["time", "pontos_vitorias", "pontos_empates", "pontos_derrotas", "pontos_totais"]
    escrita = DictWriter(arquivo_escrita, fieldnames=cabecalho)  # atribui ao fildname do arquivo o cabecalho
    escrita.writeheader()  #escrever o cabecalho

    time = None

    while time != "sair":
        time = input("Digite o nome do time: ")
        if time != "sair":
            vitorias = int(input("Informe a quant. de vitorias: "))
            pontos_v = (vitorias * 3) #calcula os pontos
            empates = int(input("Informe a quant. de impates: "))
            derrotas = int(input("Informe a quant. de derrotas: "))
            pontos_d = (derrotas * 0) #calcula os pontos

            total_pontos = (pontos_v + pontos_d + empates) #calcula total dos pontos

            classificacao_times = {
                "time": time,
                "pontos_vitorias": pontos_v,
                "pontos_empates": empates,
                "pontos_derrotas": pontos_d,
                "TOTAL DE PONTOS": total_pontos
            }
            print(classificacao_times) #mostra a quantidade de pontos dos times

            escrita.writerow( #armazena os valores no arquivo csv
                {"time": time, "pontos_vitorias": pontos_v, "pontos_empates": empates,
                 "pontos_derrotas": pontos_d, "pontos_totais" : total_pontos})  # escreve uma linha no arquivo


