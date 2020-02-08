import image
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

#TODO: print ' - ' when there is space between 2 words
#TODO: Create reset button

#init the words list
wordslist = ['CORRECTION', 'CHILDISH', 'BEACH', 'PYTHON', 'ASSERTIVE', 'INTERFERENCE', 'COMPLETE', 'SHARE', 'CREDIT CARD', 'RUSH', 'SOUTH']
word = random.choice(wordslist)
inGame = True
times = 0
hidden_word = []

window = Tk()
window.title("Hangman GAME!")
window.geometry("800x600")
#init the image - its size, the source of the image and attach it to 'tkinter'
image_src = ['Pictures/init.png','Pictures/head.png',
             'Pictures/body.png','Pictures/right_hand.png',
             'Pictures/left_hand.png','Pictures/left_leg.png',
             'Pictures/right_leg.png','Pictures/dead.png']
img = Image.open(image_src[0])
img = img.resize((150,150),Image.ADAPTIVE)
img = ImageTk.PhotoImage(img)

panel = Label(window, image = img)
panel.grid(column=0, row=0)

#check if the letter that the user clicked exist in the word
def clicked(letter):
    isLetterFound = False
    global times
    for index,let in enumerate(word): #looping to check if the letter exist
        if letter == let:
            arry_display[index].config(text = letter)
            hidden_word[index] = letter
            isLetterFound = True
    # If letter was not found, then update the image and increment by one his turn (times)
    if isLetterFound == False:
        times +=1
        image = Image.open(image_src[times])
        image = image.resize((150, 150), Image.ADAPTIVE)
        imageW = ImageTk.PhotoImage(image)
        panel.configure(image = imageW)
        panel.image = imageW

    if checkIfWin(hidden_word):
        messagebox.showinfo("Hang man", "Congratulations You win!")
        window.destroy()
    if times == 6:
        image = Image.open(image_src[7])
        image = image.resize((150, 150), Image.ADAPTIVE)
        imageW = ImageTk.PhotoImage(image)
        panel.configure(image=imageW)
        panel.image = imageW
        messagebox.showinfo("Hang man", "Too bad, you lost!")


#checking if there are * in 'hidden_word'
#if there are not * it means that the user guessed all the letters
def checkIfWin(hidden):
    if "*" in hidden:
        return False
    else:
        return True


#init Array of 'display disabled buttons' - it changes by the length of the word
arry_display = []
for i in range(0,len(word)):
    display = Button(window, text=" ", bg="white", fg="Black", width=3, height=1, font=('Helvetica', '20'))
    display.configure(state=DISABLED)
    display.grid(column=i+2, row=0)
    arry_display.append(display)

#init hidden word and also array_disply
#hidden_word contains the word with stars, its just for comparing in the 'clicked' function
#index % 3 == 0 to print every 3 letter word, and the rest blank
for index,ch in enumerate(word):
    if index % 3 == 0:
        arry_display[index].config(text=ch)
        hidden_word.append(ch)
    else:
        hidden_word.append("*")

#init the alfa button letters
#row 1
btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn8.grid(column=8, row=1)
btn9 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn9.grid(column=9, row=1)

#row 2
btn10 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn10.grid(column=2, row=2)
btn11= Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn11.grid(column=3, row=2)
btn12 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn12.grid(column=4, row=2)
btn13 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn13.grid(column=5, row=2)
btn14 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn14.grid(column=6, row=2)
btn15 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn15.grid(column=7, row=2)
btn16 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn16.grid(column=8, row=2)

#row 3
btn17 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn17.grid(column=2, row=3)
btn18 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn18.grid(column=3, row=3)
btn19 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn19.grid(column=4, row=3)
btn20 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn20.grid(column=5, row=3)
btn21 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn21.grid(column=6, row=3)
btn22 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn22.grid(column=7, row=3)
btn23 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn23.grid(column=8, row=3)

window.mainloop()

