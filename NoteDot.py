from CONSTANTS import *

class NoteDot:
    def __init__(self, x, y, note, color, canvas, Display, size=10, shift=2):
        '''

        :param x: x location of center(ish) of dot
        :param y: y location of center(ish) of dot
        :param note: String value - name of note
        :param color: Color (hex or keyword) corresponding to keytone
        :param size: Size of the dot (radius'ish')
        :param shift: SHIFT NOTE NAME DISPLAY RIGHT(+) or LEFT (-)
        '''

        self.x = x
        self.y = y

        self.canvas = canvas
        self.display = Display

        self.defaultSize = 10
        self.size = size
        self.shift = shift
        self.note = note
        self.color = color

        self.shadeAmount = 125  # amount to subtract from RGB when run through shade() function

        self.fontColor = black
        self.font = "Arial 15 bold"

        if self.color == gray:
            self.fontColor = darkGray
            self.font = "Arial 10 bold"
            self.size -= 1
        self.size2 = self.size - 2  # size of highlight on note

        if not Display.colorBlindMode:
            self.create_color_dots()




        if Display.colorBlindMode:
            self.create_color_dots()



    def create_color_dots(self):
            # --- Shaded / outlined base for Note
            self.A = self.display.canvas.create_oval(self.x + self.size * 1.5, self.y - self.size, self.x - self.size,
                                                     self.y + self.size,
                                                     fill=shade(self.color, self.shadeAmount),
                                                     outline=shade(shade(self.color, self.shadeAmount),
                                                                   self.shadeAmount),
                                                     width=1)
            # --- 'Highlight' on Note - uses color from preset [r g b y] list
            self.B = self.display.canvas.create_oval(self.x + self.size2 * 1.5, self.y - self.size2,
                                                     self.x - self.size2,
                                                     self.y + self.size2,
                                                     fill=self.color,
                                                     outline='')

            self.C = self.display.canvas.create_text(self.x + self.shift, self.y, text=self.note, font=self.font,
                                                     fill=self.fontColor)

            # binds whole note dot display to action   ----------VVVVV
            x = self
            self.display.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))
            self.display.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))
            self.display.canvas.tag_bind(self.C, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))

    def create_shape_dots(self):
        #### EDIT EDIT EDIT. use conditions of COLOR to determine what shape to use ----- draw shapes with own FUNCTIONS FOR EACH
        self.color = white
        self.size *=1.5
        self.size2 *= 1.5
        # --- Shaded / outlined base for Note
        self.A = self.display.canvas.create_polygon([self.x + self.size, self.y, self.x, self.y + self.size, self.x - self.size, self.y,self.x, self.y - self.size ],   # https://www.python-course.eu/tkinter_canvas.php
                                                 fill=shade(self.color, self.shadeAmount),
                                                 outline=shade(shade(self.color, self.shadeAmount), self.shadeAmount),
                                                 width=1)
        # --- 'Highlight' on Note - uses color from preset [r g b y] list
        self.B = self.display.canvas.create_polygon([self.x + self.size2, self.y, self.x, self.y + self.size2, self.x - self.size2, self.y,self.x, self.y - self.size2 ],
                                                 fill=self.color,
                                                 outline='')

        self.C = self.display.canvas.create_text(self.x + self.shift, self.y, text=self.note, font=self.font,
                                                 fill=self.fontColor)

        # binds whole note dot display to action   ----------VVVVV
        x = self
        self.display.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))
        self.display.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))
        self.display.canvas.tag_bind(self.C, '<ButtonPress-1>', lambda v: self.display.ALL(newRoot_Dot=x))





    def replaceDot(self, canvas):  # , x, y, note, color, size, shift):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.C)
