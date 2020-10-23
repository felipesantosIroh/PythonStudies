# ! / Usr / bin / python
# -*- coding: UTF-8 -*-

"""
Felipe testando python
lembrando sintaxe
"""

#testando prints!
print("Hello World!")
a = 10
b = 3
print(a ** b) #potenciação
print(a % b) #resto da divisão

#condicionais
if a < b:
    print (a, " é menor que ", b)
elif a == b:
    print (a, " é igual a", b)
else:
    print (a, " é maior que ", b)

#laços de repetição
x = 0
while (x < 10): #imprimindo de 0 a 9
    print(x)
    x += 1

listInicial = ["Ana", "Tyroh", "Ultimo", "Jonathas", "Ivo"] #lista com nomes
for i in listInicial:
    print(i)

for i in range(10, 20, 2): #imprimindo com laço intercalando de 2 em 2
    print(i)


#Strings
frase = "O rato roeu a roupa do rei de Roma"
tamanho = len(frase)                            #len pega tamanho
print("o tamanho da frase é", tamanho)
print("culpa foi do ", frase[2:6])              #imprimindo intervalo
print(frase.lower())                            #frase imprimindo em minusculo
print(frase.upper())                            #frase imprimindo em maiusculo
print(frase.strip())                            #tira caractere especial no final da String
print(frase.split(" "))                         #quebra a frase tirando os espaços
print(frase.split("r"))                         #quebra a frase tirando os "R"
print(frase.find("rei"))                        #busca a substring e retorna a posição
                                                #caso não encontre ele retorna "-1"
print(frase.replace("rei", "jogador"))          #substitui uma substring por outra


#funções
def SOMA(x, y):                                 #função que soma dois numeros
    print("o resultado é :", x + y)
    return x+y


#arquivo
"""
    MODO  |      FUNÇÃO
    r     = somente leitura
    w     = escrita (caso o arquivo já exista, ele será apagado
                    e um novo arquivo será criado)
    a     = leitura e escrita (adiciona o novo conteudo no fim do arquivo)
    r+    = leitura e escrita
    w+    = escrita (o modo w+, assim como o w, apaga o conteudo
                    anterior do arquivo)
    a+    = abre o arquivo para atualização

"""

arquivo = open("arquivo.txt")

linhas =  arquivo.readlines()
print(linhas)
for linha in linhas:
    print(linha)

"""
    read = lê o arquivo inteiro
    readline = lê uma linha do arquivo
    readlines = lê o arquivo e armazena em uma lista
"""

"""

w = open("arquivo2.txt", "w")

w.write("Novo arquivo")

w.close()

"""