import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FOFOCAS DO BBB")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 20, 147)
GRAY = (200, 200, 200)

# Fonte
font = pygame.font.SysFont('Arial', 28, bold=True)
small_font = pygame.font.SysFont('Arial', 20)

# Botão
button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 100, 200, 50)

# Personagens
nomes = [
    "Bruno", "Camila", "João", "Larissa", "Mateus", "Juliana",
    "Pedro", "Vanessa", "Lucas", "Tatiane", "Rafael", "Bianca",
    "Henrique", "Patrícia", "Gustavo", "Fernanda", "Tiago", "Carol",
    "Daniel", "Isabela", "Marcos", "Aline", "Eduardo", "Natália"
]

# Mensagens
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
]

random.shuffle(mensagens_base)
mensagem_index = 0

def desenhar_tela(mensagem):
    screen.fill(PINK)
    wrapped_text = wrap_text(mensagem, font, WIDTH - 40)

    y_offset = 150
    for line in wrapped_text:
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (20, y_offset))
        y_offset += 40

    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = small_font.render("PRÓXIMA FOFOCA", True, BLACK)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 15))

    pygame.display.flip()

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

# Função para obter próxima mensagem
def get_next_message():
    global mensagem_index
    if mensagem_index >= len(mensagens_base):
        return None
    template, qtd_nomes = mensagens_base[mensagem_index]
    mensagem_index += 1
    personagens = random.sample(nomes, qtd_nomes)
    return template.format(*personagens)

mensagem_atual = get_next_message()
clock = pygame.time.Clock()
tempo_espera = 0
auto_avanco = 10 * 1000  # 10 segundos

# Loop principal
running = True
while running:
    dt = clock.tick(30)
    tempo_espera += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                mensagem_atual = get_next_message()
                tempo_espera = 0

    if tempo_espera >= auto_avanco:
        mensagem_atual = get_next_message()
        tempo_espera = 0

    if mensagem_atual:
        desenhar_tela(mensagem_atual)
    else:
        screen.fill(PINK)
        fim_text = font.render("Acabaram as fofocas por hoje! 👀", True, WHITE)
        screen.blit(fim_text, (WIDTH//2 - fim_text.get_width()//2, HEIGHT//2))
        pygame.display.flip()

pygame.quit()
sys.exit()
