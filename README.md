# **Desafios Python**

#### Essa é uma lista de desafios para praticar usando Python que eu vou atualizar a cada desafio que eu fizer. Eu planejo colocar exercícios tanto de nível *intermediário* quanto *avançado* no *futuro*, no momento não tenho esse conhecimento, mas espero que possa ajudar outras pessoas que estão sem ideias de mini-projetos.
---
## **Iniciante**
[01 - Pedra, Papel e Tesoura](#pedra-papel-tesoura)         
[02 - Cadastrar Pacientes](#cadastrar-pacientes)                    
[03 - Coin Flip Streak](#coin-flip-streak)              
[04 - Inventário](#inventário)              
[05 - Inventário 2](#inventário-2)              
[06 - Picture Grid](#picture-grid)          
[07 - Zig Zag](#zig-zag)       
[08 - Validador de CPF](#validar-CPF)           
[10 - Validador de CPF 2](#validar-CPF-2)    
[09 - Jogo da Forca](#jogo-da-forca)


---

## **Pedra Papel Tesoura**                    
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/papel_tesoura.py)  
> Esse desafio consiste em recriar o jogo Pedra, Papel e Tesoura onde o usuário irá escolher quantas partidas irá jogar, após isso ele deve escolher uma opção entre pedra, papel ou tesoura e a máquina também(óbvio que a escolha dela não será mostrada na tela). Assim que o usuário clicar na tecla *enter* será mostrada a mensagem de vitória, derrota ou empate. 
---
## **Cadastrar pacientes**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/106fb1a06f4de02c4f188efdfe7de9a88d59e43e/cadastro_pacientes.py)                       
> Nesse desafio você terá uma lista com alguns pacientes e o usuário irá digitar um nome - Não importa se for em *MAIÚSCULO* ou *minúsculo* -, e caso o nome não esteja na lista ele vai precisar reescrevê-lo. Com isso feito o nome será adicionado à lista e cada valor nela será mostrado entre vírgulas na tela. Se o nome já está na lista mostre uma mensagem de já cadastrado e em seguida todos os valores da lista entre vírgulas.

---                                                                        
## **Coin Flip Streak**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/coinflip.py)                                     
> Esse desafio - como muitos outros dessa lista - vem diretamente do livro *[Automate Boring Stuffs with Python](https://automatetheboringstuff.com/)*. Ele funciona assim: você terá um moeda que irá cair em cara ou coroa 100 vezes de maneira aleatória e isso vai se repetir por 10 mil vezes. Você precisa ver quantas *streaks¹* acontecem no total. Depois disso ver a chance de uma streak acontecer em porcentagem(%).
1. Streaks são uma sequência de algo, nesse desafio a sequência precisa ser cara ou coroa 6 vezes, ou seja, se acontecer da moeda "cair" em: cara, cara, cara, cara, cara, cara -> isso forma 1 streak

---

## **Inventário**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/fantasygame.py)  
> Você criará um inventário com um objeto *ou qualquer outra coisa* e a sua determinada quantidade, ou seja, um key-pair value que usamos nos dicionários. Após isso, usando sua lógica, seu código precisa aparecer na tela da seguinte maneira: 
```
 Inventário:
 25 moedas de bronze
 15 moedas de prata
 4 moedas de ouro
 1 corda 
 2 garrafas de água
 ``` 


---
## **Inventário 2**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/fantasygame2.0.py)
> Esse se parece bastante com o anterior - o output vai ser o mesmo -, a diferença é que agora serão criados um dicionário com os itens e suas quantidades e uma lista com itens que vão ser adicionados. Se o item a ser adicionado já estiver no seu dicionário a sua quantidade irá aumentar +1, porém, se o item não estiver no dicionário ele será adicionado com quantidade 1 - caso ele apareça para ser adicionado novamente será somado +1 em sua quantidade. Exemplo:
```python
Input
itemPrincipal = {'moeda de bronze' : 2, 'garrafa de água': 1}
itensParaAdicionar = ['moeda de bronze', 'metal', 'metal']

Output
3 moeda de bronze
1 garrafa de água
2 metal
```

---

## **Picture Grid**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/picturegrid.py)  
> Nós temos um grid(grade) de x linhas e y colunas. 
```Python
grid =[['o','o','o','.','.','o','o','o'],
       ['o','o','o','.','.','o','o','o'],
       ['o','o','o','.','.','o','o','o']]
```
> Nós precisamos criar um loop que passe por todas as elementos e os imprima dessa forma na tela:
```
ooo..ooo
ooo..ooo
ooo..ooo
```
>Dica: para passar em cada elemento de cada lista você pode usar um loop junto de `grid[a][b]`
---

## **Zig Zag**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/66070292898187eec0b0614f11bbdc1b538cc634/zigzag1.py)
> Nesse nós criaremos um zigzag, eu estava aprendendo a definir funções por isso criei como uma função, mas você que sabe. O intuito é criar um zigzag infinito e ele só será parado quando for interrompido manualmente (CTRL + C). Ele deve ser imprimido dessa forma na sua tela: 
```
........
  ........
    ........
      ........
        ........
      ........
    ........
  ........
........
  ........
```
---
## **Validar CPF**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/main/validar_cpf_regex.py)
> Esse validador é feito de uma maneira super simples com o uso de uma regular expression ou regex.
---

## **Validar CPF 2**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/main/validar_cpf.py)
> Esse é um validador um pouco melhor que o anterior e não é feito com o uso de regular expression. 

1. Ele faz a cópia dos 9 primeiros dígitos de um CPF qualquer colocando em uma outra variável. 
2. Faz a multiplicação do índice 0 até o 8 por 10, 9... até chegar no 2.  
  ```
  cpf = '18445895212'
  copia_cpf = '184458952'
  copia_cpf[0] * 10, copia_cpf[1] * 9, copia_cpf[2] * 8...
  ```
3. Cada produto, resultado da multiplicação, é somado a uma variável que irá guardar o total de *todas* multiplicações.
4. Com esse total vamos descobrir o penúltimo dígito do CPF usando a seguinte fórmula: `11 - (total % 11)`
5. Se a fórmula der um resultado maior que 9, será acrescentado um `0` como penúltimo valor.
6. Se o resultado for menor ou igual 9 a própria resposta será adicionado como penúltimo valor. 
``` py
# vamos imaginar a resposta sendo maior que 12
copia_cpf = '184458952'
fórmula = 11 - (total % 11) 
# agora o CPF será:
copia_cpf = '1844589520'

#agora com a resposta sendo 9
copia_cpf = '184458952'
fórmula = 11 - (total % 11) 
# agora o CPF será:
copia_cpf = '1844589529'

```
Agora todo esse passo a passo deve acontecer de novo para encontrar o último dígito do CPF, mas ao invés da multiplicação começar em 10 e terminar em 2, ela precisa começar em 11 e terminar em 2, por causa do índice a mais.  

---
## **Jogo da Forca**
[Link para o arquivo](https://github.com/Marcelo-4ever/Desafios/blob/main/jogo-da-forca.py)
> Um jogo da forca onde você escolhe o tema das palavras(profissões, animais ou aleatório) e pode errar até 6 vezes. Caso repita uma letra - certa ou errada - você não perderá uma chance, irá continuar com a mesma quantidade até errar uma letra que ainda não foi usada.






//sempre em desenvolvimento
