def print_board(a):
    print("",a[1],"|",a[2],"|",a[3],"")
    print("___|___|___")
    print("",a[4]," |",a[5],"|",a[6],"")
    print("___|___|___")
    print("",a[7],"|",a[8],"|",a[9],"")

# for display the instrucction of game

def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE -----------\n\n")
    print_board(pos)
    print()

    players[0]=input("player 1 :")
    players[1]=input("player 2 :")

    print("\n-------- instructions --------")
    print("->",players[0],"you will using x")
    print("->",players[1],"you will using 0")
    print("-> Turn starts from",players[0])
    print("-> Potisions are like:-")
    print("1 |2 |3 ")
    print("__|__|__")
    print("4 |5 |6 ")
    print("__|__|__")
    print("7 |8 |9 ")
    print("->press 5 to start the game")
    flag = input()
    return flag

# for  start the game

def startgame():
    turn=0
    for i in range(9):
        if turn % 2==0:
            print("\nthis is ur turn",players[0])
            p=int(input("please enter postion:"))
            v="x"
            pos[p]=v
            print_board(pos)
            winner= checkwin(v)
            if winner is "nobody":
                turn = 1
                continue
            else:
                print("\n\nHurray 11",players[0],"you win")
                break
        else:
            print("\nthis is ur turn",players[1])
            p=int(input("please enter the postion"))
            v="0"
            pos[p]=v
            print_board(pos)
            winner = checkwin(v)
            if winner is "nobody":
                turn=0
                continue
            else:
                print("\n\nHurray 11",players[1],"you win")
                break
    else:
        print("\n\nGame is Tie")

# check for winner 

def checkwin(v):
    for i in winner_conditions:     
        if (pos[i[0]],pos[i[1]],pos[i[2]])==(v,v,v):
            winner=players[0]
            break
        elif (pos[i[0]],pos[i[1]],pos[i[2]])==(v,v,v):
            winner = players[1]
    else:
        winner ="nobody"
    return winner

#  main code

pos = ['',' ',' ',' ',' ',' ',' ',' ',' ','']
players=[' ',' ']
winner_conditions=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = print_instructions()
if flag=='s' or flag=='s':
    startgame()
else:
    print("invalid enter")



