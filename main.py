import random
import time
import threading
import matplotlib.pyplot as plt


    # ----------- COMEÇO DO BBB -----------

player = input("Quer jogar?? S ou N??\n").strip().lower()

if player != "s":
    print("Ok vaza então\n")
    exit()

print("Let's bora:\n")
print("Primeiro irei te explicar as regras do jogo:\n ")
print("Você precisa dar nome a 24 personagens. Quanto mais idiotas, melhor!\n")

     #----------- NOMES PARA FACILITAR OS TESTES -----------
nomes = [
    "Bruno", "Camila", "João"
]

lider = None
imune = None
perde_voto = None

round_number = 1

    # ----------- COLETA DE NOMES -----------
#nomes = []
#for i in range(1, 25):
        #nome = input(f"{i}º personagem:\n")
        #nomes.append(nome)

#print("\nTodos entram na casa do BBB...\n")

    # ----------- CÓDIGO PARA NÃO REPETIR OS NOMES -----------

for _ in range(5):  # ----------- EXIBE 5 MENSAGENS ALEATÓRIAS -----------
    selecionados = random.sample(nomes, min(4, len(nomes)))
    selecionados += [None] * (4 - len(selecionados))
    primeiro, segundo, terceiro, quarto = selecionados
    restante = [nome for nome in nomes if nome not in selecionados]
    sorteado = random.choice(restante) if restante else random.choice(nomes)

    # ----------- MENSAGENS -----------

    mensagens_base = [
        ("{0} já le tasca um beijão em {1}, a câmera pega e todo o público fica sabendo — plot twist que ninguém pediu.", 2),
        ("{0} falou que ama {1}, mas {1} era transgênero e {0} cai em depressão profunda, porque assim é o BBB: drama nonstop.", 2),
        ("{0} deu um 'corno, mas faz parte' pra {1} no meio da festa, e {1} já começou a chamar todo mundo de falso.", 2),
        ("{0} jurando que tá apaixonado, mas a gente sabe que é só jogo e que {1} já tá no próximo rolê.", 2),
        ("{0} e {1} tretando por causa de um crush, enquanto {2} só quer paz, amor e cerveja.", 3),
        ("{0} soltou a real: 'No BBB, amor é combustível, mas fofoca é gasolina na fogueira'.", 1),
        ("{0} disse que vai sair da casa com a cabeça erguida, mas a câmera já sabe que é mentira e que a treta vai até o final.", 1),
        ("{0} mandou aquele shade digno, e {1} respondeu com um 'só lamento, miga'.", 2),
        ("{0} tentou bancar o amigo, mas na real já tá planejando a revanche no próximo paredão.", 1),
        ("{0} chegou causando confusão e deixando a casa inteira com um 'quem vê, não crê'.", 1),
        ("{0} e {1} sumiram do quarto por horas, quando voltaram, {2} já tava surtando com ciúmes.", 3),
        ("{0} pegou {1} no flagra com {2} embaixo do edredom. Disfarçaram? Nem tentaram. A treta foi servida ao vivo.", 3),
        ("{0} tentou um clima com {1}, mas levou um 'você é só meu contatinho de paredão'. A vergonha foi nacional.", 2),
        ("{0} tentou fazer as pazes com {1}, mas levou um banho de bebida na cara no meio da festa.", 2),
        ("{0} foi falar mal de {1} no quarto, mas o microfone tava ligado direto na sala. Gafe histórica.", 2),
        ("{0} pegou {1} fumando escondido no banheiro, mas acabou dando uns tragos também, porque limites aqui não existem.", 2),
        ("{0} e {1} foram pegos transando no confessionário, enquanto {2} tava na sala falando que nunca faria isso ao vivo.", 3),
        ("{0} meteu o louco: beijou {1}, pegou {2} na mesma festa e ainda terminou a noite chorando na sauna.", 3),
        ("{0} e {1} tretaram feio: gritaria, dedo na cara e muita baixaria até segurança intervir.", 2),
        ("{0} abriu a geladeira de madrugada, achou bebida e chamou {1} pra virar tudo na jacuzzi. Resultado? Só acordaram ao meio-dia, pelados.", 2),
        ("{0} e {1} deram um amasso tão forte no sofá que derrubaram o vaso e quebraram a mesa. Clássico BBB.", 2),
        ("{0} puxou {1} pro edredom, mas {1} já tava tão doidão que dormiu no meio da pegação.", 2),
        ("{0} começou a flertar com {1}, mas {2} viu e já tacou bebida na cara, berrando: 'respeita minha história!'", 3),
        ("{0} foi pego pelado na cozinha fazendo miojo às 4 da manhã, enquanto {1} e {2} fumavam no sofá e riam da cena.", 3),
        ("{0} surtou de ciúmes quando viu {1} dando uns pegas em {2} na festa, tacou copo no chão e gritou: 'traidor!'", 3),
        ("{0} e {1} se pegaram tão forte na festa que até a produção ficou sem saber se cortava ou deixava rolar.", 2),
        ("{0} se declarou pra {1} depois de virar cinco shots, mas tropeçou e caiu no colo de {2}. Romance e vergonha misturados.", 3),
        ("{0} tava tão bêbado que começou a dançar pelado na área externa, enquanto {1} filmava tudo e {2} só ria: 'isso vai pro VT!'", 3),
        ("{0} saiu no tapa com {1} depois de descobrir que {1} tava pegando {2} escondido. O barraco parou a casa toda.", 3),
        ("{0} e {1} juraram que era só amizade, mas ontem foram vistos transando na despensa. Falso moralismo? Sempre.", 2),
        ("{0} e {1} fumaram tanta maconha na área externa que ficaram rindo sozinhos por duas horas, enquanto {2} surtava com o caos.", 3),
        ("{0} tentou fazer a fina, mas depois do quinto drink já tava rebolando até o chão com {1} e passando vergonha nacional.", 2),
        ("{0} ficou puto ao ver {1} lambendo o pescoço de {2} na festa. Partiu pra agressão e foi chamado no confessionário.", 3),
        ("{0} acordou de ressaca e jurou que nunca mais ia beber… até a próxima festa com {1}, claro.", 2),
        ("{0} perdeu a linha: subiu na mesa da cozinha pelado e começou a gritar que {1} era o amor da vida dele, enquanto {2} vomitava no canto.", 3),
        ("{0} se escondeu no armário pra ouvir a fofoca de {1}, mas espirrou bem na hora e foi pego no flagra, causando uma gritaria generalizada.", 2),
        ("{0} se declarou pra {1} ao vivo, mas acabou levando um fora histórico: 'Você é só mais um contatinho de festa, relaxa!'", 2),
        ("{0} ficou tão louco de cachaça que tentou beijar o dummy achando que era {1}. O Brasil inteiro riu com vergonha alheia.", 2),
        ("{0} e {1} inventaram de fazer strip-tease na varanda, mas escorregaram e caíram juntos na piscina. Cenas lamentáveis.", 2),
        ("{0} tacou fogo no parquinho: pegou a garrafa de vodka e saiu oferecendo shot pra geral, até que {1} desmaiou no sofá.", 2),
        ("{0} foi tentar fazer uma DR séria com {1}, mas tava tão chapado que esqueceu o assunto no meio da frase.", 2),
        ("{0} tentou se esconder de {1} depois da treta, mas tropeçou, caiu no chão e ainda levou uma zoada: 'Foge não, covarde!'", 2),
        ("{0} não aguentou a pressão: surtou na academia, chutou os aparelhos e ainda gritou que ia meter o soco no próximo que olhasse torto.", 1),
        ("{0} jurou que não pegava mais ninguém, mas cinco minutos depois já tava de língua com {1} na despensa, enquanto {2} filmava tudo.", 3),
        ("{0} invadiu o quarto gritando que {1} era falso, acordou geral e ainda ameaçou jogar as roupas de todo mundo na piscina.", 2),
        ("{0} e {1} se esconderam na casinha do jardim pra dar uns amassos, mas foram flagrados por {2}, que soltou: 'Só assim pra aparecer no VT!'", 3),
        ("{0} tentou provocar {1} na festa, mas levou um tapão na cara e ficou todo mundo gritando: 'É barraco!'", 2),
        ("{0} falou que não se mete em briga, mas ontem puxou {1} pelos cabelos na área externa e só parou quando {2} separou.", 3),
        ("{0} resolveu dar uma de romântico e levou café na cama pra {1}, mas acabou derrubando tudo e queimando a perna dela. Clima arruinado.", 2),
        ("{0} foi pro paredão e, ao invés de discurso, mandou um 'foda-se vocês', virou um shot e saiu pelado correndo pela casa.", 1),
        ("{0} tentou fazer charme pra {1}, mas errou o degrau e caiu de cara na escada. A galera não perdoou e virou meme na hora.", 2),
        ("{0} ficou tão louco na festa que começou a fazer pole dance no mastro da varanda, enquanto {1} e {2} só filmavam rindo.", 3),
        ("{0} disse que era o mais sensato da casa, mas ontem foi visto pelado, fumando um baseado e dando em cima de {1} e {2} ao mesmo tempo.", 3),
        ("{0} prometeu que não ia mais tretar, mas bastou {1} olhar torto que já tava partindo pra cima e quebrando o copo na parede.", 2),
        ("{0} fez juras de amor para {1}, mas à noite tava na piscina com {2} dizendo 'você que é meu crush real'.", 3),
        ("{0} deu PT na festa, vomitou na piscina e ainda tentou beijar {1}, que fugiu rindo: 'sóbrio, nunca!'", 2),

]


    # ----------- FUNCIONAMENTO DA LISTA DE MENSAGENS -----------

    random.shuffle(mensagens_base)
mensagem_index = 0

def esperar_input(flag):
    input("[Aperte Enter para a próxima ou espere...]\n")
    flag.append(True)

for _ in range(5):
    if mensagem_index >= len(mensagens_base):
        print("Acabaram as fofocas por hoje. 👀")
        break

    template, qtd_nomes = mensagens_base[mensagem_index]
    mensagem_index += 1

    # Pega somente a quantidade necessária de nomes, sem repetição
    personagens = random.sample(nomes, qtd_nomes)

    # Formata a mensagem com os nomes certos
    mensagem = template.format(*personagens)

    print(mensagem)

    # Delay com possibilidade de pulo
    delay_flag = []
    thread = threading.Thread(target=esperar_input, args=(delay_flag,))
    thread.start()

    base_delay = 20
    extra_delay = max(0, len(mensagem) - 200) // 20
    total_delay = base_delay + extra_delay

    for _ in range(total_delay):
        if delay_flag:
            break
        time.sleep(1)

    print()

        # ----------- FUNCIONAMENTO DA LISTA DE MENSAGENS -----------

# ----------- PROVAS E EVENTOS ANTES DO PAREDÃO -----------

print("\n🏆 Agora, começam as provas! 🏆\n")

print("\n🏆 PROVA DO LÍDER! 🏆\n")
input("Pressione Enter para saber quem ganhou...\n")
lider = random.choice(nomes)
print(f"👑 {lider} venceu a Prova do Líder e está imune!\n")

input("Pressione Enter para a próxima prova...\n")

print("\n😇 PROVA DO ANJO! 😇\n")
input("Pressione Enter para saber quem ganhou...\n")
anjo = random.choice([p for p in nomes if p != lider])
print(f"😇 {anjo} venceu a Prova do Anjo!\n")

input("Pressione Enter para saber quem o Anjo imunizou...\n")

# Lista de possíveis imunizados: todo mundo menos o Anjo
possiveis_imunizados = [p for p in nomes if p != anjo and p != lider]
imune = random.choice(possiveis_imunizados)

print(f"🛡️ {anjo} escolheu imunizar {imune}!\n")

input("Pressione Enter para a última prova...\n")

print("\n🚫 PROVA DA PERDA DE VOTO! 🚫\n")
input("Pressione Enter para saber quem perdeu o direito de votar...\n")
perde_voto = random.choice([p for p in nomes if p != lider and p != imune])
print(f"🚫 {perde_voto} perdeu o direito de votar nesta semana.\n")

input("Pressione Enter para seguir para o PAREDÃO...\n")
        
# ----------- PAREDÃO -----------

print("🚨🚨🚨 CHEGOU O MOMENTO DO PAREDÃO! 🚨🚨🚨\n")

# Participantes que podem ir para o paredão (exclui líder e imune)
participantes_para_paredao = [p for p in nomes if p != lider and (p != imune if imune else True)]

# Se houver menos de 3 participantes elegíveis para o paredão, elimina um aleatoriamente
if len(participantes_para_paredao) < 3:
    print("Não há participantes suficientes para formar um paredão de 3.")
    if len(nomes) > 1:  # Garante que ainda há mais de um na casa
        eliminado = random.choice(nomes)  # Escolhe alguém aleatoriamente da casa
        print(f"Para que o jogo continue, o Big Boss decidiu eliminar aleatoriamente: {eliminado.upper()}!")
        nomes.remove(eliminado)
        print(f"Restam {len(nomes)} participantes na casa.\n")
    round_number += 1
else:
    # Sorteia 3 para o paredão
    paredao = random.sample(participantes_para_paredao, 3)
    print(f"Emparedados da semana: {paredao[0]}, {paredao[1]} e {paredao[2]}!\n")

    # Inicializa votos
    votos = {participante: 0 for participante in paredao}

    # Quem pode votar: todos, menos os do paredão e quem perdeu o voto
    votantes = [p for p in nomes if p not in paredao and (p != perde_voto if perde_voto else True)]

    if not votantes:
        print("Não há votantes nesta rodada. O jogo continua sem eliminação nesta semana.")
        round_number += 1
    else:
        for _ in votantes:
            voto = random.choice(paredao)
            votos[voto] += 1

        # Mostra resultado da votação
        print("Resultado da votação:")
        for participante, num_votos in votos.items():
            print(f"{participante}: {num_votos} votos")
        
        # Elimina o mais votado
        eliminado = max(votos, key=votos.get)
        print(f"\nO eliminado da semana é: {eliminado.upper()}!")
        nomes.remove(eliminado)
        print(f"Restam {len(nomes)} participantes na casa.\n")

    round_number += 1

# ----------- RESULTADO DO PAREDÃO COM GRÁFICO -----------

print("RESULTADO DO PAREDÃO:\n")
participantes_para_paredao = [p for p in nomes if p != lider and (p != imune if imune else True)]

if len(participantes_para_paredao) >= 3:
    paredao = random.sample(participantes_para_paredao, 3)
else:
    paredao = participantes_para_paredao  # ou outro tratamento

votos = {participante: 0 for participante in paredao}
for participante, num_votos in votos.items():
    print(f"{participante}: {num_votos} votos")

# Aqui, se quiser mostrar algo, use outra variável ou lógica

# Gráfico
participantes = list(votos.keys())
quantidade_votos = list(votos.values())

plt.figure(figsize=(8, 6))
plt.bar(participantes, quantidade_votos, color=['red', 'blue', 'green'])

plt.title('Resultado do Paredão - BBB')
plt.xlabel('Participantes')
plt.ylabel('Número de Votos')

for i, v in enumerate(quantidade_votos):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.show()

# Determina eliminado
eliminado = max(votos, key=votos.get)

print(f"\n❌ O eliminado da semana é: {eliminado.upper()} com {votos[eliminado]} votos! ❌\n")

# Remove eliminado da lista
nomes.remove(eliminado)

 # ----------- FINAL DO JOGO -----------
if len(nomes) == 1:
        vencedor = nomes[0]
        print("\n--- FIM DE JOGO! ---")
        print("\n🎉🎉🎉 PARABÉNS! 🎉🎉🎉")
        print(f"O grande vencedor do BBB é: {vencedor.upper()}!")
        print("Ele(a) superou todas as fofocas, paredões e provas para se tornar o(a) campeão(ã)!")
        print("Obrigado por jogar o BBB do povão!")
else: # Isso só aconteceria se, por algum motivo, a lista ficasse vazia, o que não deve ocorrer com a lógica atual
        print("\n--- FIM DE JOGO ---")
        print("Todos os participantes foram eliminados. Ninguém venceu esta edição do BBB.")