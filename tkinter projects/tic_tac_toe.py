import random
from tkinter import *
from tkinter.messagebox import showinfo


def who_wins():
    global winner
    winner = False
    for combo in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for index in combo:
                buttons[index].config(bg="green")
            showinfo(title="Tic-Tac-Toe", message=f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

    if all(button["text"] != "" for button in buttons):
        showinfo(title="Tic-Tac-Toe", message="It's a Tie!")
        winner = True

    if winner:
        for button in buttons:
            button.config(state=DISABLED)


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        who_wins()
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")


def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", state=NORMAL, bg="SystemButtonFace")
    label.config(text=f"Player {current_player}'s turn")


window = Tk()
window.title('Tic-Tac-Toe | Project 7')

buttons = [Button(window, text="", font=('normal', 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in
           range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

option = ["X", "O"]
n = random.randint(0, 1)
current_player = option[n]
winner = False

label = Label(window, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

reset_button = Button(window, text="Reset", font=('normal', 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

window.resizable(False, False)
window.mainloop()
