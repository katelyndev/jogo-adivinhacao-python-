import random

print("🎮 Bem-vindo ao jogo da Adivinhação!")
numero_secreto = random.randint(1, 10) 
tentativas = 0 
acertou = False

while not acertou:
    palpite = int(input('Digite um número entre 1 e 10: '))
    tentativas += 1 

    if palpite == numero_secreto:
        print(f" 🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
        acertou = True
    elif palpite < numero_secreto :
        print("o número secreto é maior.")
    else:
        print("o número secreto é menor")
