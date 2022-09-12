"""Faça um programa que peça um valor monetário e diminua-o em 15%. 
Seu programa deve imprimir a mensagem “O novo valor é [valor]”."""

def main():

    valor = calc_valor(float(input("Digite o valor: ")))
    print("O novo valor é: ", valor)

def calc_valor(valor):
    valor = valor - (valor * 0.15)
    return valor

main()
