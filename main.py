import tkinter
import random
import time
import word_list


def get_rand_word():
    word = random.choice(word_list.word_list)
    return word


def start(event):
    global time_start
    global count_down
    count_down = True
    time_start = time.time()
    prompt_label.config(text="")


def next_word(event):
    global rand_word
    global words_completed
    global time_start
    global count_down

    if count_down and time.time() - time_start >= 30:       # Tells user result
        count_down = False
        result_label_1.config(text=f"WPM: ~{round((words_completed / (time.time() - time_start)) * 60)}")
        result_label_2.config(text=f"Words Typed: {words_completed}")

    if count_down and input_box.get() == rand_word:
        rand_word = get_rand_word()
        input_box.delete(0, len(input_box.get()))
        word_label.config(text=rand_word)
        words_completed += 1


def reset():
    global words_completed
    global count_down

    result_label_1.config(text="")
    result_label_2.config(text="")
    prompt_label.config(text="Double Click to begin. You will have 30 seconds.")
    words_completed = 0
    count_down = False


count_down = False
time_start = 0
words_completed = 0
rand_word = get_rand_word()


# --------------------- GUI Setup ----------------------- #


# Window

window = tkinter.Tk()
window.title("WPM Test App")
window.geometry("300x300")

window.bind("<Key>", next_word)
window.bind("<Double 1>", start)

# Input Box

input_box = tkinter.Entry(width=30)

# Labels

title_label = tkinter.Label(text="WPM Test")
word_label = tkinter.Label(text=rand_word)
prompt_label = tkinter.Label(text="Double Click to begin. You will have 30 seconds.")
result_label_1 = tkinter.Label(text="")
result_label_2 = tkinter.Label(text="")

# Buttons

reset_button = tkinter.Button(text="Reset", command=reset)

# Grid

title_label.grid(column=0, row=0)
word_label.grid(column=0, row=1)
input_box.grid(column=0, row=2)
prompt_label.grid(column=0, row=3)
result_label_1.grid(column=0, row=4)
result_label_2.grid(column=0, row=5)
reset_button.grid(column=0, row=6)


window.mainloop()
