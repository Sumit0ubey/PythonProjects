from tkinter import *
from tkinter import ttk
from emoji import emojize
from random import choice, randint

rock = emojize(":fist:", language='alias')
paper = emojize(":hand:", language='alias')
scissors = emojize(":v:", language='alias')

option = [rock, paper, scissors]


def animate():
    roll_till = randint(15, 27)

    def update_selection(roll=0, count=roll_till):
        if count == 0:
            computer_choice = choice(option)
            computer_selection.config(text=computer_choice)
            determine_winner(player_selection.get(), computer_choice)
        else:
            computer_selection.config(text=option[roll])
            next_roll = (roll + 1) % 3
            computer_selection.after(100, update_selection, next_roll, count - 1)

    update_selection()


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        winner.config(text="It's a tie!")
    elif ((player_choice == rock and computer_choice == scissors) or
          (player_choice == paper and computer_choice == rock) or
          (player_choice == scissors and computer_choice == paper)):
        winner.config(text="You win!")
    else:
        winner.config(text="Computer wins!")


window = Tk()
window.title('Rock Paper Scissor | Project 8')
window.geometry('600x400')
window.resizable(False, False)

ttk.Label(window, text='Rock Paper Scissor Game', font=("Comic Sans MS", 16)).pack(pady=25)
player_frame = Frame(window)
ttk.Label(player_frame, text="You", font=("Helvetica", 14)).pack(expand=TRUE)
player_selection = StringVar()
player_selection.set(option[0])
for i in range(3):
    ttk.Radiobutton(player_frame, text=option[i], variable=player_selection, value=option[i]).pack(anchor=W)
player_frame.pack(side=LEFT, anchor=NW, padx=50)

computer_frame = Frame(window)
ttk.Label(computer_frame, text="Computer", font=("Helvetica", 14)).pack()
computer_selection = Label(computer_frame, text='', font=("Helvetica", 32), width=4, height=2)
computer_selection.pack(pady=10)
ttk.Button(computer_frame, text="Computer turn", command=animate).pack(pady=10)
computer_frame.pack(side=RIGHT, anchor=NE, padx=50)

result = Frame(window)
winner = ttk.Label(result, text='Winner is ', font=("Helvetica", 14))
winner.pack()
result.pack(side=BOTTOM, fill=X, pady=30, padx=50)

window.mainloop()
