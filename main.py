from random import choice
import os
from arte import logo

def limparTerminal():
    # Verifica o sistema operacional e executa o comando apropriado para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
def dealer():
    '''Retorna uma carta aleatória do baralho'''
    cartas = [11, 2, 3, 4, 8, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = choice(cartas)
    return carta

def calculaPontos(lista):
    """Pega uma lista de cartas e retorna uma pontuação da soma das cartas"""
    if sum(lista) == 21 and len(lista) == 2:
        return 0
    if 11 in lista and sum(lista) > 21:
        lista.remove(11)
        lista.append(1)
    return sum(lista)

def compararMaos(pontosUsuario, pontosPc):
    """Compara as cartas do jogador e do computador retornando o resultado"""
    if pontosUsuario == pontosPc:
        return "Empate!"
    elif pontosPc == 0:
        return "Derrota! oponente possui um Blackjack!"
    elif pontosUsuario == 0:
        return "Vitória! você possui um Blackjack!"
    elif pontosUsuario > 21:
        return "Derrota! Seus pontos ultrapassaram os 21"
    elif pontosPc > 21:
        return "Vitória! Os pontos do oponente ultrapassaram os 21"
    elif pontosUsuario > pontosPc:
        return "Vitória! Você possui mais pontos!"
    else:
        return (f"Derrota!")

def jogar():
    """Inicializa o jogo"""
    cartasComputador = []
    cartasjogador = []
    fimDeJogo = False

    print(logo)

    for _ in range(0, 2):
        cartasjogador.append(dealer())
        cartasComputador.append(dealer())

    while not fimDeJogo:
        pontosDoJogador = calculaPontos(cartasjogador)
        pontosDoComputador = calculaPontos(cartasComputador)

        print(f"Suas cartas: {cartasjogador}, Seus pontos: {pontosDoJogador}")
        print(f"Primeira carta do computador: {cartasComputador[0]}")

        if pontosDoJogador == 0 or pontosDoComputador == 0 or pontosDoJogador > 21:
            fimDeJogo = True
        else:
            escolhaDoUsuario = input(
                "Quer comprar outra carta? ()'s'/'n'): ").lower()
            if escolhaDoUsuario == "s":
                cartasjogador.append(dealer())
                print(cartasjogador)
            else:
                fimDeJogo = True

    while pontosDoComputador != 0 and pontosDoComputador < 17:
        cartasComputador.append(dealer())
        pontosDoComputador = calculaPontos(cartasComputador)

    print(f"Sua mão final: {
          cartasjogador}, Seus pontos finais: {pontosDoJogador}")
    print(f"mão final do computador: {
          cartasComputador}, Pontos finais do computador: {pontosDoComputador}")
    print(compararMaos(pontosDoJogador, pontosDoComputador))

while input("Quer jogar? ('s'/'n'): ") == "s":
    limparTerminal()
    jogar()
