import tkinter as tk
import random

# Initializing window

root = tk.Tk()
root.geometry('512x384')
root.resizable(False, False)
root.title('Rock, paper, scissors!')
root.config(bg = 'pink')

# Header

header = tk.Label(text = 'Let\'s play!', font = 'arial 15 bold', bg = 'pink')
header.place(relx = .5, y = 50, anchor = tk.CENTER)

# User choice

label = tk.Label(text = 'Choose your weapon:', font = 'arial 10 bold', bg = 'pink')
label.place(relx = .5, y = 100, anchor = tk.CENTER)

user_choice = tk.StringVar()

entry_1 = tk.Entry(font = 'arial 10', justify = tk.CENTER, textvariable = user_choice)
entry_1.place(relx = .5, y = 150, anchor = tk.CENTER)

# Function to play the game

result = tk.StringVar()

def play(*args):

    user_pick = user_choice.get().lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors']) # Here we define the computer choice.

    if user_pick == computer_choice:
        result.set('Tie. Computer also selected ' + user_pick + '.')
    elif user_pick == 'rock' and computer_choice == 'paper':
        result.set('You lose. Computer selected paper.')
    elif user_pick == 'rock' and computer_choice == 'scissors':
        result.set('You win. Computer selected scissors.')
    elif user_pick == 'paper' and computer_choice == 'rock':
        result.set('You win. Computer selected rock.')
    elif user_pick == 'paper' and computer_choice == 'scissors':
        result.set('You lose. Computer selected scissors.')
    elif user_pick == 'scissors' and computer_choice == 'rock':
        result.set('You lose. Computer selected rock.')
    elif user_pick == 'scissors' and computer_choice == 'paper':
        result.set('You win. Computer selected paper.')
    else:
        result.set('Invalid input. Please choice rock, paper or scissors.')

    output()
    show()

# Output

def output():
    output_label = tk.Label(font = 'arial 10 bold', textvariable = result, bg = 'pink')
    output_label.place(relx = .5, y = 250, anchor = tk.CENTER)

# Function to reset the game

def reset():
    user_choice.set('')
    result.set('')

#Function to exit the game

def exit():
    root.destroy()

# Now the buttons

play_button = tk.Button(font = 'arial 10 bold', text = 'PLAY', command = play)
play_button.place(relx = .5, y = 200, anchor = tk.CENTER)

root.bind('<Return>', play) # We let pressing the enter key instead of hitting the play button.

def show():

    reset_button = tk.Button(font = 'arial 10 bold', text = 'RESET', command = reset)
    reset_button.place(x = 150, y = 300)

    exit_button = tk.Button(font = 'arial 10 bold', text = 'EXIT', command = exit)
    exit_button.place(x = 300, y = 300)

root.mainloop()