#pop - remove o ultimo elemento de uma lista
#join concatena,inclui ou altera itens de uma lista
lista = ['2', '3', '4', '5']
lista2 = '='.join(lista)
print(lista2)

# #Indexação ex: começo - onde começa /  fim - onde o indice termina   
lista = [1,2,3,4,5]
lista2 = lista[:3] #Informações antes do 3
print(lista2)
lista3 = lista[3:] #Informações após o 3
print(lista3)
lista4 = lista[2:5] #Informações entre o 2 e 5
print (lista4)

## Aula 15 #Importações
          #math(funçoes matematicas)

# 1 - sqrt(x): Calcula a raiz quadrada de x.

# 2 -pow(x, y): Calcula x elevado à potência de y.

# 3 -log(x, base)**: Calcula o logaritmo de x na base especificada - (base padrão é e, número de Euler)

# 4 - exp(x): Calcula o valor de e (número de Euler) elevado à potência de x.

# 5 -sin(x), cos(x) e tan(x): Calcula os valores dos trigonometria seno, cosseno e tangente do ângulo em radianos

# 6 - pi: Retorna o valor de π (pi).

#random(numeros aleatorios), 
#os(sistema op), 
#datetime(datas e horas),
#json (manipular arquivo)

#Exemplos - import math  uma vez e pode-se usar em todo código
# import math

raiz_quadrada = math.sqrt(25)
print(raiz_quadrada)

potencia = math.pow(2,5)
print(potencia)

logaritmo = math.log(2,3)
print(logaritmo)                

exponencial = math.exp(2)
print(exponencial)     

angulo_radianos = math.radians(45)
print(angulo_radianos)

seno = math.sin(angulo_radianos)
print(seno)

cosseno = math.cos(angulo_radianos)
print(cosseno) 

tangente = math.tan(angulo_radianos)
print(tangente)




#Exercício 1: Calcule a raiz quadrada de um número inteiro inserido,pelo usuário usando o módulo math

import math
num = int(input('Digite um número para calculo da raiz quadrada: '))
raiz_quadrada = math.sqrt(num)
print(raiz_quadrada)


# Exercício 2:
# Calcule o valor absoluto de um número decimal inserido, pelo usuário usando o módulo math (Distância de um numero ate o 0)

num2 = float(input('Digite um numero: '))
absoluto = math.fabs(num2)
print(absoluto)

# Exercício 3:
# Arredonde um número decimal inserido pelo usuário para o inteiro mais próximo usando o módulo math

num3 = float(input('Digite um numero para arredondamento: '))
arredondar = math.ceil(num3)
print(arredondar)

# Exercício 4:
# Calcule o seno de um ângulo em graus inserido pelo usuário usando o módulo math.

angulo = int(input('Digite um numero para calculo do seno: '))
seno = math.sin(angulo)
print(seno)














