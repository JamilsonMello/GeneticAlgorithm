import random

tamanho_populacao = 10
tamanho_individuo = 3

montanha = [[10,30], [30,10], [30,38]]

def criar_individuo(min, max):
    return [random.randint(min, max) for i in range(tamanho_individuo)]

def criar_populacao():
    return [criar_individuo(0, 1) for i in range(tamanho_populacao)]

def fitness(valores):
    return [valores[0][i+ 1] + valores[0][i] for i in range(len(valores))]

populacao = criar_populacao()

print(populacao)
print(fitness(montanha))
 