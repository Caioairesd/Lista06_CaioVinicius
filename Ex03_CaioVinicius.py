"""03 - Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista.
Depois de inserir os três nomes, pergunte se deseja adicionar outro.
Se o fizer, permita que adicione mais nomes até responder "não".
Quando ele responder "não", mostre quantas pessoas ele convidou para a festa,
uma vez que o usuário tenha completado sua lista de nomes, exiba a lista completa e peça que ele digite um dos nomes da lista.
Exiba a posição desse nome na lista. Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa.
Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente."""

Lista = []
for i in range(3):
    convidados = input("Adicione um convidado: ").title()
    Lista.append(convidados)

confirm = input("Você deseja adiconar mais um convidado?\n(S/s para sim ou N/n para não): ").lower()

while confirm != "n":
    convidados = input("Adicione um convidado: ")
    Lista.append(convidados)
    confirm = input("Você deseja adiconar mais um convidado?\n(S/s para sim ou N/n para não): ").lower()
    

qtde = Lista.__len__()
print("Você convidou {} pessoas".format(qtde))

print(Lista)

convidados = input("Insira um dos convidados presentes na lista: ").title()
if convidados in Lista:
    i = Lista.index(convidados)
    print("A posição do convidado na lista é: {} ".format(i))
else:    
    print("{} não está presente na lista!".format(convidados))

confirm = input("Você ainda deseja que essa pessoa venha a festa?\n(S/s para sim ou N/n para não): ").lower
if confirm == "s":
    print("{} continua na lista de convidados!".format(convidados))
else:
    i = Lista.index(convidados)
    Lista.remove(convidados)
    print(Lista)



print("----------------------------------------------------")
print("Caio Vinicius Aires da Silva")
print("Fim do programa.")