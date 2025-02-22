"""02 - Faça um programa que o usuario insira 10 produtos numa tupla.
Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele,
em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla."""

produtos = ('Bola','Caneta','Papel','Borracha','Estojo','Caderno','Livro','Regua','Mochila','Lancheira')

print(produtos)

produto = input("Insira um dois produtos: ").title()
if produto in produtos:
    i = produtos.index(produto)
    print("A posição na lista é: {} ".format(i))
else:    
    print("{} não está presente na lista!".format(produto))

posicao = int(input("Insira um número de 0 a 9: "))
scanner = produtos.__getitem__(posicao)


print("O {} está na lista na posição {}".format(scanner,i))