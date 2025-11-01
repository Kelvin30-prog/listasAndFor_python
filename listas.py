# Criando uma lista de números
numeros = [99, 2, 1, 5, 9, 7]

# Acessando os numeros da lista
print(numeros)
print("O primeiro número da lista é:", numeros[0])
print("O segundo número da lista é:", numeros[1])
print("O último número da lista é:", numeros[-1])
print("O penultimo número da lista é:", numeros[-2])

# Modificando os itens da lista
print("")
numeros [0] = 3
numeros [4] = 6
numeros [-1] = 55
print("Lista após modificação:", numeros)

# Adicionando um item na lista
numeros.append(56)
print("")
print("Lista após a adição de um elemento:", numeros)

# Removendo um item da lista
# Quando não específicado o índice do ítem, ele remove o último
ultimo = numeros.pop()
print("")
print("Número removido:", ultimo)
print("Lista após a remoção do último elemento: ", numeros)

# Removendo um ítem especifico da lista
numeros.remove(1)
print("")
print("Lista após a remoção do ítem específico:", numeros)