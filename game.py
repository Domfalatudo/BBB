import pygame
import random
import sys

# Inicializa Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BBB do Povão - Pygame")

# Cores
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
CIANO = (0, 255, 255)

# Fonte
FONT = pygame.font.SysFont("consolas", 22)
FONT_BIG = pygame.font.SysFont("consolas", 30, bold=True)

# Clock para controlar FPS
clock = pygame.time.Clock()

# Mensagens base (reduzidas para simplificar)
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

# Nomes para testes
nomes = ["Bruno", "Camila", "João", "Ana", "Pedro", "Lucas"]

# Estados do jogo
ESTADO_INICIO = 0
ESTADO_FOFOCAS = 1
ESTADO_PROVAS = 2
ESTADO_PAREDAO = 3
ESTADO_FIM = 4

estado = ESTADO_INICIO
mensagem_index = 0

# Variáveis do jogo
lider = None
anjo = None
imune = None
perde_voto = None
paredao = []
votos = {}

def draw_text(surface, text, pos, color=CIANO, font=FONT, max_width=760):
    """Desenha texto quebrando linhas se necessário"""
    words = text.split(' ')
    lines = []
    line = ''
    for word in words:
        test_line = line + word + ' '
        if font.size(test_line)[0] > max_width:
            lines.append(line)
            line = word + ' '
        else:
            line = test_line
    lines.append(line)

    y = pos[1]
    for l in lines:
        rendered = font.render(l.strip(), True, color)
        surface.blit(rendered, (pos[0], y))
        y += font.get_height() + 2

def wait_for_key():
    """Espera que o usuário aperte ENTER para continuar"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

def draw_bar_chart(surface, participantes, votos):
    total = max(votos.values()) if votos else 1
    bar_width = 150
    gap = 40
    x_start = (WIDTH - (bar_width * len(participantes) + gap * (len(participantes) -1))) // 2
    y_base = HEIGHT // 2 + 50

    cores = [CIANO, CINZA, (100, 100, 100)]  # Cores dentro da paleta

    for i, participante in enumerate(participantes):
        altura = int((votos[participante] / total) * 200) if total > 0 else 0
        x = x_start + i * (bar_width + gap)
        y = y_base - altura

        # Barra
        pygame.draw.rect(surface, cores[i % len(cores)], (x, y, bar_width, altura))
        # Nome
        nome_render = FONT.render(participante, True, CINZA)
        nome_rect = nome_render.get_rect(center=(x + bar_width // 2, y_base + 20))
        surface.blit(nome_render, nome_rect)
        # Votos
        votos_render = FONT.render(str(votos[participante]), True, CINZA)
        votos_rect = votos_render.get_rect(center=(x + bar_width // 2, y - 20))
        surface.blit(votos_render, votos_rect)

def main():
    global estado, mensagem_index, lider, anjo, imune, perde_voto, paredao, votos, nomes

    running = True

    while running:
        screen.fill(PRETO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if estado == ESTADO_INICIO:
            draw_text(screen, "Quer jogar? Pressione S para SIM ou N para NÃO", (20, HEIGHT//2 - 40), CIANO, FONT_BIG)
            pygame.display.flip()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                estado = ESTADO_FOFOCAS
                mensagem_index = 0
                pygame.time.wait(300)  # evita múltiplos inputs rápidos
            elif keys[pygame.K_n]:
                draw_text(screen, "Ok, vaza então!", (20, HEIGHT//2), CINZA, FONT_BIG)
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False

        elif estado == ESTADO_FOFOCAS:
            if mensagem_index < len(mensagens_base):
                template, qtd = mensagens_base[mensagem_index]
                personagens = random.sample(nomes, qtd)
                mensagem = template.format(*personagens)
                draw_text(screen, f"Fofoca #{mensagem_index +1}:", (20, 20), CINZA, FONT_BIG)
                draw_text(screen, mensagem, (20, 70), CIANO)

                draw_text(screen, "Pressione ENTER para a próxima fofoca ou ESC para pular", (20, HEIGHT - 40), CINZA)

                pygame.display.flip()

                # Espera input
                esperar = True
                while esperar:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_RETURN:
                                mensagem_index += 1
                                esperar = False
                            if ev.key == pygame.K_ESCAPE:
                                mensagem_index = len(mensagens_base)
                                esperar = False
            else:
                estado = ESTADO_PROVAS
                pygame.time.wait(300)

        elif estado == ESTADO_PROVAS:
            draw_text(screen, "🏆 Prova do Líder 🏆", (20, 20), CIANO, FONT_BIG)
            if lider is None:
                draw_text(screen, "Pressione ENTER para saber quem venceu", (20, 70), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        lider = random.choice(nomes)
            else:
                draw_text(screen, f"O Líder é: {lider}", (20, 70), CIANO)
                draw_text(screen, "Pressione ENTER para Prova do Anjo", (20, 110), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        estado = 2.1

        elif estado == 2.1:  # Prova do Anjo
            draw_text(screen, "😇 Prova do Anjo 😇", (20, 20), CIANO, FONT_BIG)
            if anjo is None:
                draw_text(screen, "Pressione ENTER para saber quem venceu", (20, 70), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        anjo = random.choice([p for p in nomes if p != lider])
            else:
                draw_text(screen, f"O Anjo é: {anjo}", (20, 70), CIANO)
                draw_text(screen, "Pressione ENTER para imunizar alguém", (20, 110), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        possiveis = [p for p in nomes if p != anjo and p != lider]
                        imune = random.choice(possiveis)
                        estado = 2.2

        elif estado == 2.2:  # Imunização
            draw_text(screen, f"O Anjo imunizou: {imune}", (20, 20), CIANO, FONT_BIG)
            draw_text(screen, "Pressione ENTER para Prova da Perda de Voto", (20, 70), CINZA)
            pygame.display.flip()
            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                    estado = 2.3

        elif estado == 2.3:  # Perda de voto
            draw_text(screen, "🚫 Prova da Perda de Voto 🚫", (20, 20), CIANO, FONT_BIG)
            if perde_voto is None:
                draw_text(screen, "Pressione ENTER para saber quem perdeu o direito de votar", (20, 70), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        perde_voto = random.choice([p for p in nomes if p != lider and p != imune])
            else:
                draw_text(screen, f"{perde_voto} perdeu o direito de votar!", (20, 70), CIANO)
                draw_text(screen, "Pressione ENTER para o Paredão", (20, 110), CINZA)
                pygame.display.flip()
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        estado = ESTADO_PAREDAO

        elif estado == ESTADO_PAREDAO:
            participantes_para_paredao = [p for p in nomes if p != lider and p != imune]

            if len(participantes_para_paredao) < 3:
                draw_text(screen, "Não há participantes suficientes para formar paredão de 3.", (20, 20), CINZA, FONT_BIG)
                pygame.display.flip()
                pygame.time.wait(3000)
                estado = ESTADO_FIM
            else:
                if not paredao:
                    paredao = random.sample(participantes_para_paredao, 3)
                    votos = {p:0 for p in paredao}

                    # Quem pode votar
                    votantes = [p for p in nomes if p not in paredao and p != perde_voto]

                    for _ in votantes:
                        voto = random.choice(paredao)
                        votos[voto] += 1

                draw_text(screen, "🚨 PAREDÃO 🚨", (20, 20), CIANO, FONT_BIG)
                draw_text(screen, "Emparedados da semana:", (20, 60), CINZA)
                draw_text(screen, f"{paredao[0]}, {paredao[1]} e {paredao[2]}", (20, 90), CIANO)

                draw_text(screen, "Resultado da votação:", (20, 130), CINZA)
                y = 160
                for participante, v in votos.items():
                    draw_text(screen, f"{participante}: {v} votos", (20, y), CINZA)
                    y += 30

                draw_text(screen, "Pressione ENTER para eliminar o participante com mais votos", (20, HEIGHT - 40), CINZA)

                draw_bar_chart(screen, paredao, votos)
                pygame.display.flip()

                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_RETURN:
                            eliminado = max(votos, key=votos.get)
                            nomes.remove(eliminado)
                            draw_text(screen, f"{eliminado} foi eliminado!", (20, HEIGHT//2), CIANO, FONT_BIG)
                            pygame.display.flip()
                            pygame.time.wait(2000)

                            # Reset para próxima rodada ou fim
                            paredao = []
                            votos = {}
                            lider = None
                            anjo = None
                            imune = None
                            perde_voto = None

                            if len(nomes) == 1:
                                estado = ESTADO_FIM
                            else:
                                estado = ESTADO_FOFOCAS
                            break

        elif estado == ESTADO_FIM:
            vencedor = nomes[0] if len(nomes) == 1 else None
            if vencedor:
                draw_text(screen, "--- FIM DE JOGO ---", (20, 50), CIANO, FONT_BIG)
                draw_text(screen, f"🎉 O vencedor é: {vencedor} 🎉", (20, 100), CIANO, FONT_BIG)
                draw_text(screen, "Obrigado por jogar o BBB do povão!", (20, 150), CINZA)
            else:
                draw_text(screen, "Todos foram eliminados. Ninguém venceu.", (20, HEIGHT//2), CINZA, FONT_BIG)

            draw_text(screen, "Pressione ESC para sair", (20, HEIGHT - 40), CINZA)
            pygame.display.flip()

            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
