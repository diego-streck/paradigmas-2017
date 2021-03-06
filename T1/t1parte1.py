#1.Defina uma função somaQuad(x,y) que calcule a soma dos quadrados de dois números x e y.

def somaquad(x,y):
    return pow(x,2)+pow(y,2)


#2.#Crie uma função hasEqHeads(l1,l2) que verifique se as listas l1 e l2 possuem o mesmo primeiro elemento.

def hasEqHeads(l1,l2):
    return l1[0] == l2[0]



#3.Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " adicionada ao início de cada nome.
#Defina uma função auxiliar para ajudar neste exercício.

def SrNome (lista):
    def addSr(x):
        return 'Sr. ' + x
    return list(map(addSr,lista))

#4.Crie uma função que receba uma string e retorne o número de espaços nela contidos.
#Defina uma função auxiliar para ajudar neste exercício.

def contaespaco (string):
    return string.count(' ')


#5.Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista. Defina uma função auxiliar para ajudar neste exercício.

def result(x):
    return((3*x**2)+((2/x)+1))

#testar: list(map(result,[1,2,3]))

#6.Escreva uma função que, dada uma lista de números, retorne uma lista com apenas os que forem negativos. Defina uma função auxiliar para ajudar neste exercício.

#solução melhor:

list(filter(lambda x: x<0, [1,2,3,-5,-6,-7])) 

#7.Escreva uma função que receba uma lista de números e retorne somente os que estiverem entre 1 e 100, inclusive. Defina uma função auxiliar para ajudar neste exercício.

list(filter(lambda x: x>0 and x<100,[1,2,99,100,-1]))

#8.Escreva uma função que receba uma lista de números e retorne somente aqueles que forem pares. Defina uma função auxiliar para ajudar neste exercício.

list(filter(lambda x: x%2==0,[1,2,3,8,4]))

#9.Crie uma função charFound(c,s) que verifique se o caracter c está contido na string. O resultado deve ser True ou False. Você não deve usar o operador in. 
#Defina uma função auxiliar para ajudar neste exercício.

def charFound(c,s):
    return s.find(c) > 0

#10.Escreva uma função que receba uma lista de strings e retorne uma nova lista com adição de marcações HTML (p.ex.: <B> e </B>) antes e depois de cada string.
def addmarca(lista,m1,m2):
    def addmarcas(x):
        return m1 + x + m2
    return list(map(addmarcas,lista))
    
