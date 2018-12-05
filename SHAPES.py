from tkinter import *




from CONSTANTS import *
import NoteDot



class DIAMOND:
    def __init__(self, x, y,  note, fill , Display, size = 11, shift = 0, canvas = 'c'):
        self.x = x
        self.y = y
        shadeamnt = 50
        self.color = fill
        self.fill = shade(fill, shadeamnt)
        self.note = note

        self.font = "Arial 15 bold"

        self.canvas = Display.canvas# canvas

        self.shift = shift


        self.size = size

        self.defaultSize = 11

        self.outline = (1 / 6) * self.size
        # coordinates of polygon

        poly_coord = [ self.x,                  # North                     # DIAMOND
                       self.y - size,

                       self.x + size + size/2.5,# East
                       self.y,

                       self.x,                  # South
                       self.y + size,

                       self.x - size - size/2.5,           # West
                       self.y ]

        shade_size = self.size / 4
        borderComp = self.outline/2

        highlight_coord = [self.x,  # North                     # DIAMOND
                      self.y - size + borderComp,

                      self.x + size + size / 2.5 - shade_size - borderComp,  # East
                      self.y - shade_size/2,

                      self.x - borderComp,  # South
                      self.y + size - shade_size - borderComp,

                      self.x - size + shade_size/2 + borderComp,  # West
                      self.y - borderComp/1.1]





        self.A = self.canvas.create_polygon(poly_coord, fill = self.fill, outline = 'black', width = self.outline)
        self.B = self.canvas.create_polygon(highlight_coord, fill=lightn(self.fill, shadeamnt), outline='', width=self.outline)
        self.text = self.canvas.create_text(self.x, self.y, text = self.note, font = self.font)

        self.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot= self))
        self.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))



    def replaceDot(self, canvas):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.text)

class SQUARE:
    def __init__(self, x, y, note, fill, Display, size=12, shift=0, canvas='c'):
        self.x = x
        self.y = y
        shadeamnt = 100
        self.color = fill
        self.fill = shade(fill,shadeamnt)
        self.note = note

        self.font = "Arial 15 bold"
        if self.fill not in color_pallet:
            self.font = "Arial 10"


        self.canvas = Display.canvas # canvas

        self.shift = shift

        self.size = size+2
        self.defaultSize = 11
        self.adjust = 1.2
        self.outline = (1 / 6) * self.size
        if self.fill == shade(gray,shadeamnt):

            self.size -= 5

        # coordinates of polygon
        poly_coord = [self.x + self.size/self.adjust,  # lower right
                      self.y + self.size/self.adjust,

                      self.x - self.size/self.adjust,  # lower left
                      self.y + self.size/self.adjust,

                      self.x - self.size/self.adjust,  # upper left
                      self.y - self.size/self.adjust,

                      self.x + self.size/self.adjust,  # upper right
                      self.y - self.size/self.adjust,]

        shade_size = self.size/5
        borderComp = self.outline/2
        highlight_coord = [self.x + self.size / self.adjust - shade_size - borderComp,  # lower right
                      self.y + self.size / self.adjust - shade_size - borderComp,

                      self.x - self.size / self.adjust + borderComp,  # lower left
                      self.y + self.size / self.adjust - shade_size - borderComp,

                      self.x - self.size / self.adjust + borderComp,  # upper left
                      self.y - self.size / self.adjust + borderComp,

                      self.x + self.size / self.adjust - shade_size - borderComp,  # upper right
                      self.y - self.size / self.adjust + borderComp ]

        self.A = self.canvas.create_polygon(poly_coord, fill=self.fill, outline='black', width=self.outline)
        self.B = self.canvas.create_polygon(highlight_coord, fill=lightn(self.fill, shadeamnt), outline='', width=self.outline)
        self.text = self.canvas.create_text(self.x, self.y, text=self.note, font=self.font)

        self.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))

    def replaceDot(self, canvas):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.text)


class POLY_org:
    def __init__(self, x, y, note, fill, Display, size=12, shift=0, canvas='c'):
        self.x = x
        self.y = y
        shadeamnt = 100
        self.color = fill
        self.fill = fill
        self.fillshade = shade(fill,shadeamnt)
        self.note = note

        self.font = "Arial 15 bold"



        self.canvas = Display.canvas # canvas

        self.shift = shift

        self.size = size

        self.defaultSize = 11
        self.adjust = 1
        self.outline = (1 / 6) * self.size

        # coordinates of polygon
        poly_coord = [self.x + (self.size * 1.2),  # lower right
                      self.y + (self.size*self.adjust),

                      self.x,                       # middle bottom
                      self.y + self.size/1.5,

                      self.x - (self.size * 1.2),  # lower left
                      self.y + (self.size*self.adjust),

                      self.x - (self.size / 1.2),  # middle left
                      self.y,

                      self.x - (self.size * 1.2),  # upper left
                      self.y - (self.size*self.adjust),

                      self.x,  # middle top
                      self.y - self.size / 1.5,

                      self.x + (self.size * 1.2),  # upper right
                      self.y - (self.size*self.adjust),
                      self.x + (self.size/1.2),  # middle right
                      self.y,
                      ]

        shade_size = self.size/5
        borderComp = self.outline/2
        highlight_coord = [self.x + (self.size * 1.2) - shade_size - borderComp,  # lower right
                      self.y + (self.size * self.adjust) - shade_size,
                           self.x,                          # middle bottom
                           self.y + self.size/2,

                      self.x - (self.size * 1.2) + borderComp*2,  # lower left
                      self.y + (self.size * self.adjust) - borderComp*2,

                      self.x - (self.size / 2) + borderComp,  # middle left
                      self.y,

                      self.x - (self.size * 1.2) + borderComp,  # upper left
                      self.y - (self.size * self.adjust) + borderComp,

                           self.x,  # middle top
                           self.y - self.size / 2,

                      self.x + (self.size * 1.2) - shade_size - borderComp,  # upper right
                      self.y - (self.size * self.adjust) + borderComp,
                      self.x + (self.size/2) - borderComp ,  # middle right
                      self.y,
                      ]

        self.A = self.canvas.create_polygon(poly_coord, fill=self.fillshade, outline='black', width=self.outline)
        self.B = self.canvas.create_polygon(highlight_coord, fill=fill, outline='', width=self.outline)
        self.text = self.canvas.create_text(self.x, self.y, text=self.note, font=self.font)

        self.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))

    def replaceDot(self, canvas):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.text)


class STAR: ### STAR
    def __init__(self, x, y, note, fill, Display, size=12, shift=0, canvas='c'):
        self.x = x
        self.y = y
        self.true_y = y - size/6 # compensation because Note letter displays offcenter - STAR now rides a bit high
        shadeamnt = 50
        self.color = fill
        self.fill = fill
        self.fillshade = shade(fill,shadeamnt)
        self.note = note

        self.font = "Arial 15 bold"



        self.canvas = Display.canvas # canvas

        self.shift = shift

        self.size = size  ## larger to emphisize ROOT note

        self.defaultSize = 11
        self.adjust = 1
        self.outline = (1 / 6) * self.size

        # coordinates of polygon
        poly_coord = [self.x + (self.size * 1.1),  # lower right
                      self.y + (self.size*self.adjust),

                      self.x,                       # middle bottom
                      self.y + self.size/2,

                      self.x - (self.size * 1.1),  # lower left
                      self.y + (self.size*self.adjust),

                      self.x - (self.size / 1.2),  # middle left
                      self.y,

                      self.x - (self.size * 1.2),  # upper left
                      self.y - (self.size*self.adjust)/1.4,

                      self.x - self.size/2,  # middle inset left
                      self.y - self.size/1.5,

                      self.x,  # middle top
                      self.y - (self.size * 1.5),

                      self.x + self.size / 2,  # middle inset right
                      self.y - self.size/1.5,

                      self.x + (self.size * 1.2),  # upper right
                      self.y - ((self.size*self.adjust)/1.4),


                      self.x + (self.size/1.2),  # middle right
                      self.y,
                      ]

        shade_size = self.size/5
        borderComp = self.outline/2
        highlight_coord = [self.x + (self.size * 1.1) - shade_size - borderComp,  # lower right
                      self.y + (self.size * self.adjust) - shade_size,
                           self.x,                          # middle bottom
                           self.y + self.size/4,

                      self.x - (self.size * 1.1) + borderComp*2,  # lower left
                      self.y + (self.size * self.adjust) - borderComp*2,

                      self.x - (self.size / 1.8) + borderComp,  # middle left
                      self.y,

                      self.x - (self.size * 1.2) + borderComp,  # upper left
                      self.y - (self.size * self.adjust)/1.4 + borderComp,

                           self.x - self.size / 2 + shade_size,  # middle inset left
                           self.y - self.size / 1.4 + shade_size,

                           self.x,  # middle top
                           self.y - self.size*1.2,

                           self.x + self.size / 2 - shade_size ,  # middle inset right
                           self.y - self.size / 1.4 + shade_size,

                      self.x + (self.size * 1.2) - shade_size - borderComp,  # upper right
                      self.y - (self.size * self.adjust)/1.4 + borderComp,
                      self.x + (self.size/1.8) - borderComp ,  # middle right
                      self.y,
                      ]

        self.A = self.canvas.create_polygon(poly_coord, fill=self.fillshade, outline='black', width=self.outline)
        self.B = self.canvas.create_polygon(highlight_coord, fill=fill, outline='', width=self.outline)
        self.text = self.canvas.create_text(self.x, self.true_y, text=self.note, font=self.font, fill = 'black')

        self.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))

    def replaceDot(self, canvas):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.text)


class CIRCLE:
    def __init__(self, x, y, note, fill, Display, size=12, shift=0, canvas='c'):
        self.x = x
        self.y = y
        shadeamnt = 100
        self.color = fill
        self.fill = shade(fill,shadeamnt)
        self.note = note


        self.canvas = Display.canvas # canvas

        self.shift = shift

        self.size = size
        self.font = ''

        if self.color == gray:
            self.font = "Arial 10"
            self.size -= 2

        else:
            self.font = "Arial 15 bold"
        self.defaultSize = 11
        self.adjust = 1.2
        self.outline = (1 / 6) * self.size


        # coordinates of polygon
        poly_coord = [self.x + self.size/self.adjust,  # lower right
                      self.y + self.size/self.adjust,

                      self.x - self.size/self.adjust,  # lower left
                      self.y + self.size/self.adjust,

                      self.x - self.size/self.adjust,  # upper left
                      self.y - self.size/self.adjust,

                      self.x + self.size/self.adjust,  # upper right
                      self.y - self.size/self.adjust,]

        shade_size = self.size/3
        borderComp = self.outline/2
        highlight_coord = [self.x + self.size / self.adjust - shade_size - borderComp,  # lower right
                      self.y + self.size / self.adjust - shade_size - borderComp,

                      self.x - self.size / self.adjust + borderComp - shade_size/2,  # lower left
                      self.y + self.size / self.adjust - shade_size - borderComp,

                      self.x - self.size / self.adjust + borderComp,  # upper left
                      self.y - self.size / self.adjust + borderComp,

                      self.x + self.size / self.adjust - shade_size - borderComp,  # upper right
                      self.y - self.size / self.adjust + borderComp ]

        self.A = self.canvas.create_oval(self.x + self. size, self.y - self.size, self.x - self.size, self.y +self.size, fill=self.fill, outline='black', width=self.outline)
        self.x2 = self.x + borderComp *2
        self.y2 = self.y + borderComp *2

        self.B = self.canvas.create_oval(self.x2 + self.size/2, self.y2 - self.size, self.x2 - self.size, self.y2 +self.size/2, fill=lightn(self.fill, shadeamnt), outline='', width=self.outline)
        self.text = self.canvas.create_text(self.x, self.y, text=self.note, font=self.font)

        self.canvas.tag_bind(self.A, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.B, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', lambda v: Display.ALL(newRoot_Dot=self))

    def replaceDot(self, canvas):
        canvas.delete(self.A)
        canvas.delete(self.B)
        canvas.delete(self.text)

def genShape(x, y, note, fill, Display, size=11, shift=0, canvas='c'):
    if fill == Default_Colors[0] or fill == ColorBlind_Colors[0]:
        return STAR(x, y, note, fill, Display, size, shift, canvas)
    elif fill == Default_Colors[1] or fill == ColorBlind_Colors[1]:
        return CIRCLE(x, y, note, fill, Display, size, shift, canvas)
    elif fill == Default_Colors[2] or fill == ColorBlind_Colors[2]:
        return DIAMOND(x, y, note, fill, Display, size, shift, canvas)

    elif fill == Default_Colors[3]or fill == ColorBlind_Colors[3]:
        return SQUARE(x, y, note, fill, Display, size, shift, canvas)
    else:
        return CIRCLE(x, y, note, fill, Display, size, shift, canvas)

# root = Tk()
#
# canvas = Canvas(root, width = 500, height = 500)
# canvas.pack()
#
#
# x = 250
# y = 100
#
# #c = DIAMOND(x, y, 'C', 'red', canvas, 10)
#
# canvas.create_text(250, 250, text='FUUCK')
#
#
# for i in color_pallet:
#
#     genShape(x,y, 'C#', i, root, 50, 0, canvas)
#     y += 100
#
#
# root.mainloop()
