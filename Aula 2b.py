#Pede o nome do aluno e a sua nota de 0 a 10 e se ele tiver tirado 10 mostrar "você é bichão mesmo..."
nome = input ("Informe o seu nome: ")
nota = float(input("Digite a sua nota: "))
if (nota == 10):
  print("Parabéns {} Você é bichão mesmo, a sua nota foi: {}".format(nome, nota))
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho a sua nota foi: {nota}")

else:
  print(f"Burro, não tirou dez, a sua nota foi {nota}")
