import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog as fd

root = tk.Tk()
root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()


def left_clik(event):
    # print B G R color
    print(event.x, event.y)
    print(panel.image[event.y, event.x])


def openfn():
    filename = fd.askopenfile(title='open')
    return filename


def select_img():
    global panel
    path = fd.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        if panel is None:
            panel = tk.Label(image=image)
            panel.image = image
            panel.pack(side="left", padx=10, pady=10)
        else:
            panel.configure(image=image)
            panel.image = image


def open_img():
    x = openfn()
    img = Image.open(x)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()


panel = None
button = tk.Button(root, text="Select image", command=open_img)
button.pack(side="bottom", padx=10, pady=10)

root.bind("<Button-1>", left_clik)

root.mainloop()
