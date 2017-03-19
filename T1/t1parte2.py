#1.Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " adicionada ao início de cada nome.

def srlambda (lista):
    return list(map (lambda c: 'Sr. ' + c,lista))

#2.Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista.

def formulalambda (lista):
    return list(map(lambda x: (3*x**2) + ((2/x)+1),lista))

#3.Crie uma função que receba uma lista de nomes e retorne outra lista com somente aqueles nomes que terminarem com a letra 'a'.

def retornanome (lista):
    return list(filter(lambda c: c[-1] == 'a',lista))

#4.Escreva uma função que, dada uma lista de idades de pessoas no ano atual, retorne uma lista somente com as idades de quem nasceu depois de 1970.
# Importando a bibliteca datetime seria possível obter o ano automaticamente

def testaidade (lista,ano_atual):
    return list(filter(lambda c: ano_atual - c >= 1970,lista))

#5.
