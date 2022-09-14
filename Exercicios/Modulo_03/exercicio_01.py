# Neste exercício você deve criar um programa que abra o arquivo "alunos.csv" 
# e imprima o conteúdo do arquivo linha a linha.
import csv

def main():

    with open('alunos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)

        next(arquivo) # Pula a primeira linha

        for linha in leitor:
            print(linha)
            
main()