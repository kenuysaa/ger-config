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
if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50]
    valor = 30
    resultado = busca_binaria(lista, valor)
    if resultado != -1:
        print(f"Valor {valor} encontrado na posição {resultado}.")
    else:
        print(f"Valor {valor} não encontrado na lista.")