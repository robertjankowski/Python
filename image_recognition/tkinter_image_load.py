from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as fd
import cv2


def callback(event):
    print(event.x, event.y)


def select_image():
    global panelA, panelB
    path = fd.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(grey, 50, 100)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)

        else:
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged


root = Tk()
panelA = None
panelB = None

root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx=10, pady=10)

root.bind("<Button-1>", callback)

root.mainloop()
