# Uma lista com nomes de pacientes, a pessoa deve digitar o nome dela, se ela não for um paciente ela vai poder se cadastrar

pacientes = [
    "JOSE FERREIRA",
    "AMANDA PEREIRA",
    "KAYLANE COSTA",
    "VERA SILVA",
    "FERNANDA AMORIM",
]
usuário = str(input("Nome: ")).strip().upper()  # nome do  paciente
cadastro = ' '
if usuário in pacientes:  # se o usuário estiver na lista
    print("Esse nome já foi cadastrado!")
elif usuário not in pacientes:  # se o usuário não estiver na lista
    cadastro = (
        str(input("Esse nome não está cadastrado. Para cadastrá-lo digite novamente: "))
        .strip()
        .upper()
    )
    sexo = (
        str(input("Sexo: [M/F] ")).strip().upper()[0]
    )  # perguntado o sexo pra responder senhor ou senhora
    if sexo in "M":
        print("Pronto! O senhor foi cadastrado!")
    elif sexo in "F":
        print("Pronto! A senhora foi cadastrada!")
    else:
        sexo = str(input("Sexo: [M/F] "))  # deve precisar fazer um loop pra funcionar
    pacientes += (cadastro,)  # acrescenta uma tupla(precisa da vírgula pro python entender) a outra tupla
for paciente in pacientes:
    if paciente == pacientes[-1]:
        print(paciente)
    else:
        pacientes[0] = (cadastro,)  # queria trocar de lugar o nome, mas não funcionou
        print(paciente, end=", ")
#