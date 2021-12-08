import random
#lista de palavras para jogar
frutas = ['maça', 'banana', 'pera', 'kiwi', 'melância', 'limão', 'mamão', 'jabuticaba', 'laranja']
#setar palavra
palavra = random.choice(frutas)
#escondendo palavra
resposta = len(palavra)*'*'
#limitando tentativas
tentativas = 3

print('''Vamos jogar forca!
Dicas : Utilize a grafia correta na hora de advinhar! Acentos e "ç" contam!
O tema é frutas!''')

while tentativas > 0:
    letra = str(input(f'A palavra é {resposta}. Tente acertar uma letra : ').lower().strip())
    #garantindo que seja somente uma letra
    if len(letra) > 1:
        print('Não! Isso não pode! Tente advinhar somente uma letra por vez')
    else:
        #checar se existe a letra na palavra
        if letra in palavra:
            print('Aeee! Você acertou uma letra')
            #encontrando o indice da letra certa na palavra
            substitui = palavra.index(letra)
            #transformando a resposta exibida ao usuario em lista pra poder usar o indice
            aux = list(resposta)
            #substituindo a letra certa na palavra escondida exibida ao usuario
            aux[substitui] = letra
            #transformando em string
            resposta = "".join(aux)
            #sair do laço caso ganhe
            if resposta == palavra:
                break
        #tratando erro do usuario
        else:
            print('Ah! Você errou :(')
            tentativas -= 1
            #para não mostrar 'você ainda tem 0 tentativas'
            if tentativas != 0:
                print(f'Você ainda tem {tentativas} tentativas')

print(f'Você perdeu :(\nTente novamente' if tentativas == 0 else f'Você ganhou!\nA palavra era {palavra}')
