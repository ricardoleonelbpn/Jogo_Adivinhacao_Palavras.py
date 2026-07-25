# Tenha uma palavra secreta armazenada no programa.
# Solicite ao usuário um palpite.
# Continue fazendo o loop enquanto o palpite não estiver correto.
# Calcule o número de palpites e exiba-o no final.

import random

jogar_novamente = "sim"

print("\nSeja bem-vindo ao Jogo de adivinhação de palavras!")

print("\n------------------------------------- Dicas Importantes ------------------------------------------------------------")
print("Um sublinhado _ indica que a letra não estar presente na palavra secreta.")
print("Uma letra minúscula indica que a letra estar presente em algum lugar da palavra secreta, mas não naquela posição.")
print("Uma letra maiúscula indica que a letra estar presente naquele ponto exato da palavra secreta.")
print("-----------------------------------------------------------------------------------------------------------------------")

while jogar_novamente == "sim":

    palavras = ["vasoura", "lapis", "cadeira", "caderno", "celular", "carregador", "televisao", "carteira", "sofa", "fogão", "porta", "balde", "cama"]
    palavra_aleatoria = random.choice(palavras)
    palpite = ""
    contador = 0
    quantidade_letras = len(palavra_aleatoria)
    dica = "_ " * quantidade_letras
    
    print(f"\nA dica é {dica}")

    while palpite != palavra_aleatoria:

        palpite = input("\nQual é o seu palpite? ").lower()
        contador +=1

        if len(palpite) != len(palavra_aleatoria):
            print("\nDesculpe, o palpite precisa ter o mesmo número de letras que a palavra secreta.")
        elif palpite == palavra_aleatoria:
            break
        else:
        
            resultado = ""

            for index in range(len(palavra_aleatoria)):
                if palpite[index] == palavra_aleatoria[index]:
                    resultado += palpite[index].upper()
                elif palpite[index] in palavra_aleatoria:
                    resultado += palpite[index].lower()
                else:
                    resultado += "_"
            print(f"\nSua dica é {resultado}")
            
    print ("\nVocê adivinhou, parabéns! ",  end = "")
    print(f"Seus palpites foram {contador}")

    jogar_novamente = input("\nGostaria de jogar novamente, Sim/Não: ").lower()
print("Obrigado por Jogar!")