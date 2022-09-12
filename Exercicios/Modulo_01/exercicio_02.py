"""
    Faça um programa que leia a validade das informações:
    a. Idade: entre 0 e 150; 
    b. Salário: maior que 0; 
    c. Sexo: M, F ou Outro;
    O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""

def main():

    idade = check_idade(int(input("Digite a idade: ")))
    salario = check_salario(float(input("Digite o salário: ")))
    sexo = check_sexo(input("Digite o sexo: "))

    if idade == False:
        print("Idade inválida!")
    if salario == False:
        print("Salário inválido!")
    if sexo == False:
        print("Sexo inválido!") 

def check_idade(idade):
    if idade < 0 or idade > 150:
        return False
    return True

def check_salario(salario):
    if salario <= 0:
        return False
    return True

def check_sexo(sexo):
    if sexo == "M" or sexo == "F" or sexo == "Outro":
        return True
    return False

main()