"""01- Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida,
 exibir o número de índice (ou seja, posição na lista) desse item na tupla."""

paises = ('Brasil','Angola','japão','Alemanha','Georgia')

print(paises)

try:
    pais = str(input("Insira um dois países: ")).title()
    if pais in paises:
        i = paises.index(pais)
        print("A posição na lista é: {} ".format(i))
    else:
        print("{} não está presente na lista!".format(pais))
except:
    ("ERRO 404")

print("----------------------------------------------------")
print("Caio Vinicius Aires da Silva")
print("Fim do programa.")
