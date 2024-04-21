from pathlib import Path
from tkinter import Tk, Canvas, Button, Label, Image
from PIL import Image, ImageTk
import os
import urllib.request
from io import BytesIO


def open_(filename):
    menu.destroy()
    user_path = os.path.expanduser("~/Downloads")
    os.chdir(user_path)
    os.system('python '+filename)


def button(url, file, x, y, w, h):
    u = urllib.request.urlopen(url)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((50, 50))
    photo = ImageTk.PhotoImage(im)
    button = Button(image=photo, command=lambda: open_(file))
    button.place(x=x, y=y, width=w, height=h)
    button.image = photo


def img(file, x, y):
    user_path = os.path.expanduser("~/Downloads/")
    absolute_path = os.path.dirname('menu/assets/frame0/')
    relative_path = file
    full_path = os.path.join(user_path + absolute_path + relative_path)
    image = ImageTk.PhotoImage(Image.open(full_path))
    image_label = Label(menu, image=image, bg="#FFFFFF")
    image_label.place(x=x, y=y)
    image_label.image = image


menu = Tk()
menu.geometry("1280x832")
menu.configure(bg="#FFFFFF")
canvas = Canvas(menu, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)
canvas.create_text(35.0, 217.0, anchor="nw", text="Actividades:", fill="#000000", font=("Lato Regular", 36 * -1))

img("/image_1.png", 35, 280)

img("/image_2.png", 35, 650)

img("/image_3.png", 535, 650)

canvas.create_rectangle(0.0, 0.0, 1280.0, 182.0, fill="#81B16B", outline="")

canvas.create_text(35.0, 14.0, anchor="nw", text="Hello.", fill="#1B3C29", font=("Inter SemiBold", 128 * -1))

# Perfil
button("https://cdn-icons-png.flaticon.com/512/6522/6522516.png", "perfil/perfil.py", 985.0, 60.0, 77.0, 63.0)

canvas.create_text(35.0, 600.0, anchor="nw", text="Charlas o información:", fill="#000000", font=("Lato Regular", 36))

# Home
button("https://cdn-icons-png.flaticon.com/512/25/25694.png", "menu/menu.py", 1081.0, 60.0, 77.0, 63.0)

# Notificaciones
button("https://cdn-icons-png.flaticon.com/512/60/60753.png", "menu/menu.py", 889.0, 60.0, 77.0, 63.0)

# Info
button("https://cdn-icons-png.flaticon.com/512/6399/6399624.png", "info/info.py", 1163.0, 380.0, 90.0, 90.0)

menu.resizable(False, False)
menu.mainloop()
