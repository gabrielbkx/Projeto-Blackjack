from random import randint
#Lista cartas com um dicionario que gera as "cartas" para o Dealer e o jogador
cartas = [{
    "cartasDealer":[randint(1,10),randint(1,10)],
    "cartasJogador":[randint(1,10),randint(1,10)]
}]

#Soma das cartas do Dealer e do Jogador
somaDealer = cartas[0]["cartasDealer"][0] + cartas[0]["cartasDealer"][1]
somaJogador = cartas[0]["cartasJogador"][0] + cartas[0]["cartasJogador"][1]
#Pergunta ao Jogador se ele quer jogar e manipula a string para lowercase
perguntaInicial = input("Você quer jogar o Blackjack? 'S'/'N'\n").lower()
#Printa as duas primeiras cartas selecionadas pelo modulo randint
print(f"Suas cartas: {cartas[0]["cartasJogador"]},Seu score é : {somaJogador}")
#Printa a primeira cartas do "dealer" usando tambem o modulo randint
print(f"Primeira carta do computador: {cartas[0]["cartasDealer"][0]}")
#Pergunta ao jogador se ele quer passar ou obter uma nova carta
escolhaDoJogador = input("Aperte 'S' para obter uma nova carta ou 'N' para passar\n ").lower()

if escolhaDoJogador == "s":
    cartas[0]["cartasJogador"].append(randint(1,10))
    somaJogador = somaJogador + cartas[0]["cartasJogador"][2]
    print(f"Suas cartas: {cartas[0]["cartasJogador"]}, Seus pontos são: {somaJogador}")
    print(f"Cartas finais do computador: {cartas[0]["cartasDealer"]}, Pontos so computador: {somaDealer}")
    if somaDealer > somaJogador:
        print("Você Perdeu!")
    elif somaDealer < somaJogador:
        print("Você ganhou!")
elif escolhaDoJogador == "n":
    if somaDealer <= 16:
        cartas[0]["cartasDealer"].append(randint(1,10))
        if (somaJogador > somaDealer) and somaJogador < 21:
            print(f"Sua mão final: {somaJogador}")
            print(f"Mão final do computador: {somaDealer}")
            print("Você ganhou!")
        elif (somaDealer > somaJogador) and (somaDealer < 21):
            print(f"Sua mão final: {somaJogador}")
            print(f"Mão final do computador: {somaDealer}")
            print("Você perdeu!")
        elif somaDealer == somaJogador:
            print(f"Sua mão final: {somaJogador}")
            print(f"Mão final do computador: {somaDealer}")
            print("Empate!")
        elif somaJogador > 21:
            print(f"Sua mão final: {somaJogador}")
            print(f"Mão final do computador: {somaDealer}")
            print("Você perdeu!")
        else:
            print(f"Sua mão final: {somaJogador}")
            print(f"Mão final do computador: {somaDealer}")
            print("Você ganhou!")