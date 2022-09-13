# Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.
# Exemplo:
# Janeiro - 31 
# Fevereiro - 28 
# Março - 31 
# Etc...

def main():
    meses = {
        'Janeiro': 31,
        'Fevereiro': 28,
        'Março': 31,
        'Abril': 30,
        'Maio': 31,
        'Junho': 30,
        'Julho': 31,
        'Agosto': 31,
        'Setembro': 30,
        'Outubro': 31,
        'Novembro': 30,
        'Dezembro': 31
    }
    
    for mes, dias in meses.items():
        print(f'{mes} - {dias}')
        
main()