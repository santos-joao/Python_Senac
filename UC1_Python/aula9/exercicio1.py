repetir = 0
while(repetir < 1):
 #primeira pergunta
 ponto = 0
 print("Python é uma linguagem de programação de alto nível, verdairo ou falso?")
 resposta = input().lower()
 
 if (resposta == "sim" or resposta == "s"):
    print("Você acertou!!!")
    ponto += 1
 else:
    print("Você errouuuu!!\nPython é uma linguagem de programação de alto nível interpretada de script imperativa orientada a objetos funcional de tipagem dinâmica e forte descreva e exemplifique com suas palavras o que significa afirmação Python é uma linguagem de tipagem dinâmica")
 
 #Segunda pergunta
 print("comando 'print' é uso para receber informação do usuário, verdairo ou falso?")
 resposta = input().lower()
 
 if (resposta == "sim" or resposta == "s"):
    print("Você Errou!!\n'print' comando para mostrar/ escrever algo na tela e input que atribuirar um valor ou informação.")
 else:
    print("Você certou!!")
    ponto += 1
 
 #Terceira pergunta
 print("comando 'int' é uso para receber informação número inteiros, verdairo ou falso?")
 resposta = input().lower()
 
 if (resposta == "sim" or resposta == "s"):
    print("Você acertou!!")
    ponto += 1
 else:
    print("Você errouu!!\n'int' para interiro e 'fload' para numeros com varivel.")
    

 #Ganhou?

 if(ponto >= 2):
    print(f"Você ganhou!! Vez total {ponto} pontos!!")
 else:
    print("Que pena você perdeu.")

 #Tentar novamente
 
 tentar = input("gostária de tentar novamente, sim ou não?").lower()
 if( tentar == "sim" or tentar == "s"):
    repetir = 0 
 else:
    repetir += 1