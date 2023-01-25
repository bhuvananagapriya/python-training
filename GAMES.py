#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ROCK PAPER SCISSORS GAME
from random import randint
choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=5
while p_score!=limit and c_score!=limit:
    print(f"enter among the folloowing",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice: {sys_ch}")
    if my_ch==sys_ch:
        print("Draw")
        continue
    if my_ch=="rock" and sys_ch=="scissor":
        p_score+=1
    elif my_ch=="paper" and sys_ch=="rock":
        p_score+=1
    elif my_ch=="scissor" and sys_ch=="paper":  
        p_score+=1
    else:
        c_score+=1
    print(f"your score: {p_score},system score: {c_score}")
    
    
if p_score>c_score:
    print("you win the match")
else:
    print("system wins the match")


# In[10]:


#TIC TAC TOE GAME
board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
def print_board(board):
    print(*board[0],sep="|")
    print("---------------")
    print(*board[1],sep="|")
    print("---------------")
    print(*board[2],sep="|")
    print("---------------")
print_board(board)
def get_markers():
    marker1=input("player 1 choice(X or O):").upper()
    marker2=""
    if marker1=='X':
        marker2='O'
        return['X','O']
    elif marker1=='O':
        marker2='X'
        return['O','X']
    else:
        return get_markers
player1=0
player2=0    
m1,m2=get_markers()
print(f"player:{m1},player2:{m2}")
def get_coordinates():
    x,y=list(map(int,input("enter the coordinates").split()))
    if x in [0,1,2] and y in [0,1,2]:
        return[x,y]
    else:
        print("Invalid Input")
        return get_coordinates()
x,y=get_coordinates()
print(x,y) 
def check_win(board):
    for row in board:
        if row[0]==row[1] and row[1] == row[2] and row:
            return True
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] ==board[2][0]
            return True
    if board[0][0] ==board[1][i]
def update_board(board,chance,marker,x,y):            #player1 ----->chance if chance=True
    if chance==True:
        board[x][y]=marker
        return False
    else:
        board[x][y]=marker
        chance=True
def play_game():
    player1=0
    player2=0
    m1,m2=get_markers()
    print(f"player 1:{m1},player2:{m2}")
    chance=True
    while True:
        x,y=get_coordinates()
        if chance:
            chance=update_board(board,chance,m1,x,y)
        else:
            chance=update_board(board,chance,m2,x,y)
play_game()


# In[ ]:




