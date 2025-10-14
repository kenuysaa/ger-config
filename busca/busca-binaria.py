def busca_binaria(lista, valor):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Exemplo de uso
lista = [1, 3, 5, 7, 9]
valor = 5
resultado = busca_binaria(lista, valor)
if resultado != -1:
    print(f"Valor {valor} encontrado no índice {resultado}.")
else:
    print(f"Valor {valor} não encontrado na lista.")