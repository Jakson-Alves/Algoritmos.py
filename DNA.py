#Compactar a estrutura básica de DNA

#classe em python
class GeneCompactado:
    #construtor, esse método devolve um vazio, ou seja, nada (tipo o void no java)
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    #esse método passa o gene como uma string, e vai fazer um processamento com isso
    def _compress(self, gene: str) -> None:
        #atributo do tipo inteiro, iniciando em um, Chamamos ele de SENTINELA
        self.bit_string: int = 1 #sentinela

        for nucleotideo in gene.upper():
            self.bit_string <<= 2  #faz o deslocamento da string duas casas para a esquerda

            if nucleotideo == "A": #Se o nucleotideo for igual a A, vai mudar os dois ultimos bits para 00
                self.bit_string |= 0b00 #Compara ou atribui a cadeia de bits
            elif nucleotideo == "C": #Quando for C, mudar os ultimos bits para 01
                self.bit_string |= 0b01
            elif nucleotideo == "G": #Mudar os dois ultimos bits para 10
                self.bit_string |= 0b10
            elif nucleotideo == "T": #Mudar os dois ultimos bits para 11
                self.bit_string |= 0b11

            else: #Caso o que eu tenha passado não seja uma das letras acima
                raise ValueError(f"Nucleotideo nao eh valido: {nucleotideo}")

    def descompacta(self) -> str: #O retorno esperado dele é uma str
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int =  self.bit_string >> i & 0b11 #movendo apenas os dois ultimos bits de referencia.
            if bits == 0b00: #A
                gene += "A"
            elif bits == 0b01: #C
                gene += "C"
            elif bits == 0b10: #G
                gene += "G"
            elif bits == 0b11: #T
                gene += "T"
            else:
                raise ValueError(f"bit inválidos:  {bits}")
        return gene [::-1] #inverter a string usando fatiamento

    def __str__(self) -> str: #devolve uma string
        return self.descompacta() #o descompacta vai retornar como string para o usuário

if __name__ == "__main__":
    from sys import getsizeof #biblioteca para trabalhar com tamanhos
    str_original: str = "TTTTAGCTAGCCCTAAAGGGGGCTAGCCCTAAAAGCTAGCTAGCAAGGGTTTCCCGGG"*100
    print(str_original)
    print(f"O gene original possui: {getsizeof(str_original)} bytes")
    str_compactada: GeneCompactado = GeneCompactado(str_original) #Compacta a string
    print(str_compactada)
    print(f"O gene compactado possui: {getsizeof(str_compactada)}")

    print(f"[+]Os genes sao identicos: {str_original == str_compactada.descompacta()}") #se a string original for igual a string descompactada, ela vai retornar um true, se não for um false





