from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("472x319")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 319,
    width = 472,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    177.0, 119.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 67, y = 257,
    width = 89,
    height = 25)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    116.5, 154.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 30, y = 142,
    width = 173,
    height = 22)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    116.5, 214.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 30, y = 203,
    width = 173,
    height = 21)

window.resizable(False, False)
window.mainloop()
