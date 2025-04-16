def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")
    print("\n")

def movimento_valido(tabuleiro, linha, coluna):
    return (0 <= linha < len(tabuleiro) and
            0 <= coluna < len(tabuleiro[0]) and
            tabuleiro[linha][coluna] == ' ')

def chegou_destino(linha, coluna):
    return linha == 3 and coluna == 3

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    if chegou_destino(linha_atual, coluna_atual):
        return (linha_atual, coluna_atual, profundidade)

    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # direita, esquerda, cima, baixo

    for dl, dc in direcoes:
        nova_linha = linha_atual + dl
        nova_coluna = coluna_atual + dc

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '*'
            _, _, profundidade_atual = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
            tabuleiro[nova_linha][nova_coluna] = ' '

            if profundidade_atual < melhor_profundidade:
                melhor_profundidade = profundidade_atual
                melhor_linha = nova_linha
                melhor_coluna = nova_coluna

    return melhor_linha, melhor_coluna, melhor_profundidade

def main():
    tabuleiro = [
        [' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['*', 'X', 'X', ' ', 'X']
    ]

    linha_atual, coluna_atual = 3, 0
    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha_atual, coluna_atual):
        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

        if profundidade == float('inf'):
            print("Caminho não encontrado.")
            return

        linha_atual, coluna_atual = nova_linha, nova_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'
        mostrar_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()
