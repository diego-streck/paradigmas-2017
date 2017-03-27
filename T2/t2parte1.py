#1

def addSuffix(x,y):
	return [i+x for i in y]

#teste: addSuffix("@inf.ufsm.br",["diego","ronaldo"])

#2
def countShorts(x):
	return len(list(filter(lambda x:x<5,[len(i) for i in x])))

#teste: countShorts(["diego,abc"])

#3 - 

vogais = 'aeiouAEIOU'

def stripVowels(x):
	return ''.join([x for x in x if x not in vogais])

#4
def hideChars(s):
	return ''.join([x if x in ' ' else '-' for x in s])


#5

def tabela(x):
	return list([(x,x*x) for x in (range(1,x+1))])

#6

def ultimo(y):
	return ''.join([x[0]+x[-1] for x in y])



