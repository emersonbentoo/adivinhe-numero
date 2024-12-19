import random 
print("Ola, eu sou um jogo de adivinhação\nJogo funciona assim:\nVou pensar em um numero de 0 a 10 e voce precisa adivinhar qual numero eu pensei! ")
while True:
    o = int(input("Digite:\n1 - Jogar\n2 - Sair\n" + '='*20+'\n'))
    if o == 1:
        pc = random.randint(0,10)
        jogador =int (input("Digite um valor de 0 a 10: "))
        if jogador >= 0 and jogador <=10 :
            if jogador != pc:
                print(f"Voce errou.\nEu pensei no numero {pc}")
            else:
                print(f"Eu e voce pensamos no numero {pc}.\nParabens voce ganhou\nDeseja continuar")
        else:
            print("Operação invalida!\nPor favor digite novamente")
    elif o ==2:
        print("Foi um prazer ter voce aqui!")
        break
    else:
        print("Erro: valor invalido\n.Por favor digite 1 ou 2")