# hangman 
from random import choice

while True:
    tema = str(input('''Digite qual tema você quer jogar: 
    1 - aleatórias
    2 - profissão
    3 - animal
    -> '''))
    if not tema.isdigit(): #validar se é um número
        continue
    if int(tema) > 3 or int(tema) <= 0:
        continue
    if tema: # Se for um número e é menor que 3, o loop acaba
        break
    
        
aleatorio = ['axioma', 'azulejo', 'blitz', 'catarro', 'coçar', 'crespo', 'cripta', 'duplex', 'fúcsia', 'girar', 'gnóstico', 'haicai', 'hera', 'hífen', 'icterícia']
profissão = ['apicultor', 'agrônomo', 'auditor', 'bartender', 'cerimonialista', 'chef', 'coach', 'desembargador', 'despachante', 'endocrinologista', 'embaixador', 'intérprete', 'juiz']
animal = 'albatroz', 'alpaca', 'anchova', 'bacalhau', 'badejo', 'barracuda', 'beluga', 'cágado', 'chinchila', 'craca', 'dromedário', 'escaravelho', 'gerbo', 'gnu', 'gralha', 'hamster', 'lêmure', 'lhama', 'lince', 'marreco'
 
if tema: #cada valor é atribuído a uma lista
    if tema in '1':
        tema = aleatorio
    elif tema in '2':
        tema = profissão
    elif tema in '3':
        tema = animal
                
escolha = choice(tema) #tema já foi atribuído a uma lista aqui 
letras_digitadas = []
guardar_letras = []
chances = 6 #chances de errar

while True:
     
    user = str(input('Digite uma letra: '))
    if len(user) > 1: 
        print('Precisa ser apenas uma letra!')
        continue
    
    if user in guardar_letras: # guardar TODAS as letras para verificar se é repetida e não ter uma chance a menos
        print('Você já digitou essa letra!')
        continue
    
    guardar_letras.append(user)
    letras_digitadas.append(user) # apenas letras certas
    
    
    if user not in escolha: #se a letra não está na palavra secreta será eliminada da lista letras_digitadas e terá -1 chance
        print('Essa letra não existe na palavra secreta!\n')
        letras_digitadas.pop()
        chances -= 1        
        if chances == 0:
            print(f'Você não conseguiu! A palavra secreta era "{escolha}"')
            break
        
        
    palavra_temporaria = ''    
    for letra_secreta in escolha: # cada letra da palavra escolhida
        if letra_secreta in letras_digitadas: # se a letra estiver na letras_digitadas 
            palavra_temporaria += f'{letra_secreta} ' # a letra vai ser add a variável para formar uma palavra 
        else:
            palavra_temporaria += '_ ' # caso a letra não esteja na lista será add uma underline(igual o jogo da forca)
            
    print(f'{palavra_temporaria}\n') # mostrar a situação do usuário
    
    palavra_temporaria = palavra_temporaria.split() #palavra ficou com espaços e precisa ir pra uma lista p/ poder se juntar
    palavra_temporaria = ''.join(palavra_temporaria) #aqui o espaço é tirado
   
    if palavra_temporaria == escolha: # e finalmente ela pode ser comparada com a palavra original
        print('Acertou!')
        break
    
