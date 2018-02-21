# calcula o inss
def inss(salario):
    if salario<=1000:
        return 0.0
    elif salario<=2000:
        return salario * 0.1 
    else:
        return 0.2*salario
print (inss(3000))


# calcula o desconto total de acordo com o número de dependentes:
def desc_dependentes(num_dependentes):
    return 100*num_dependentes
print(desc_dependentes(2))

# calcula o salario base: salario bruto - desconto inss - desconto dependentes

def salario_base(salario,num_dependentes):
    return salario - inss(salario)-desc_dependentes(num_dependentes)
print(salario_base(3000,2))
    