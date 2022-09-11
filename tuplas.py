# Tuplas são imutáveis e não podem ser alteradas
# Aceitam qualquer tipo de dado
# São mais rápidas que listas
# São representadas por ()
# Aceita fatiamento e comando len()
# Tem o comando unpacking

tupla_paises = ('Brasil', 'Argentina', 'Chile', 'Uruguai', 'Paraguai')

# Imprime a lista
print(tupla_paises)

# verifica tamanho da tupla
print(len(tupla_paises))

# Imprime o item da posição 0
print(tupla_paises[0])

# Unpacking
pais1, pais2, pais3, pais4, pais5 = tupla_paises
print(pais1, pais2, pais3, pais4, pais5)
print(*tupla_paises)