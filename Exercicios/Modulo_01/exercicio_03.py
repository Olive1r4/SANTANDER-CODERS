# Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, 
# a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?

# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos 
# são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando 
# outras investigações. Valores iguais ou abaixo de 1 são liberados.

def main():
    pontos = 0
    pergunta1 = input("Mora perto da vítima? (S/N): ").upper()
    while pergunta1 != 'S' and pergunta1 != 'N':
        pergunta1 = input("Mora perto da vítima? (S/N): ").upper()
    pontos += check_pergunta(pergunta1)

    pergunta2 = input("Já trabalhou com a vítima? (S/N): ").upper()
    while pergunta2 != 'S' and pergunta2 != 'N':
        pergunta2 = input("Já trabalhou com a vítima? (S/N): ").upper()
    pontos += check_pergunta(pergunta2)

    pergunta3 = input("Telefonou para a vítima? (S/N): ").upper()
    while pergunta3 != 'S' and pergunta3 != 'N':
        pergunta3 = input("Telefonou para a vítima? (S/N): ").upper()
    pontos += check_pergunta(pergunta3)

    pergunta4 = input("Esteve no local do crime? (S/N): ").upper()
    while pergunta4 != 'S' and pergunta4 != 'N':
        pergunta4 = input("Esteve no local do crime? (S/N): ").upper()
    pontos += check_pergunta(pergunta4)

    pergunta5 = input("Devia para a vítima? (S/N): ").upper()
    while pergunta5 != 'S' and pergunta5 != 'N':
        pergunta5 = input("Devia para a vítima? (S/N): ").upper()
    pontos += check_pergunta(pergunta5)

    sentence(pontos)

def check_pergunta(pergunta):
    if pergunta == "S":
        return 1
    elif pergunta == "N":
        return 0

def sentence(pontos):
    if pontos == 5:
        print("Assassino")
    elif pontos == 4 or pontos == 3:
        print("Cúmplice")
    elif pontos == 2:
        print("Suspeito")
    else:
        print("Liberado")

main()