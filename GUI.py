from tkinter import *


class GuiMain:
    def __init__(self):
        root = Tk()
        root.title("Game")

        canvas = Canvas(root, width=1350, height=800, bg='white')
        canvas.pack()

        for i in range(36):
            x = 50 + (i * 40)
            canvas.create_line(x, 800, x, -850, width=4)

        for i in range(36):
            y = 50 + (i * 40)
            canvas.create_line(1600, -y, 10, -y, width=4)

        root.mainloop()


if __name__ == '__main__':
    GuiMain()
