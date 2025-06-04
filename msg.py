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
    terceiro = random.choice(nomes)
    quarto = random.choice(nomes)
    sorteado = random.choice(nomes)

    print("\nLet's Bora\n")
    print("Todos entram na casa do BBB:\n")

    mensagens = [
        f"\n{sorteado} já le tasca um beijão em {sorteado},\ne a câmera pega tudo ao vivo — plot twist que ninguém pediu!\n",
        f"\n{primeiro} falou que ama {segundo},\nmas {terceiro} é ex do {quarto} e já começa o clima de tensão no ar.\n",
        f"\n{primeiro} deu um 'corno, mas faz parte' pra {segundo} no meio da festa,\ne {quarto} começou a quebrar taça de vinho.\n",
        f"\n{segundo} jurando amor eterno,\nmas à noite já tava no edredom com {primeiro}. Eita!\n",
        f"\n{terceiro} e {quarto} tretando pesado por causa de um selinho em {primeiro},\na casa para pra assistir o barraco ao vivo.\n",
        f"\n{sorteado} subiu na mesa, tirou a blusa e gritou:\n'Isso aqui é libertação, não retiro nada!'\n",
        f"\n{primeiro} disse que só está no programa pela cachaça,\ne provou isso vomitando atrás da piscina.\n",
        f"\n{segundo} e {terceiro} passaram a madrugada no edredom,\no barulho foi tanto que os microfones quase explodiram.\n",
        f"\n{quarto} tentou bancar o zen, mas surtou quando viu {sorteado} dançando com {primeiro}.\n",
        f"\n{sorteado} inventou uma fofoca sobre {terceiro},\ne {segundo} passou a informação no sussurro como se fosse segredo de estado.\n",
        f"\nDurante a festa, {primeiro} dançou até o chão,\nmas caiu bêbado(a) e teve que ser carregado por {quarto}.\n",
        f"\n{terceiro} gritou:\n'Esse jogo é sobre lealdade!',\ne {segundo} respondeu:\n'Então por que você beijou o {primeiro} ontem?'\n",
        f"\n{sorteado} chorou, sorriu, beijou, brigou e ainda teve tempo pra fofocar com {quarto}.\n",
        f"\n{primeiro} disse que queria ir embora,\nmas depois da bebida começou a dar em cima de todo mundo, inclusive de {segundo}.\n",
        f"\n{quarto} puxou {terceiro} pelo braço e falou:\n'Vamos conversar no reservado'. A câmera foi junto, claro.\n",
        f"\n{sorteado} e {primeiro} fizeram aliança,\nmas no mesmo dia {primeiro} votou no {sorteado}.\n",
        f"\n{segundo} descobriu que {terceiro} falava mal dele pelas costas\ne jogou sabão em todo o espelho do quarto.\n",
        f"\nNa hora do ao vivo, {quarto} mandou shade para {primeiro} com um sorriso forçado:\n'Quem planta, colhe!'\n",
        f"\n{sorteado} disse que não ia beijar ninguém,\nmas no segundo drink já tava agarrando {segundo} na pista de dança.\n",
        f"\n{terceiro} derrubou a caixa de som na piscina,\ne a festa virou rave silenciosa com gente pelada pulando água.\n",
        f"\n{primeiro} se olhou no espelho e disse:\n'Eu nasci pra brilhar e ninguém vai apagar meu fogo'.\n",
        f"\n{quarto} fingiu que dormia,\nmas estava ouvindo a fofoca debaixo do edredom com o microfone aberto.\n",
        f"\n{segundo} fez discurso de paz,\nmas terminou gritando com {terceiro} na cozinha por causa de arroz queimado.\n",
        f"\n{sorteado} pediu desculpas por ter gritado,\nmas já estava xingando outro por não dividir o energético.\n",
        f"\n{primeiro} e {quarto} se trancaram no banheiro por 30 minutos.\nA edição colocou musiquinha e coraçãozinhos.\n",
        f"\nDurante o Jogo da Discórdia, {segundo} levantou e foi pra cima do {terceiro}:\n'Você é falso, manipulador e mentiroso!'\n",
        f"\n{terceiro} fez um funk sobre a casa e cantou no ao vivo:\n'Você finge que me ama, mas só quer imunidade!'\n",
        f"\n{quarto} tentou se fazer de santo,\nmas o VT mostrou ele combinando voto com {sorteado} na madrugada.\n",
        f"\nA produção teve que intervir porque {primeiro} colocou espuma de barbear no colchão do {segundo}.\n",
        f"\n{segundo} virou líder e já mandou {terceiro} pro paredão só por causa de um olhar atravessado.\n"
    ]

    for _ in range(5):  # Exibe 5 mensagens únicas
        mensagem = random.choice(mensagens)
        print(mensagem)
        mensagens.remove(mensagem)
