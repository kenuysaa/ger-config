def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


# Exemplo de uso
if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50]
    valor = 30
    resultado = busca_linear(lista, valor)
    if resultado != -1:
        print(f"Valor {valor} encontrado na posição {resultado}.")
    else:
        print(f"Valor {valor} não encontrado na lista.")
