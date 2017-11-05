possibilidade1 = 10
possibilidade2 = 30

print("\t\t\t\t\t\t MEGA SENA")
print("Bem vindo a MEGA SENA, o lugar onde pode-se ficar rico!")
dinheiro = int(input("Escolha seu capital inicial:"))
print("DICA: O número esta entre 7 e 13")
resposta1 = int (input("Digite o número:"))
ganho1 = resposta1 == possibilidade1
print(ganho1)
resposta1!=possibilidade1==print("ERROU! Perdeu todo o seu dinheiro, que era de",dinheiro,"reais,hahahahah, tente"
" dê novo e me de mais dimdim")
resposta1!=possibilidade1==exit()

dinheiro2 = dinheiro**3
dinheiro3 = dinheiro2*5

print("Parabens, você passou pela primeira fase. O seu dinheiro foi elevado por 3! Tome cuidado para não perder tudo!"
"Pois agora ele é de",(dinheiro2))
print("DICA: O número esta entre 10 e 73, é multiplo de 5, 3 e 2")
resposta2 = int(input("Digite o número:"))
ganho2 = resposta2 == possibilidade2
print(ganho2)
resposta2!=possibilidade2==print("ERROU! Perdeu todo o seu dinheiro, que era de",dinheiro2,"reais,hahahahah, tente"
" dê novo e me de mais dimdim")
resposta2!=possibilidade2==exit()
possibilidade3 = dinheiro3

print("Parabens, você passou pela segunda frase. O seu dinheiro foi multiplicado por 5! Tome cuidado para não perder "  
"tudo!Pois agora ele é de",dinheiro3)
print("DICA: O número esta entre 1 e infinito(pode ser qualquer número!) e este número ja foi elevado a três e "
      "multiplicado por cinco. Alem disso você conhece bem este número.")
resposta3 = int(input("Digite o número:"))
ganho3 = resposta3 == possibilidade3
print(ganho3)
resposta3!=possibilidade3==print("ERROU! Perdeu todo o seu dinheiro, que era de",dinheiro3,"reais,hahahahah, tente"
" dê novo e me de mais dimdim")
resposta3!=possibilidade3==exit()
desistindo = 1
continuando = 2
dinheiro4 = dinheiro3+10000000

print("Parabens! Você é bom nisto viu? Seu dinheiro foi multiplicado por 10! Isto aí meu, você ta ricão, quer desistir?")
desistir = int(input("Digite 1 para desistir ou 2 para continuar:"))
vacilaum = desistir == continuando
print(vacilaum)
desistir != continuando==print("Vacilão, vacilão, você desistiu então e vacilaum!")
desistir!=continuando==exit()
vencedor = desistir == continuando


print("Não desistiu? Parabens! Você terminou a Mega Sena. Como bônus, ganhará 10000000. Mas... Com o que irá gastar"
      " o seu dinheiro? Não sabe? Vou lher dar sugestões.")

print("OBS:Quando for comprar, aperte 1 para sim, 2 para não")

print("Temos três modelos de carros, vamos ver")
carrinho1 = int(input("Este fusquinha custa 500 reais, quer comprar?"))

fuscacom = 1
fuscanao = 2
dinheiro5 = dinheiro4-500

compra1 = carrinho1 == fuscacom
print(compra1)
morte = carrinho1 == fuscanao
carrinho1!=fuscacom==print("Não é assim que funciona, agora você deve morrer!")
carrinho1!=fuscacom==exit()

print("Você comprou fusquinha, seu dinheiro é de",dinheiro5,"reais. Vamos ver o próximo carro")

bmwcom = 1
bmwnao = 2
dinheiro6 = dinheiro5-50000
carrinho2 = int(input("Esta BMW custa 50000 reais, quer comprar?"))

compra2 = carrinho2 == bmwcom
print(compra2)
morte = carrinho2 == bmwnao
carrinho2!=bmwcom==print("Não é assim que funciona, agora você deve morrer!")
carrinho2!=bmwcom==exit()

print("Você comprou BMW, seu dinheiro é de",dinheiro6,"reais. Vamos ver o ultimo carro")

ferraricom = 1
ferrarinao = 2
dinheiro7 = dinheiro6-50000000
carrinho3 =  int(input("Esta Ferrari custa 50000000 reais, quer comprar?"))

compra = carrinho3 == ferraricom
print(compra)
morte = carrinho3 == ferrarinao
carrinho3!=ferraricom==print("Não é assim que funciona, agora você deve morrer!")
carrinho3!=ferraricom==exit()

print("Você comprou Ferrari, seu dinheiro é de",dinheiro7,"reais. Vamos ver a última coisa para comprar")

comprartalao = 1
naotalao = 2

talaodamega = int(input("Talão novo da Mega Sena, vai comprar? É de graça! Ou seja... Você não compra... GANHA!"))
final = talaodamega == comprartalao
print(final)


talaodamega!=comprartalao==print("Você nunca vai saber o verdadeiro final do jogo... A não ser se comece de novo!")
talaodamega!=comprartalao==exit()

print("\t\t\t\t\t\t\t\t\t MEGA SENA\n\n\n\t\t\t\tPARABENS, VOCÊ TERMINOU A MEGA SENA! FAÇA DE NOVO SE GOSTOU!")

#Selo Raphael - Qualidade e Sincronia
print("\n\n\nSelo Raphael - Qualidade e Sincronia, se você não gostou, é uma cutia de",25,"metros\nFeito, criado e organizado "
"pelo grande programador com vários cursos em premiadas e grandes universidades: Raphael Gimenenez Neto")