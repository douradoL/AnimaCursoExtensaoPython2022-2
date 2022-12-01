# comando input(): quero permitir que
# o usuário digite algo...
nome = input("Digite seu nome: ")
print(nome)
# Frase com o dado inserido
print(f"Boa noite {nome}")
'''
Idade não estava declarado como número por isso não dava para fazer operações:
idade = input("Digite a sua idade:")

E se eu quiser mostrar o dobro da idade?

Não funcionaria pois idade não era um inteiro, quando imprimia aparecia um número errado e não o dobro
'''
idade = int(input("Digite a sua idade: "))
print("A sua idade é: {}".format(idade))
dobro = idade * 2
print("O dobro da sua idade é: {}".format(dobro))
#Estrutura condicional - o famoso "SE" (if)
# Se a pessoa for maior se idade, mostre " Você é maior de idade, ótimo! Já pode beber ou dirigir "
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode dirigir ou beber!")
else:
  print("Você não pode dirigir, e nem beber!")
#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
  genero = input("Qual o seu gênero? digite F para feminino e M para masculino ")
  if idade >= 18 and genero == "M":
  print("Você é maior de idade, ótimo! Já pode dirigir ou beber!E deve prestar o serviço militar obrigatório! ")
else:
  print("Você é xóvem ainda, xóvem ainda...")
#Neste caso precisa satisfazer todas as condições do if
  