from random import randint

quant_cpf = int(input('Criar quantos CPF\'s? '))
    
for k in range(quant_cpf):
    cpf = ''
    for i in range(9):
        escolher_numero = randint(0,9) 
        cpf += str(escolher_numero) #criar o 9 dígitos 
    reverso = 10
    total = 0

    for i in range(19): 
        if i >= 9: #se o i for >= 9 o index do novo_cpf[i] fica out of range, e é necessário deixar como 0,1,2,3..9 para o 2º loop 
            i -= 9

        total += int(cpf[i]) * reverso

        reverso -= 1 #reverso serve como o multiplicador 10,9,8,...2
        if reverso < 2:
            reverso = 11 # depois do 1º loop ele passa a valer 11,10,9...2
            formula = 11 - (total % 11) #formula para os 2 últimos dígitos do CPF
            
            if formula > 9: #se for 10 ou mais 
                cpf += "0" #acrescenta o 0 no novo_cpf
            
            else: #se for 9 ou menos acrescenta o próprio valor
                cpf += str(formula)
            total = 0 #o total é zerado para o 2º loop ocorrer sem problemas
    print(cpf)