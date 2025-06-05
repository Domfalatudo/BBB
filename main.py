import random
import time
import threading

    # ----------- COMEÇO DO BBB -----------

player = input("Quer jogar?? S ou N??\n").strip().lower()

if player != "s":
    print("Ok vaza então\n")
    exit()

print("Let's bora:\n")
print("Primeiro irei te explicar as regras do jogo:\n ")
print("Você precisa dar nome a 24 personagens. Quanto mais idiotas, melhor!\n")

    # ----------- NOMES PARA FACILITAR OS TESTES -----------
nomes = [
    "Bruno", "Camila", "João", "Larissa", "Mateus", "Juliana",
    "Pedro", "Vanessa", "Lucas", "Tatiane", "Rafael", "Bianca",
    "Henrique", "Patrícia", "Gustavo", "Fernanda", "Tiago", "Carol",
    "Daniel", "Isabela", "Marcos", "Aline", "Eduardo", "Natália"
]

    # ----------- COLETA DE NOMES -----------
#nomes = []
#for i in range(1, 25):
        #nome = input(f"{i}º personagem:\n")
       # nomes.append(nome)
    # ----------- COLETA DE NOMES -----------

print("\nTodos entram na casa do BBB...\n")



    # ----------- CÓDIGO PARA NÃO REPETIR OS NOMES -----------

for _ in range(5):  # ----------- EXIBE 5 MENSAGENS ALEATÓRIAS -----------
    selecionados = random.sample(nomes, 4)
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
        ("{0} fez juras de amor para {1}, mas à noite tava na piscina com {2} dizendo 'você que é meu crush real'.", 3)
]

    # ----------- MENSAGENS -----------

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

    





    
    