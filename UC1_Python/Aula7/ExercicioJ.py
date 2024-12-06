login = input("Você desejar acessar [E] para entrar [S] sair: ").lower()
x = 0
senha_correta = "654321"
if( login == "s"):
 while(x < 3):
     senha = input("Insira a senha:")
     if (senha_correta == senha):
         print(" Senha esta correta!")
         x += 5
     else:
         print(" senha errada, tente novamente.")
         x += 1

else:
 print("Obrigado")

if (x == 3):
   print("numero de tentativas chegou limiti, verifiquei seu e-mail")
else:
   print("Bem-Vindo")