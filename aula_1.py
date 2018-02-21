""" caso eu queira que o python aceite acentos etc, basta declarar:
# -*- coding: utf-8 -*-
"""

"""
#funcao que define soma
def soma(a,b):
    return a+b

print (soma(12,100))

# versão onde o usuário define os parâmetros:

def area_coroa3(r1,r2,pi=3.14):
    return (pi*r1**2) - (pi*r2**2)

a1=input("digite r1:") 
a1 = float(a1) #necessário pois o python 3 não converte automaticamente pra número
a2=input("digite r2, menor do que r1:")
a2 = float(a2)
a3=input("digite o valor de pi com separador de decimal .:")
a3 = float(a3) 
ac=area_coroa3(a1,a2)

print (" a area da coroa e:", ac)

# funcao que calcula a area da coroa circular
def area_coroa(r1,r2,pi):
    return (pi*r1**2) - (pi*r2**2)
print (area_coroa(10,9,3.1416))

# versao melhorada
def area_circulo(r,pi):
    return(pi*r**2)
print(area_circulo(10,3.1416))
print(area_circulo(9,3.1416))

def area_coroa2(r1,r2,pi):
    return area_circulo(r1,pi) - area_circulo(r2,pi) 
print (area_coroa2(10,9,3.1416))
"""

# exemplo a ser executado:função para calcular o número de itens que é possível comprar com uma determinada quantia e o troco que deve ser dado"""
# pegando a parte inteira
def parteinteira(n):
    return int(n)
print (parteinteira(10.78))
## ok funciona! ele trunca ;)

def caixa_registradora(dinheiro,preco):
    num_bombons=int(dinheiro/preco) # pega a parte inteira"truncada" da divisão
    troco=dinheiro - (num_bombons * preco)
    return num_bombons, troco

preco=0.6
dinheiro=10
bombons,troco=caixa_registradora(dinheiro,preco)
print ("número de bombons é:", bombons)
# essa parte %.2f"%(troco) é para garantir que a resposta seja em casas decimais
print ("o troco é:%.2f"%(troco))
print(caixa_registradora(10,0.6))   






    