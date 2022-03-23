
Grid = [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]    
win = False
import random
import Connect_4_GUI as G
turns_no = 0
        
G.Grid() 
def Check(cooX,cooY,Turn,ref):
    win = False
    #Checking for Win
    #Check Below
    for a in range (1,5):
        try:
            if Grid[cooY+a][cooX] == ref:
                if a == 3 :
                    win = True
                    print("Player ",Turn," Wins!")

            else:
                break
        except:
            IndexError
            break

    #Check Horizontal
    score = int(0)
    for b in range (1,5):
        try:
            if Grid[cooY][cooX+b] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    for b in range (1,5):
        try:
            if Grid[cooY][cooX-b] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    
    #Check Positive Gradient Diagonal
    score = int(0)
    for c in range (1,5):
        try:
            if Grid[cooY+c][cooX-c] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    for c in range (1,5):
        try:
            if Grid[cooY-c][cooX+c] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    #Check Negative Gradient Diagonal
    score = int(0)
    for c in range (1,5):
        try:
            if Grid[cooY+c][cooX+c] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    for c in range (1,5):
        try:
            if Grid[cooY-c][cooX-c] == ref:
                score = score + 1
                if score == 3 :
                    win = True
                    print("Player ",Turn," Wins!")
            else:
                break
        except:
            IndexError
            break
    
    return win
    
#def Full():
    #Ends game when theboard is full
    #print("All of the columns are full, so nobody wins!")
    #G.win("NOBODY")

def Input():
    while True:
        try:
            cooX = int(input("What column would you like to put a chip in?: "))
        except:
            ValueError
            print("...Invalid...")
        else:
            if cooX > 7:
                print("...Invalid...")
                continue
            else:
                break
            
    return cooX
    
def gravity(cooX,Grid):
    #Makes the piece fall to the bottom of the grid
    for cooY in range (0,6):
        if (Grid[cooY][cooX] == "X") or (Grid[cooY][cooX] == "O"):
            cooY = cooY-1
            break
    return cooY

def AI():
    #calculates the AI's actions
    move = random.randint(1,7)
    return move


                            #====================Start of the main code====================
#Player selection screen
  
while True:
    try:
        players = int(input("What mode would you like to play?:\n1.   1 vs AI: \n2.   1 v 1: "))
    except:
        ValueError
        print("...Invalid...")
    else:
        if players != 1 and players != 2:
            print("...Invalid...")
            continue
        else:
            break

                                    #====================X's Turn====================    
while win!= True:
    print("\n====Player RED's turn====")
    G.Turns("X")
    cooX = Input()
    while Grid[0][cooX-1] == "X" or Grid[0][cooX-1] == "O":
        print("...This column is full!...")
        print("Please try again?: ")
        cooX = Input()
    cooY = gravity(cooX-1,Grid)
    G.Move(cooX,cooY)
    Grid[cooY][cooX-1] = "X"
    win = Check(cooX-1,cooY,"RED","X")
    if win == True:
        G.win("RED")
        break
    turns_no += 1
    #if turns_no == 42:
        #Full()
        #break
    
                                    #====================O's Turn====================
    print("\n====Player BLUE's turn====")
    G.Turns("O")
    if players == 1:
        print("Thinking...")
        cooX = AI()
    elif players == 2:
        cooX = Input()
        while Grid[0][cooX-1] == "X" or Grid[0][cooX-1] == "O":
            print("...This column is full!...")
            print("Please try again?: ")
            cooX = Input()
    cooY = gravity(cooX-1,Grid)
    G.Move(cooX,cooY)
    Grid[cooY][cooX-1] = "O"
    win = Check(cooX-1,cooY,"BLUE","O")
    if win == True:
        G.win("BLUE")
        break
    turns_no += 1
    #if turns_no == 42:
        #Full()
        #break
    

