import re 

while True: 
    cpf = str(input('Digite seu CPF: ')).strip()
    try:
        pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d') 
        find_pattern = pattern.search(cpf)
        a = find_pattern.group()  
        if find_pattern.group() and len(cpf) == 11:
            print('CPF válido!')
            break
        print('CPF muito grande!')
    except (AttributeError):
        pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d-\d\d')
        find_pattern = pattern.search(cpf)
        if find_pattern.group() and len(cpf) == 14:
            print('CPF válido também!')
            break
        print('Não válido!')

