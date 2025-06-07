import pygame
import sys
import random
import time

pygame.init()

# ------ CONFIGURAÇÕES DA TELA ------
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("BBB do Povão")

# ------ FONTES E CORES ------
fonte = pygame.font.SysFont("Arial", 28)
fonte_grande = pygame.font.SysFont("Arial", 40)
branco = (255, 255, 255)
preto = (0, 0, 0)

caixa_mensagem = []  # fila de mensagens pendentes

def desenhar_texto(texto, y, fonte=fonte, cor=branco):
    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        txt = fonte.render(linha, True, cor)
        rect = txt.get_rect(center=(LARGURA//2, y + i * 40))
        tela.blit(txt, rect)

def esperar_enter():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return

def exibir_mensagem(titulo, mensagem):
    caixa_mensagem.append((titulo, mensagem))

def processar_mensagens():
    while caixa_mensagem:
        titulo, mensagem = caixa_mensagem.pop(0)
        tela.fill(preto)
        desenhar_texto(titulo, 60, fonte_grande)
        linhas = mensagem.split("\n")
        y_inicial = 150
        for i, linha in enumerate(linhas):
            desenhar_texto(linha, y_inicial + i * 40)
        pygame.display.flip()
        esperar_enter()

# ------ PARTICIPANTES DE TESTE ------
nomes = ["Bruno", "Camila", "João"]

lider = None
imune = None
perde_voto = None
round_number = 1

# ------ MENSAGENS ALEATÓRIAS DE EVENTOS ------
eventos_aleatorios = [
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
    ("{0} deu PT na festa, vomitou na piscina e ainda tentou beijar {1}, que fugiu rindo: 'sóbrio, nunca!'", 2)
]

# ------ FUNÇÃO DE EVENTO ALEATÓRIO ------
def evento_aleatorio(participantes):
    evento = random.choice(eventos_aleatorios)
    frase, num_participantes = evento
    escolhidos = random.sample(participantes, min(num_participantes, len(participantes)))
    mensagem = frase.format(*escolhidos)
    exibir_mensagem("Evento Aleatório", mensagem)
    processar_mensagens()

# ------ PROSSEGUIMENTO DO JOGO ------
def prova_do_lider():
    global lider
    lider = random.choice(nomes)
    exibir_mensagem("Prova do Líder", f"{lider} venceu a Prova do Líder e está imune!")

def prova_do_anjo():
    global imune
    anjo = random.choice([p for p in nomes if p != lider])
    possiveis = [p for p in nomes if p != lider]
    if possiveis:
        imune = random.choice(possiveis)
        texto = f"{anjo} venceu a Prova do Anjo e escolheu imunizar {imune}!"
    else:
        imune = None
        texto = f"{anjo} venceu a Prova do Anjo, mas não havia ninguém para imunizar."
    exibir_mensagem("Prova do Anjo", texto)

def prova_perda_voto():
    global perde_voto
    possiveis = [p for p in nomes if p != lider and p != imune]
    if possiveis:
        perde_voto = random.choice(possiveis)
        texto = f"{perde_voto} perdeu o direito de votar nesta semana."
    else:
        perde_voto = None
        texto = "Ninguém perdeu o direito de votar."
    exibir_mensagem("Prova da Perda de Voto", texto)

def paredao():
    participantes_para_paredao = [p for p in nomes if p != lider and p != imune]
    if len(participantes_para_paredao) < 3:
        eliminado = random.choice(nomes)
        nomes.remove(eliminado)
        texto = f"Poucos participantes. Big Boss eliminou aleatoriamente: {eliminado}!"
        exibir_mensagem("Eliminação Aleatória", texto)
    else:
        paredao = random.sample(participantes_para_paredao, 3)
        votos = {p: 0 for p in paredao}
        votantes = [p for p in nomes if p not in paredao and p != perde_voto]
        for _ in votantes:
            voto = random.choice(paredao)
            votos[voto] += 1
        eliminado = max(votos, key=votos.get)
        nomes.remove(eliminado)
        texto = f"Emparedados: {', '.join(paredao)}\n"
        texto += "\nResultado da votação:\n"
        for p, v in votos.items():
            texto += f"{p}: {v} votos\n"
        texto += f"\nO eliminado é: {eliminado}!"
        exibir_mensagem("Paredão", texto)

def jogo():
    global round_number
    while len(nomes) > 1:
        exibir_mensagem(f"SEMANA {round_number}", "A semana começa na casa mais vigiada do Brasil!")
        processar_mensagens()
        evento_aleatorio(nomes)
        prova_do_lider()
        processar_mensagens()
        prova_do_anjo()
        processar_mensagens()
        prova_perda_voto()
        processar_mensagens()
        paredao()
        processar_mensagens()
        round_number += 1

    vencedor = nomes[0] if nomes else None
    if vencedor:
        exibir_mensagem("FIM DE JOGO", f"🎉 O grande vencedor é: {vencedor.upper()}! 🎉")
    else:
        exibir_mensagem("FIM DE JOGO", "Todos foram eliminados. Não houve vencedor.")
    processar_mensagens()

# ------ INÍCIO DO JOGO ------
tela.fill(preto)
desenhar_texto("Bem-vindo ao BBB do Povão!", 200, fonte_grande)
desenhar_texto("Pressione ENTER para começar...", 300)
pygame.display.flip()
esperar_enter()

jogo()

pygame.quit()
sys.exit()