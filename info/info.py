from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Image
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
    im = im.resize((50, 50))
    photo = ImageTk.PhotoImage(im)
    button = Button(image=photo, command=lambda: open_(file))
    button.place(x=x, y=y, width=w, height=h)
    button.image = photo


def img(file, x, y):
    user_path = os.path.expanduser("~/Downloads/")
    absolute_path = os.path.dirname('info/assets/frame0/')
    relative_path = file
    full_path = os.path.join(user_path + absolute_path + relative_path)
    image = ImageTk.PhotoImage(Image.open(full_path))
    image_label = Label(window, image=image, bg="#FFFFFF")
    image_label.place(x=x, y=y)
    image_label.image = image


window = Tk()
window.geometry("1280x760")
window.configure(bg="#FFFFFF")
canvas = Canvas(window, bg="#FFFFFF", height=760, width=1280, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)

img('/image_1.png', -5, 230)

canvas.create_rectangle(70.0, 239.0, 1182.0, 617.0, fill="#4D6472", outline="")

canvas.create_text(79.0, 261.0, anchor="nw", text="Más detalles:\nEste 29 de marzo nos puedes ayudar a limpiar la playa de Monterrico, nos reuniremos \ndesde las 9:00 am en ---. Podrás llegar hasta las 6 pm.\n\nRecomendaciones:\nTe recomendamos llevar gorra, protector solar, ropa y zapatos cómodos \ny bastante agua pura.\n\n¿Qué debes llevar?\nNo es necesario llevar nada, nosotros proveemos todo lo necesario para poder \nlimpiar la playa, gracias a nuestros patrocinadores: ", fill="#FFFFFF", font=("Lato Regular", 24 * -1))


canvas.create_rectangle(0.0, 619.0, 1280.0, 771.0, fill="#E1E8EE", outline="")

canvas.create_text(562.0, 629.0, anchor="nw", text="Contacto:", fill="#000000", font=("Lato Bold", 40 * -1))

canvas.create_text(566.0, 674.0, anchor="nw", text="gmail: ejemplo@gmail.com", fill="#000000", font=("Lato Regular", 24 * -1))

canvas.create_text(562.0, 705.0, anchor="nw", text="teléfono: 1234-5678", fill="#000000", font=("Lato Regular", 24 * -1))

canvas.create_text(139.0, 645.0, anchor="nw", text="Recuerda que si tienes alguna otra \nduda puedes escribir o llamar a:", fill="#000000", font=("Lato Regular", 24 * -1))

canvas.create_text(900.0, 629.0, anchor="nw", text="Redes sociales:", fill="#000000", font=("Lato Bold", 40 * -1))

canvas.create_text(900.0, 671.0, anchor="nw", text="Instagram: @ejemplo_1", fill="#000000", font=("Lato Regular", 24 * -1))

canvas.create_text(900.0, 705.0, anchor="nw", text="facebook: @ejemplo_2", fill="#000000", font=("Lato Regular", 24 * -1))

canvas.create_rectangle(0.0, 142.0, 1280.0, 241.0, fill="#32784F", outline="")

canvas.create_text(37.0, 167.0, anchor="nw", text="Monterrico", fill="#E9E0C3", font=("Inter SemiBold", 48 * -1))

canvas.create_rectangle(0.0, 1.0, 1280.0, 141.0, fill="#81B16B", outline="")

canvas.create_text(37.0, 1.0, anchor="nw", text="Hello", fill="#1B3C29", font=("Inter SemiBold", 128 * -1))

# Perfil
button("https://cdn-icons-png.flaticon.com/512/6522/6522516.png", "perfil/perfil.py", 985.0, 40.0, 77.0, 63.0)

# Home
button("https://cdn-icons-png.flaticon.com/512/25/25694.png", "menu/menu.py", 1081.0, 40.0, 77.0, 63.0)

# Notificaciones
button("https://cdn-icons-png.flaticon.com/512/60/60753.png", "menu/menu.py", 889.0, 40.0, 77.0, 63.0)

window.resizable(False, False)
window.mainloop()
