nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
genero = input("Qual o seu gênero? digite F para feminino e M para masculino ")
dobro = idade * 2
print("Boa noite {} o dobro da sua idade é: {}".format(nome, dobro))
if idade >= 18 and genero == "M":
  print("Você é maior de idade, ótimo! Já pode dirigir ou beber!E deve prestar o serviço militar obrigatório! ")
else:
  print("Você é xóvem ainda, xóvem ainda...")
  