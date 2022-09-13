# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

def main():

    itens = [1,2,3,4,5,6,7,8,9]
    pares = 0
    nPares = []

    for item in itens:
        if item % 2 == 0:
            pares += 1
            nPares.append(item)
    
    print(f'Foram encontrados {pares} números pares, são eles: {nPares}')
        
main()