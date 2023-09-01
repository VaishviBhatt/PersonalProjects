from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words={}

# -------------------------Reading file data ----------------------------
try:
    data = pd.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    Originaldata = pd.read_csv("data/french_words.csv")
    words = Originaldata.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill= "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill= "black")
    flip_timer = window.after(3000, func=flip_card)


#-------------------- flipping card--------------------------------------
def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")


#----------------------- words learnt ------------------------------------
def words_known():
    words.remove(current_card)
    df = pd.DataFrame(words)
    df.to_csv("data/Words_to_learn.csv", index= False)
    next_card()

#---------------------------- UI ------------------------------------------
# create a main window
window = Tk()
# set window title
window.title("flash cards")
# set window size
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# creates canvas widget for the images
canvas = Canvas(width= 800, height= 526)
# loads the images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
# create image inside canvas
card_background = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan= 2)

# create buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command= next_card)
unknown_button.grid(row= 1, column= 0)

check_image = PhotoImage(file= "images/right.png")
known_button = Button(image= check_image, highlightthickness=0, command= words_known)
known_button.grid(row= 1, column= 1)

next_card()

window.mainloop()
