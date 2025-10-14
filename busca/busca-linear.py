def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

# Exemplo de uso
lista = [1, 3, 5, 7, 9]
valor = 5
resultado = busca_linear(lista, valor)
if resultado != -1:
    print(f"Valor {valor} encontrado no índice {resultado}.")
else:
    print(f"Valor {valor} não encontrado na lista.")