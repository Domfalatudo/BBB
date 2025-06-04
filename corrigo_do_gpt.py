import random

player = input("Quer jogar?? S ou N??\n").lower()

if player != "s":
    print("Ok vaza então\n")
else:
    print("Let's bora:\n")
    print("Primeiro irei te explicar as regras do jogo:\n")
    print("Você precisa dar nome a 24 personagens. Quanto mais idiotas, melhor!\n")

    nomes = []
    for i in range(1, 25):
        nome = input(f"{i}º personagem:\n")
        nomes.append(nome)

    primeiro = random.choice(nomes)
    segundo = random.choice(nomes)
    terceiro = segundo
    quarto = primeiro

    sorteado = random.choice(nomes)

    print("\nLet's Bora\n")
    print("Todos entram na casa do BBB:\n")

    mensagens = [
        f"\n{sorteado} já le tasca um beijão em {sorteado},\na câmera pega e todo o público fica sabendo — plot twist que ninguém pediu.\n",
        f"\n{primeiro} falou que ama {segundo},\nmas {terceiro} era transgênero e {quarto} cai em depressão profunda,\nporque assim é o BBB: drama nonstop.\n",
        f"\n{primeiro} deu um 'corno, mas faz parte' pra {segundo} no meio da festa,\ne {quarto} já começou a chamar todo mundo de falso.\n",
        f"\n{segundo} jurando que tá apaixonado,\nmas a gente sabe que é só jogo e que {quarto} já tá no próximo rolê.\n",
        f"\n{terceiro} e {quarto} tretando por causa de um crush,\nenquanto {primeiro} só quer paz, amor e cerveja.\n",
        f"\n{sorteado} soltou a real:\n'No BBB, amor é combustível, mas fofoca é gasolina na fogueira'.\n",
        f"\n{primeiro} disse que vai sair da casa com a cabeça erguida,\nmas a câmera já sabe que é mentira e que a treta vai até o final.\n",
        f"\n{segundo} mandou aquele shade digno,\ne {terceiro} respondeu com um 'só lamento, miga'.\n",
        f"\n{quarto} tentou bancar o amigo,\nmas na real já tá planejando a revanche no próximo paredão.\n",
        f"\n{sorteado} chegou chegando, causando confusão\ne deixando a casa inteira com um 'quem vê, não crê'.\n",
    ]

    for _ in range(4):  # Exibir 4 mensagens únicas
        mensagem = random.choice(mensagens)
        print(mensagem)
        mensagens.remove(mensagem)
