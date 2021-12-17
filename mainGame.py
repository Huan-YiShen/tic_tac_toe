from tkinter import *
import tkinter.font as font
'''
Game board position is indexed as the follow
1,2,3
4,5,6
7,8,9
'''
# #######################################################
# global variables
WIN_CONDITION = [[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [1,4,7],
                 [2,5,8],
                 [3,6,9],
                 [1,5,9],
                 [3,5,7]
                ]
BTN_gameBoard = list(range(9))
TURN = 0
X_PLAY = True
# #######################################################

def deactivateALL():
    for btn in BTN_gameBoard:
        btn.config(state = "disabled")
    
    
def restart(lab_message):
    global TURN, X_PLAY
    TURN = 0
    X_PLAY = True
    lab_message.config(text = "x goes first")
    for index, btn in enumerate(BTN_gameBoard):
        btn.config(text = index+1, state = "normal", background = 'SystemButtonFace')
    
    print("New Game _______________________________________________")
    

def take_turn(btn_index, lab_message):
    # displace output on screen 
    global TURN, X_PLAY, BTN_gameBoard, WIN_CONDITION

    currentlyPlaying = ""
    if X_PLAY:
        currentlyPlaying = 'X'
        nextPlaying = 'O'
        TURN = TURN +1
        X_PLAY = False
    else:
        currentlyPlaying = 'O'
        nextPlaying = 'X'
        X_PLAY = True

    BTN_gameBoard[btn_index].config(text = currentlyPlaying, state = "disabled")
    print(f"Current Turn: {TURN} | {currentlyPlaying} played in square {btn_index+1}")


    # detect win conditon
    finish = False
    if TURN > 2:
        for variation in WIN_CONDITION:
            btn1 = BTN_gameBoard[variation[0]-1]
            btn2 = BTN_gameBoard[variation[1]-1]
            btn3 = BTN_gameBoard[variation[2]-1]
            # print(f"btn1: {variation[0]}, {btn1.cget('text')} | btn2: {variation[1]}, {btn2.cget('text')} | btn3: {variation[2]}, {btn3.cget('text')}")

            if btn1.cget('text') == btn2.cget('text') == btn3.cget('text'):
                btn1.config(bg = "yellow")
                btn2.config(bg = "yellow")
                btn3.config(bg = "yellow")
                finish = True
                break
    
    if finish == True:
        lab_message.config(text = f"{currentlyPlaying} WON")
        deactivateALL()
    elif TURN == 5:
        lab_message.config(text = f" DRAW ")
    else: 
        lab_message.config(text = f"{nextPlaying}'s turn")


    
def create_btn(root, index, lab_message):
    size = font.Font(size=30)
    return  Button(root, text = (index+1), padx = 40, pady = 40, borderwidth =3, font = size, command = lambda: take_turn(index, lab_message))
    

def gameGUI():
    root = Tk()
            
    # initate GUI objects
    lab_message = Label(root, text = "x goes first")

    global BTN_gameBoard    
    BTN_gameBoard[0] = create_btn(root, 0, lab_message)
    BTN_gameBoard[1] = create_btn(root, 1, lab_message)
    BTN_gameBoard[2] = create_btn(root, 2, lab_message)
    BTN_gameBoard[3] = create_btn(root, 3, lab_message)
    BTN_gameBoard[4] = create_btn(root, 4, lab_message)
    BTN_gameBoard[5] = create_btn(root, 5, lab_message)
    BTN_gameBoard[6] = create_btn(root, 6, lab_message)
    BTN_gameBoard[7] = create_btn(root, 7, lab_message)
    BTN_gameBoard[8] = create_btn(root, 8, lab_message)

    end_btn = Button(root, text = "new game", borderwidth =3, command = lambda: restart(lab_message))

   

    # placement of GUI elements
    lab_message.grid(row = 0, column = 0, columnspan=3)
    btn_index = 0
    for row_ind in range(1,4):
        for col_ind in range(3):
            BTN_gameBoard[btn_index].grid(row = row_ind, column = col_ind) 
            btn_index += 1        
    end_btn.grid(row = 4, column = 0, columnspan = 3)
        
    root.mainloop()


if __name__ == "__main__":
    # initiate GUI
    root = gameGUI()
    
    