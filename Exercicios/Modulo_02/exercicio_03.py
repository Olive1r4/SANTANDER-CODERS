# Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve 
# retornar [1+3, 4+5, 3+1] = [4, 9, 4].

def main():
    list1 = [1, 4, 3]
    list2 = [3, 5, 1]

    print(soma_listas(list1, list2))

def soma_listas(list1, list2):
    soma = []
    for i in range(len(list1)):
        soma.append(list1[i] + list2[i])
    return soma
    
main()