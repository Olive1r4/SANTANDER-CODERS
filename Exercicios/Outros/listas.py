lista_paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai', 'Paraguai']

# Imprime a lista
print(lista_paises)

# Verifica se o item está na lista
print("Brasil" in lista_paises)

# Verifica se o item não está na lista
print("Espanha" not in lista_paises)

# Imprime o tamanho da lista
print(len(lista_paises))

# Imprime o item da posição 0
print(lista_paises[0])

# Incluindo um item na lista
lista_paises.append('Espanha')
print(lista_paises)

# Incluindo um item na lista em uma posição específica
lista_paises.insert(0, 'Portugal')
print(lista_paises)

# Invetendo a ordem da lista
lista_paises.reverse()
print(lista_paises)

# Removendo um item da lista
lista_paises.remove('Espanha')
print(lista_paises)

# Removendo um item da lista em uma posição específica
lista_paises.pop(0)
print(lista_paises)

# Imprimir o ultimo item da lista
print(lista_paises[-1])

# Imprimir o penultimo item da lista
print(lista_paises[-2])

# Imprimir parte da lista
print(lista_paises[1:3])
print(lista_paises[1:])
print(lista_paises[:3])