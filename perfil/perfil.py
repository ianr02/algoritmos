from tkinter import Tk, Canvas, Button, Label, Image
from PIL import Image, ImageTk
import os
import urllib.request
from io import BytesIO


def open_(filename):
    perfil.destroy()
    user_path = os.path.expanduser("~/Downloads/")
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
    absolute_path = os.path.dirname('perfil/assets/frame0/')
    relative_path = file
    full_path = os.path.join(user_path + absolute_path + relative_path)
    image = ImageTk.PhotoImage(Image.open(full_path))
    image_label = Label(perfil, bg="#FFFFFF", image=image)
    image_label.place(x=x, y=y)
    image_label.image = image


perfil = Tk()
perfil.geometry("1280x832")
perfil.configure(bg="#FFFFFF")
canvas = Canvas(perfil, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_text(573.0, 321.0, anchor="nw", text="Usuario: nombre_12345\nNombre: nombres\nApellidos: Apellidos \nCorreo: nombre@gmail.com\n", fill="#000000", font=("Lato Regular", 36 * -1))

# contraseña
button("https://cdn-icons-png.flaticon.com/512/561/561127.png", "menu.py", 573.0, 514.0, 77, 63)

# contraseña
button("https://cdn-icons-png.flaticon.com/512/6117/6117000.png", "menu.py", 773.0, 514.0, 77, 63)

canvas.create_rectangle(0.0, 0.0, 1280.0, 182.0, fill="#81B06A", outline="")

canvas.create_text(46.0, 14.0, anchor="nw", text="Hello.", fill="#1B3C29", font=("Inter SemiBold", 128 * -1))

img("/image_1.png", 201, 334)

# Perfil
button("https://cdn-icons-png.flaticon.com/512/6522/6522516.png", "perfil/perfil.py", 985.0, 60.0, 77.0, 63.0)

# Home
button("https://cdn-icons-png.flaticon.com/512/25/25694.png", "menu/menu.py", 1081.0, 60.0, 77.0, 63.0)

# Notificaciones
button("https://cdn-icons-png.flaticon.com/512/60/60753.png", "menu/menu.py", 889.0, 60.0, 77.0, 63.0)

perfil.resizable(False, False)
perfil.mainloop()
