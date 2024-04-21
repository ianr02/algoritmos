from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, Image
from PIL import Image, ImageTk
import os
import urllib.request
from io import BytesIO



def open_(filename):
    window.destroy()
    user_path = os.path.expanduser("~/Downloads/")
    os.chdir(user_path)
    os.system('python '+filename)


def button(url, file, x, y, w, h):
    u = urllib.request.urlopen(url)
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((170, 140))
    photo = ImageTk.PhotoImage(im)
    button = Button(image=photo, command=lambda: open_(file))
    button.image = photo
    button.place(x=x, y=y, width=w, height=h)


def img(file, x, y):
    user_path = os.path.expanduser("~/Downloads/")
    absolute_path = os.path.dirname('inicio/assets/frame0/')
    relative_path = file
    full_path = os.path.join(user_path + absolute_path + relative_path)
    image = ImageTk.PhotoImage(Image.open(full_path))
    image_label = Label(window, bg="#FFFFFF", image=image)
    image_label.place(x=x, y=y)
    image_label.image = image


def path(file):
    user_path = os.path.expanduser("~/Downloads/")
    absolute_path = os.path.dirname('inicio/assets/frame0/')
    relative_path = file
    full_path = os.path.join(user_path + absolute_path + relative_path)
    return full_path


window = Tk()

window.geometry("1280x832")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 541.0, 832.0, fill="#5D8E5F", outline="")

canvas.create_text(48.0, 126.0, anchor="nw", text="Listo para hacer \nun cambio?", fill="#132B1D", font=("Lato Bold", 64 * -1))

canvas.create_text(818.0, 169.0, anchor="nw", text="¡Bienvenidos!", fill="#000000", font=("Lato Bold", 36 * -1))

canvas.create_text(664.0, 334.0, anchor="nw", text="Ingresa tu carnet de estudiante", fill="#1B3C29", font=("Lato SemiBold", 24 * -1))

canvas.create_text(694.0, 232.0, anchor="nw", text="Necesitas iniciar sesión con tu cuenta para \n                      ingresar a la página.", fill="#000000", font=("Lato Regular", 24 * -1))

img('/image_1.png', 48, 331)

canvas.create_text(664.0, 428.0, anchor="nw", text="Contraseña", fill="#1B3C29", font=("Lato SemiBold", 24 * -1))

entry_image_1 = PhotoImage(file=path("/entry_1.png"))
entry_bg_1 = canvas.create_image(925.0, 489.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=680.0, y=470.0, width=490.0, height=37.0)

# Iniciar sesion
button("https://t3.ftcdn.net/jpg/05/99/24/32/240_F_599243211_OV8joBt12UZSpWS1a7kPArSo9sKwXVCH.jpg", "menu/menu.py", 838.0, 543.0, 174.0, 80.0)

entry_image_2 = PhotoImage(file=path("/entry_2.png"))
entry_bg_2 = canvas.create_image(925.0, 394.5, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_2.place(x=680.0, y=375.0, width=490.0, height=37.0)

window.resizable(False, False)
window.mainloop()
