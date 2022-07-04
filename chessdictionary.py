"""
A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can't be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.
"""

""" Se tiver peça repetida vai ser contado +1 na lista, porém, só vai acontecer isso mesmo e a mensagem que a peça não é válida. """ 
from time import sleep 

grafico_chess = [['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.']]
def validateMovement(keys):
    if (len(keys) == 2 and keys[0] in "abcdefgh"):  # must have only 2 digits and the first is in 'abcdefgh'
        if keys[1] in "12345678":
            print(f"{keys} is a valid movement",end=' ')
        else:
            print(f"{keys} is not a valid movement")
    else:
        print(f"{keys} is not a valid movement")


quantity_pieces = [0,0,0,0,0,0,0,0,0,0,0,0]
def piecesQuantity(values1):
    pieces_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    if values1 in 'bpawn': 
        grafico_chess[1][quantity_pieces[0]] = 'P'
        quantity_pieces[0] += 1
        if quantity_pieces[0] > 8:
            print('Chess has only 8 pawns')
    elif values1 in 'wpawn':
        grafico_chess[-2][quantity_pieces[1]] = 'P'
        quantity_pieces[1] += 1
        if quantity_pieces[1] > 8:
            print('Chess has only 8 wpawns')
    
    elif values1 in 'bknight':
        quantity_pieces[2] += 1
        if quantity_pieces[2] == 1:
            grafico_chess[0][1] = 'N'
        elif quantity_pieces[2] == 2:
            grafico_chess[0][-2] = 'N'
        if quantity_pieces[2] > 2:
            print('Chess has only 2 bkinghts')
    elif values1 in 'wknight': 
        quantity_pieces[3] += 1
        if quantity_pieces[3] == 1:
            grafico_chess[-1][1] = 'N'
        elif quantity_pieces[3] == 2:
            grafico_chess[-1][-2] = 'N'
        if quantity_pieces[3] > 2:
            print('Chess has only 2 wknights')  
    
    elif values1 in 'bbishop':
        quantity_pieces[4] += 1
        if quantity_pieces[4] == 1:
            grafico_chess[0][2] = 'B'
        elif quantity_pieces[4] == 2:
            grafico_chess[0][-3] = 'B'
        if quantity_pieces[4] > 2: 
            print('Chess has only 2 bbishops')
    elif values1 in 'wbishop':
        quantity_pieces[5] += 1
        if quantity_pieces[5] == 1:
            grafico_chess[-1][2] = 'B'
        elif quantity_pieces[5] == 2:
            grafico_chess[-1][-3] = 'B'
        if quantity_pieces[5] > 2:
            print('Chess has only 2 wbishops')
            
    elif values1 in 'brook':
        quantity_pieces[6] += 1
        if quantity_pieces[6] == 1:
            grafico_chess[0][0] = 'R'
        elif quantity_pieces[6] == 2:
            grafico_chess[0][-1] = 'R'
        if quantity_pieces[6] > 2:
            print('Chess has only 2 brook')
    elif values1 in 'wrook':
        quantity_pieces[7] += 1
        if quantity_pieces[7] == 1:
            grafico_chess[-1][0] = 'R'
        elif quantity_pieces[7] == 2:
            grafico_chess[-1][-1] = 'R'
        if quantity_pieces[7] > 2:
            print('Chess has only 2 wrooks') 
        
    elif values1 in 'bqueen':
        quantity_pieces[8] += 1
        if quantity_pieces[8] == 1:
            grafico_chess[0][4] = 'Q'
        if quantity_pieces[8] > 1:
            print('Chess has only 1 bqueen')
    elif values1 in 'wqueen':
        quantity_pieces[9] += 1
        if quantity_pieces[9] == 1:
            grafico_chess[-1][4] = 'Q'
        if quantity_pieces[9] > 1:
            print('Chess has only 1 wqueen')
            
    elif values1 in 'bking':
        quantity_pieces[10] += 1
        if quantity_pieces[10] == 1:
            grafico_chess[0][3] = 'K'
        if quantity_pieces[10] > 1:
            print('Chess has only 1 bking')
    elif values1 in 'wking':
        quantity_pieces[11] += 1
        if quantity_pieces[11] == 1:
            grafico_chess[-1][3] = 'K'
        if quantity_pieces[11] > 1:
            print('Chess has only 1 wking')

   

def validatePiece(values): #validate if is a real piece 
    pieces_list = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
   
    #validate a piece
    if values[0] in 'bw':
        if values[1:] in pieces_list:
            piecesQuantity(values)
            print(f'and {values} is a valid piece')

        else:
            print(f'but {values} is not a valid piece')
    else: 
        print(f'{values} is not a valid movement')   

#*Principal Function
def isValidChessBoard(chess):

    for keys, values in chess.items(): 
        validateMovement(keys.lower())#dictionary keys(movements) and validate it
        validatePiece(values.lower())#dictionary values(pieces) and validate it 
        sleep(0.5)


#*Principal Program
chess_dictionary = {'a2':'bpawn', 'b2': 'bpawn', 'c2': 'bpawn', 'd2': 'bpawn', 'e2': 'bpawn', 'f2': 'bpawn', 'g2': 'bpawn', 'h2': 'bpawn', 'a1':'brook', 'h1':'brook','b1':'bknight', 'g1':'bknight', 'c1':'bbishop', 'f1':'bbishop', 'd1':'bqueen', 'e1':'bking', 'a7':'wpawn', 'b7': 'wpawn', 'c7': 'wpawn', 'd7': 'wpawn', 'e7': 'wpawn', 'f7': 'wpawn', 'g7': 'wpawn', 'h7': 'wpawn', 'a8':'wrook', 'h8':'wrook','b8':'wknight', 'g8':'wknight', 'c8':'wbishop', 'f8':'wbishop', 'd8':'wqueen', 'e8':'wking'}
isValidChessBoard(chess_dictionary)
for grade in grafico_chess:
    print(grade)
#