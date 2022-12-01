# Criação de funções

preco = 1999.90

# Calcular apenas 5% de imposto, guardar na variável imposto e imprimir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu.
#Isso é a declaração da função (como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

# Aqui é uso / aqui é imposto a calcular e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

# Explicação de variável local x variável global 
print(preco)
preco_produto = 100
print(preco_produto)
