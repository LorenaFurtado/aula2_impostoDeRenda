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

# calcula o imposto de renda:
def imposto_renda(salario,num_dependentes):
    if salario<=1000:
        faixa=0.01
    elif salario<=2000:
        faixa=0.03
    elif salario<=3000:
        faixa=0.05
    else:
        faixa=0.06                
    return salario_base(salario,num_dependentes)*faixa
print(imposto_renda(3000,2))   

#calcula o salario liquido
def salario_liquido(salario,num_dependentes):
    return salario-inss(salario)-imposto_renda(salario,num_dependentes)

 
print(salario_liquido(3000,2))  

print(salario_liquido(1000,2))   
print(salario_liquido(2000,2))  
