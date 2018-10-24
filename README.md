# Arpeggio-Builder
Guitar and Bass Arpeggio Builder

from tkinter import *

class Window(Frame): #this class is the opening window
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Chord and Arpeggio Builder')
        self.pack(fill=BOTH, expand = 1)

        quitButton = Button(self, text = 'Quit', command = self.client_exit)
        quitButton.place(x=180, y=100)

        label1 = Label(text = 'In which key would you like to build?')
        label1.place(x=100,y=10)
        
        v = StringVar()
        entry1 = Entry(textvariable=v)
        entry1.place(x=137,y=40)
        
        #this button sends the input variable to the Build function outside of the class
        gbutton = Button(text='Guitar', command=lambda: BuildGuitar(v.get()))
        gbutton.place(x=158,y=70)
        
        bbutton = Button(text='Bass', command=lambda: BuildBass(v.get()))
        bbutton.place(x=203, y=70)

        conditionline1 = Label(text = 'Example Inputs:')
        conditionline1.place(x=153,y=130)

        conditionline2 = Label(text = 'Amin')
        conditionline2.place(x= 180 , y=150 )

        conditionline3 = Label(text = 'G#maj')
        conditionline3.place(x=177,y=170)

        conditionline4 = Label(text = 'Dbmin')
        conditionline4.place(x=177,y=190)

        conditionline5 = Label(text = '*Use # for sharps and b for flats*')
        conditionline5.place(x=110,y=210)

        
    def client_exit(self):
        exit()
        

def rotate(l):
    lst = l[:]
    return lst[1:]+[lst[0]]

def rotate_to(target, l):
    lst = l[:]

    if target in lst:
        while target != lst[0]:
            lst = rotate(lst)
    return lst


def build_maj_scale(Notes):
    ## build scale using (Notes)
    major_intvl_indx = [0, 2, 4, 5, 7, 9, 11]
    return [Notes[i] for i in major_intvl_indx]
    

def build_min_scale(Notes):
    ## build scale using (self.Notes)
    minor_intvl_indx = [0, 2, 3, 5, 7, 9, 11]
    return [Notes[i] for i in minor_intvl_indx]


        
def BuildGuitar(key):

    """ This mess of a function takes the key input and builds
    the neck window of guitar or displays an error message depending on if
    the input is valid """
    
    labelfont = ("Times", 12, "bold")
    key = key.upper()
    if key != '':
        if key[0] == 'A' or key[0] == 'B' or key[0] == 'C' or key[0] == 'D' or key[0] == 'E' or key[0] == 'F' or key[0] == 'G':
            if key[-3:] == 'MAJ' or key[-3:] == 'MIN' or key[-5:] == 'MAJOR' or key[-5:] == 'MINOR':
                window = Toplevel(root)
                window.geometry('1400x300+50+400')
                window.configure(background='white')
                window.title(key)
                canvas = Canvas(window)

                canvas.create_line(100, 50, 100, 200, width = 3) #frets
                canvas.create_line(200, 50, 200, 200, width = 2)
                canvas.create_line(300, 50, 300, 200, width = 2)
                canvas.create_line(400, 50, 400, 200, width = 2)
                canvas.create_line(500, 50, 500, 200, width = 2)
                canvas.create_line(600, 50, 600, 200, width = 2)
                canvas.create_line(700, 50, 700, 200, width = 2)
                canvas.create_line(800, 50, 800, 200, width = 2)
                canvas.create_line(900, 50, 900, 200, width = 2)
                canvas.create_line(1000, 50, 1000, 200, width = 2)
                canvas.create_line(1100, 50, 1100, 200, width = 2)
                canvas.create_line(1200, 50, 1200, 200, width = 2)
                canvas.create_line(1300, 50, 1300, 200, width = 2)
                
                #dots on frets
                canvas.create_oval(340, 115, 360, 135, outline="black", fill="black", width=2)
                canvas.create_oval(540, 115, 560, 135, outline="black", fill="black", width=2)
                canvas.create_oval(740, 115, 760, 135, outline="black", fill="black", width=2)
                canvas.create_oval(940, 115, 960, 135, outline="black", fill="black", width=2)
                canvas.create_oval(1240, 85, 1260, 105, outline="black", fill="black", width=2)
                canvas.create_oval(1240, 145, 1260, 165, outline="black", fill="black", width=2)

                canvas.create_line(100, 62, 1300, 62, width = 1.5) #strings
                canvas.create_line(100, 87, 1300, 87, width = 2)
                canvas.create_line(100, 112, 1300, 112, width = 2)
                canvas.create_line(100, 137, 1300, 137, width = 2.5)
                canvas.create_line(100, 162, 1300, 162, width = 3)
                canvas.create_line(100, 187, 1300, 187, width = 3)

                canvas.create_rectangle(150, 240, 165, 255, fill='red')
                canvas.create_rectangle(350, 240, 365, 255, fill='yellow')
                canvas.create_rectangle(550, 240, 565, 255, fill='blue')
                canvas.create_rectangle(750, 240, 765, 255, fill='green')
                canvas.create_rectangle(950, 240, 965, 255, fill='gray')
                
                canvas.pack(fill=BOTH, expand=1)
                
                #String labeling
                EString1 = Label(window, text = 'E', font = labelfont).place(x=80,y=176)
                EString2 = Label(window, text = 'E', font = labelfont).place(x=1305,y=176)
                AString1 = Label(window, text = 'A', font = labelfont).place(x=80,y=151)
                AString2 = Label(window, text = 'A', font = labelfont).place(x=1305,y=151)
                DString1 = Label(window, text = 'D', font = labelfont).place(x=80,y=126)
                DString2 = Label(window, text = 'D', font = labelfont).place(x=1305,y=126)
                GString1 = Label(window, text = 'G', font = labelfont).place(x=80,y=101)
                GString2 = Label(window, text = 'G', font = labelfont).place(x=1305,y=101)
                BString1 = Label(window, text = 'B', font = labelfont).place(x=80,y=76)
                BString2 = Label(window, text = 'B', font = labelfont).place(x=1305,y=76)
                eString1 = Label(window, text = 'e', font = ("Times", 14, "bold")).place(x=80,y=47)
                eString2 = Label(window, text = 'e', font = ("Times", 14, "bold")).place(x=1305,y=47)
                print(key)
                
                notekey1 = Label(window, text='Root:', font=('Times', 10, 'bold')).place(x=50,y=240)
                notekey2 = Label(window, text='Third:', font=('Times', 10, 'bold')).place(x=250,y=240)
                notekey3 = Label(window, text='Fifth:', font=('Times', 10, 'bold')).place(x=450,y=240)
                notekey4 = Label(window, text='Seventh:', font=('Times', 10, 'bold')).place(x=650,y=240)
                notekey5 = Label(window, text='Other:', font=('Times', 10, 'bold')).place(x=850,y=240)
            else:
                errorlabel2 = Label(text = 'Please enter a valid Key', fg = 'red')
                errorlabel2.pack()
        else:
            errorlabel1 = Label(text = 'Please enter a valid Key', fg = 'red')
            errorlabel1.pack()
    else:
        errorlabel = Label(text = 'Please enter the Key', fg = 'red')
        errorlabel.pack()


    fillcolor = 'black'

    if key[1] == '#':
        Root = key[0].upper() + key[1]
    elif key[1] == 'B':
        Root = key.upper() + key[1]
    else:
        Root = key[0].upper()
    print(Root)


    SharpNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    FlatNotes =  ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


    Notes = []

    if Root in SharpNotes:
        Notes = SharpNotes[:]
    elif self.Root in FlatNotes:
        Notes = FlatNotes[:]
    else:
        print('Invalid Tonic')


    if Notes[0] != Root:
        Notes = rotate_to(Root, Notes)
        

    MajScale = build_maj_scale(Notes)
    MinScale = build_min_scale(Notes)
    #self.chord_names = self.build_chord_names()

    # [0, 2, 4, 5, 7, 9, 11]
    

    if key[-3:] == 'MAJ' or key[-5:] == 'MAJOR':
        majcount = 1
        for itemsmaj in MajScale:

            if majcount == 1:
                fillcolor = 'red'
            elif majcount == 3:
                fillcolor = 'yellow'
            elif majcount == 5:
                fillcolor = 'blue'
            elif majcount == 7:
                fillcolor = 'green'
            else:
                fillcolor = 'gray'

            if itemsmaj == 'A':
                ca = Canvas(window)
                canvas.create_oval(545, 182, 555, 192, fill = fillcolor)
                canvas.create_oval(45, 157, 55, 167, fill = fillcolor)
                canvas.create_oval(1245, 157, 1255, 167, fill = fillcolor)
                canvas.create_oval(745, 132, 755, 142, fill = fillcolor)
                canvas.create_oval(245, 107, 255, 117, fill = fillcolor)
                canvas.create_oval(1045, 82, 1055, 92, fill = fillcolor)
                canvas.create_oval(545, 57, 555, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
                
            elif itemsmaj == 'A#' or itemsmaj =='BB':
                ca = Canvas(window)
                canvas.create_oval(645, 182, 655, 192, fill = fillcolor)
                canvas.create_oval(145, 157, 155, 167, fill = fillcolor)
                canvas.create_oval(845, 132, 855, 142, fill = fillcolor)
                canvas.create_oval(345, 107, 355, 117, fill = fillcolor)
                canvas.create_oval(1145, 82, 1155, 92, fill = fillcolor)
                canvas.create_oval(645, 57, 655, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'B':
                ca = Canvas(window)
                canvas.create_oval(745, 182, 755, 192, fill = fillcolor)
                canvas.create_oval(245, 157, 255, 167, fill = fillcolor)
                canvas.create_oval(945, 132, 955, 142, fill = fillcolor)
                canvas.create_oval(445, 107, 455, 117, fill = fillcolor)
                canvas.create_oval(45, 82, 55, 92, fill = fillcolor)
                canvas.create_oval(1245, 82, 1255, 92, fill = fillcolor)
                canvas.create_oval(745, 57, 755, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'C':
                ca = Canvas(window)
                canvas.create_oval(845, 182, 855, 192, fill = fillcolor)
                canvas.create_oval(345, 157, 355, 167, fill = fillcolor)
                canvas.create_oval(1045, 132, 1055, 142, fill = fillcolor)
                canvas.create_oval(545, 107, 555, 117, fill = fillcolor)
                canvas.create_oval(145, 82, 155, 92, fill = fillcolor)
                canvas.create_oval(845, 57, 855, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'C#' or itemsmaj == 'DB':
                ca = Canvas(window)
                canvas.create_oval(945, 182, 955, 192, fill = fillcolor)
                canvas.create_oval(445, 157, 455, 167, fill = fillcolor)
                canvas.create_oval(1145, 132, 1155, 142, fill = fillcolor)
                canvas.create_oval(645, 107, 655, 117, fill = fillcolor)
                canvas.create_oval(245, 82, 255, 92, fill = fillcolor)
                canvas.create_oval(945, 57, 955, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'D':
                ca = Canvas(window)
                canvas.create_oval(1045, 182, 1055, 192, fill = fillcolor)
                canvas.create_oval(545, 157, 555, 167, fill = fillcolor)
                canvas.create_oval(45, 132, 55, 142, fill = fillcolor)
                canvas.create_oval(1245, 132, 1255, 142, fill = fillcolor)
                canvas.create_oval(745, 107, 755, 117, fill = fillcolor)
                canvas.create_oval(345, 82, 355, 92, fill = fillcolor)
                canvas.create_oval(1045, 57, 1055, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'D#' or itemsmaj == 'EB':
                ca = Canvas(window)
                canvas.create_oval(1145, 182, 1155, 192, fill = fillcolor)
                canvas.create_oval(645, 157, 655, 167, fill = fillcolor)
                canvas.create_oval(145, 132, 155, 142, fill = fillcolor)
                canvas.create_oval(845, 107, 855, 117, fill = fillcolor)
                canvas.create_oval(445, 82, 455, 92, fill = fillcolor)
                canvas.create_oval(1145, 57, 1155, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'E':
                ca = Canvas(window)
                canvas.create_oval(45, 182, 55, 192, fill = fillcolor)
                canvas.create_oval(1245, 182, 1255, 192, fill = fillcolor)
                canvas.create_oval(745, 157, 755, 167, fill = fillcolor)
                canvas.create_oval(245, 132, 255, 142, fill = fillcolor)
                canvas.create_oval(945, 107, 955, 117, fill = fillcolor)
                canvas.create_oval(545, 82, 555, 92, fill = fillcolor)
                canvas.create_oval(45, 57, 55, 67, fill = fillcolor)
                canvas.create_oval(1245, 57, 1255, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'F':
                ca = Canvas(window)
                canvas.create_oval(145, 182, 155, 192, fill = fillcolor)
                canvas.create_oval(845, 157, 855, 167, fill = fillcolor)
                canvas.create_oval(345, 132, 355, 142, fill = fillcolor)
                canvas.create_oval(1045, 107, 1055, 117, fill = fillcolor)
                canvas.create_oval(645, 82, 655, 92, fill = fillcolor)
                canvas.create_oval(145, 57, 155, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'F#' or itemsmaj == 'GB':
                ca = Canvas(window)
                canvas.create_oval(245, 182, 255, 192, fill = fillcolor)
                canvas.create_oval(945, 157, 955, 167, fill = fillcolor)
                canvas.create_oval(445, 132, 455, 142, fill = fillcolor)
                canvas.create_oval(1145, 107, 1155, 117, fill = fillcolor)
                canvas.create_oval(745, 82, 755, 92, fill = fillcolor)
                canvas.create_oval(245, 57, 255, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'G':
                ca = Canvas(window)
                canvas.create_oval(345, 182, 355, 192, fill = fillcolor)
                canvas.create_oval(1045, 157, 1055, 167, fill = fillcolor)
                canvas.create_oval(545, 132, 555, 142, fill = fillcolor)
                canvas.create_oval(45, 107, 55, 117, fill = fillcolor)
                canvas.create_oval(1245, 107, 1255, 117, fill = fillcolor)
                canvas.create_oval(845, 82, 855, 92, fill = fillcolor)
                canvas.create_oval(345, 57, 355, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'G#' or itemsmaj == 'AB':
                ca = Canvas(window)
                canvas.create_oval(445, 182, 455, 192, fill = fillcolor)
                canvas.create_oval(1145, 157, 1155, 167, fill = fillcolor)
                canvas.create_oval(645, 132, 655, 142, fill = fillcolor)
                canvas.create_oval(145, 107, 155, 117, fill = fillcolor)
                canvas.create_oval(945, 82, 955, 92, fill = fillcolor)
                canvas.create_oval(445, 57, 455, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)

            majcount+=1




    elif key[-3:] == 'MIN' or key[-5:] == 'MINOR':
        mincount = 1
        for itemsmin in MinScale:

            if mincount == 1:
                fillcolor = 'red'
            elif mincount == 3:
                fillcolor = 'yellow'
            elif mincount == 5:
                fillcolor = 'blue'
            elif mincount == 7:
                fillcolor = 'green'
            else:
                fillcolor = 'gray'
            
            if itemsmin == 'A':
                ca = Canvas(window)
                canvas.create_oval(545, 182, 555, 192, fill = fillcolor)
                canvas.create_oval(45, 157, 55, 167, fill = fillcolor)
                canvas.create_oval(1245, 157, 1255, 167, fill = fillcolor)
                canvas.create_oval(745, 132, 755, 142, fill = fillcolor)
                canvas.create_oval(245, 107, 255, 117, fill = fillcolor)
                canvas.create_oval(1045, 82, 1055, 92, fill = fillcolor)
                canvas.create_oval(545, 57, 555, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
                
            elif itemsmin == 'A#' or itemsmin =='BB':
                ca = Canvas(window)
                canvas.create_oval(645, 182, 655, 192, fill = fillcolor)
                canvas.create_oval(145, 157, 155, 167, fill = fillcolor)
                canvas.create_oval(845, 132, 855, 142, fill = fillcolor)
                canvas.create_oval(345, 107, 355, 117, fill = fillcolor)
                canvas.create_oval(1145, 82, 1155, 92, fill = fillcolor)
                canvas.create_oval(645, 57, 655, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'B':
                ca = Canvas(window)
                canvas.create_oval(745, 182, 755, 192, fill = fillcolor)
                canvas.create_oval(245, 157, 255, 167, fill = fillcolor)
                canvas.create_oval(945, 132, 955, 142, fill = fillcolor)
                canvas.create_oval(445, 107, 455, 117, fill = fillcolor)
                canvas.create_oval(45, 82, 55, 92, fill = fillcolor)
                canvas.create_oval(1245, 82, 1255, 92, fill = fillcolor)
                canvas.create_oval(745, 57, 755, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'C':
                ca = Canvas(window)
                canvas.create_oval(845, 182, 855, 192, fill = fillcolor)
                canvas.create_oval(345, 157, 355, 167, fill = fillcolor)
                canvas.create_oval(1045, 132, 1055, 142, fill = fillcolor)
                canvas.create_oval(545, 107, 555, 117, fill = fillcolor)
                canvas.create_oval(145, 82, 155, 92, fill = fillcolor)
                canvas.create_oval(845, 57, 855, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'C#' or itemsmin == 'DB':
                ca = Canvas(window)
                canvas.create_oval(945, 182, 955, 192, fill = fillcolor)
                canvas.create_oval(445, 157, 455, 167, fill = fillcolor)
                canvas.create_oval(1145, 132, 1155, 142, fill = fillcolor)
                canvas.create_oval(645, 107, 655, 117, fill = fillcolor)
                canvas.create_oval(245, 82, 255, 92, fill = fillcolor)
                canvas.create_oval(945, 57, 955, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'D':
                ca = Canvas(window)
                canvas.create_oval(1045, 182, 1055, 192, fill = fillcolor)
                canvas.create_oval(545, 157, 555, 167, fill = fillcolor)
                canvas.create_oval(45, 132, 55, 142, fill = fillcolor)
                canvas.create_oval(1245, 132, 1255, 142, fill = fillcolor)
                canvas.create_oval(745, 107, 755, 117, fill = fillcolor)
                canvas.create_oval(345, 82, 355, 92, fill = fillcolor)
                canvas.create_oval(1045, 57, 1055, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'D#' or itemsmin == 'EB':
                ca = Canvas(window)
                canvas.create_oval(1145, 182, 1155, 192, fill = fillcolor)
                canvas.create_oval(645, 157, 655, 167, fill = fillcolor)
                canvas.create_oval(145, 132, 155, 142, fill = fillcolor)
                canvas.create_oval(845, 107, 855, 117, fill = fillcolor)
                canvas.create_oval(445, 82, 455, 92, fill = fillcolor)
                canvas.create_oval(1145, 57, 1155, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'E':
                ca = Canvas(window)
                canvas.create_oval(45, 182, 55, 192, fill = fillcolor)
                canvas.create_oval(1245, 182, 1255, 192, fill = fillcolor)
                canvas.create_oval(745, 157, 755, 167, fill = fillcolor)
                canvas.create_oval(245, 132, 255, 142, fill = fillcolor)
                canvas.create_oval(945, 107, 955, 117, fill = fillcolor)
                canvas.create_oval(545, 82, 555, 92, fill = fillcolor)
                canvas.create_oval(45, 57, 55, 67, fill = fillcolor)
                canvas.create_oval(1245, 57, 1255, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'F':
                ca = Canvas(window)
                canvas.create_oval(145, 182, 155, 192, fill = fillcolor)
                canvas.create_oval(845, 157, 855, 167, fill = fillcolor)
                canvas.create_oval(345, 132, 355, 142, fill = fillcolor)
                canvas.create_oval(1045, 107, 1055, 117, fill = fillcolor)
                canvas.create_oval(645, 82, 655, 92, fill = fillcolor)
                canvas.create_oval(145, 57, 155, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'F#' or itemsmin == 'GB':
                ca = Canvas(window)
                canvas.create_oval(245, 182, 255, 192, fill = fillcolor)
                canvas.create_oval(945, 157, 955, 167, fill = fillcolor)
                canvas.create_oval(445, 132, 455, 142, fill = fillcolor)
                canvas.create_oval(1145, 107, 1155, 117, fill = fillcolor)
                canvas.create_oval(745, 82, 755, 92, fill = fillcolor)
                canvas.create_oval(245, 57, 255, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'G':
                ca = Canvas(window)
                canvas.create_oval(345, 182, 355, 192, fill = fillcolor)
                canvas.create_oval(1045, 157, 1055, 167, fill = fillcolor)
                canvas.create_oval(545, 132, 555, 142, fill = fillcolor)
                canvas.create_oval(45, 107, 55, 117, fill = fillcolor)
                canvas.create_oval(1245, 107, 1255, 117, fill = fillcolor)
                canvas.create_oval(845, 82, 855, 92, fill = fillcolor)
                canvas.create_oval(345, 57, 355, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'G#' or itemsmin == 'AB':
                ca = Canvas(window)
                canvas.create_oval(445, 182, 455, 192, fill = fillcolor)
                canvas.create_oval(1145, 157, 1155, 167, fill = fillcolor)
                canvas.create_oval(645, 132, 655, 142, fill = fillcolor)
                canvas.create_oval(145, 107, 155, 117, fill = fillcolor)
                canvas.create_oval(945, 82, 955, 92, fill = fillcolor)
                canvas.create_oval(445, 57, 455, 67, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)

            mincount+=1
        












def BuildBass(key):

    """ This mess of a function takes the key input and builds
    the neck window of bass or displays an error message depending on if
    the input is valid """
    
    labelfont = ("Times", 12, "bold")
    key = key.upper()
    if key != '':
        if key[0] == 'A' or key[0] == 'B' or key[0] == 'C' or key[0] == 'D' or key[0] == 'E' or key[0] == 'F' or key[0] == 'G':
            window = Toplevel(root)
            window.geometry('1400x300+50+400')
            window.configure(background='white')
            window.title(key)
            canvas = Canvas(window)

            canvas.create_line(100, 50, 100, 200, width = 3) #frets
            canvas.create_line(200, 50, 200, 200, width = 2)
            canvas.create_line(300, 50, 300, 200, width = 2)
            canvas.create_line(400, 50, 400, 200, width = 2)
            canvas.create_line(500, 50, 500, 200, width = 2)
            canvas.create_line(600, 50, 600, 200, width = 2)
            canvas.create_line(700, 50, 700, 200, width = 2)
            canvas.create_line(800, 50, 800, 200, width = 2)
            canvas.create_line(900, 50, 900, 200, width = 2)
            canvas.create_line(1000, 50, 1000, 200, width = 2)
            canvas.create_line(1100, 50, 1100, 200, width = 2)
            canvas.create_line(1200, 50, 1200, 200, width = 2)
            canvas.create_line(1300, 50, 1300, 200, width = 2)
            
            #dots on frets
            canvas.create_oval(340, 115, 360, 135, outline="black", fill="black", width=2)
            canvas.create_oval(540, 115, 560, 135, outline="black", fill="black", width=2)
            canvas.create_oval(740, 115, 760, 135, outline="black", fill="black", width=2)
            canvas.create_oval(940, 115, 960, 135, outline="black", fill="black", width=2)
            canvas.create_oval(1240, 85, 1260, 105, outline="black", fill="black", width=2)
            canvas.create_oval(1240, 145, 1260, 165, outline="black", fill="black", width=2)


            canvas.create_line(100, 65, 1300, 65, width = 3) #strings
            canvas.create_line(100, 105, 1300, 105, width = 3)
            canvas.create_line(100, 145, 1300, 145, width = 4)
            canvas.create_line(100, 185, 1300, 185, width = 4)

            canvas.create_rectangle(150, 240, 165, 255, fill='red')
            canvas.create_rectangle(350, 240, 365, 255, fill='yellow')
            canvas.create_rectangle(550, 240, 565, 255, fill='blue')
            canvas.create_rectangle(750, 240, 765, 255, fill='green')
            canvas.create_rectangle(950, 240, 965, 255, fill='gray')
            
            canvas.pack(fill=BOTH, expand=1)
            
            #String labeling
            EString1 = Label(window, text = 'E', font = labelfont).place(x=80,y=173)
            EString2 = Label(window, text = 'E', font = labelfont).place(x=1305,y=173)
            AString1 = Label(window, text = 'A', font = labelfont).place(x=80,y=133)
            AString2 = Label(window, text = 'A', font = labelfont).place(x=1305,y=133)
            DString1 = Label(window, text = 'D', font = labelfont).place(x=80,y=92)
            DString2 = Label(window, text = 'D', font = labelfont).place(x=1305,y=92)
            GString1 = Label(window, text = 'G', font = labelfont).place(x=80,y=53)
            GString2 = Label(window, text = 'G', font = labelfont).place(x=1305,y=53)
            
            print(key)

            notekey1 = Label(window, text='Root:', font=('Times', 10, 'bold')).place(x=50,y=240)
            notekey2 = Label(window, text='Third:', font=('Times', 10, 'bold')).place(x=250,y=240)
            notekey3 = Label(window, text='Fifth:', font=('Times', 10, 'bold')).place(x=450,y=240)
            notekey4 = Label(window, text='Seventh:', font=('Times', 10, 'bold')).place(x=650,y=240)
            notekey5 = Label(window, text='Other:', font=('Times', 10, 'bold')).place(x=850,y=240)
            
        else:
            errorlabel1 = Label(text = 'Please enter a valid Key', fg = 'red')
            errorlabel1.pack()
    else:
        errorlabel = Label(text = 'Please enter the Key', fg = 'red')
        errorlabel.pack()


    


    
    fillcolor = 'black'

    if key[1] == '#':
        Root = key[0].upper() + key[1]
    elif key[1] == 'B':
        Root = key.upper() + key[1]
    else:
        Root = key[0].upper()
    print(Root)


    SharpNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    FlatNotes =  ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


    Notes = []

    if Root in SharpNotes:
        Notes = SharpNotes[:]
    elif self.Root in FlatNotes:
        Notes = FlatNotes[:]
    else:
        print('Invalid Tonic')


    if Notes[0] != Root:
        Notes = rotate_to(Root, Notes)
        

    MajScale = build_maj_scale(Notes)
    MinScale = build_min_scale(Notes)
    #self.chord_names = self.build_chord_names()

    # [0, 2, 4, 5, 7, 9, 11]

    if key[-3:] == 'MAJ' or key[-5:] == 'MAJOR':
        majcount = 1
        for itemsmaj in MajScale:

            if majcount == 1:
                fillcolor = 'red'
            elif majcount == 3:
                fillcolor = 'yellow'
            elif majcount == 5:
                fillcolor = 'blue'
            elif majcount == 7:
                fillcolor = 'green'
            else:
                fillcolor = 'gray'
            
            if itemsmaj == 'A':
                ca = Canvas(window)
                canvas.create_oval(545, 180, 555, 190, fill = fillcolor)
                canvas.create_oval(45, 140, 55, 150, fill = fillcolor)
                canvas.create_oval(1245, 140, 1255, 150, fill = fillcolor)
                canvas.create_oval(745, 100, 755, 110, fill = fillcolor)
                canvas.create_oval(245, 60, 255, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
                
            elif itemsmaj == 'A#' or itemsmaj =='BB':
                ca = Canvas(window)
                canvas.create_oval(645, 180, 655, 190, fill = fillcolor)
                canvas.create_oval(145, 140, 155, 150, fill = fillcolor)
                canvas.create_oval(845, 100, 855, 110, fill = fillcolor)
                canvas.create_oval(345, 60, 355, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'B':
                ca = Canvas(window)
                canvas.create_oval(745, 180, 755, 190, fill = fillcolor)
                canvas.create_oval(245, 140, 255, 150, fill = fillcolor)
                canvas.create_oval(945, 100, 955, 110, fill = fillcolor)
                canvas.create_oval(445, 60, 455, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'C':
                ca = Canvas(window)
                canvas.create_oval(845, 180, 855, 190, fill = fillcolor)
                canvas.create_oval(345, 140, 355, 150, fill = fillcolor)
                canvas.create_oval(1045, 100, 1055, 110, fill = fillcolor)
                canvas.create_oval(545, 60, 555, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'C#' or itemsmaj == 'DB':
                ca = Canvas(window)
                canvas.create_oval(945, 180, 955, 190, fill = fillcolor)
                canvas.create_oval(445, 140, 455, 150, fill = fillcolor)
                canvas.create_oval(1145, 100, 1155, 110, fill = fillcolor)
                canvas.create_oval(645, 60, 655, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'D':
                ca = Canvas(window)
                canvas.create_oval(1045, 180, 1055, 190, fill = fillcolor)
                canvas.create_oval(545, 140, 555, 150, fill = fillcolor)
                canvas.create_oval(45, 100, 55, 110, fill = fillcolor)
                canvas.create_oval(1245, 100, 1255, 110, fill = fillcolor)
                canvas.create_oval(745, 60, 755, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'D#' or itemsmaj == 'EB':
                ca = Canvas(window)
                canvas.create_oval(1145, 180, 1155, 190, fill = fillcolor)
                canvas.create_oval(645, 140, 655, 150, fill = fillcolor)
                canvas.create_oval(145, 100, 155, 110, fill = fillcolor)
                canvas.create_oval(845, 60, 855, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'E':
                ca = Canvas(window)
                canvas.create_oval(45, 180, 55, 190, fill = fillcolor)
                canvas.create_oval(1245, 180, 1255, 190, fill = fillcolor)
                canvas.create_oval(745, 140, 755, 150, fill = fillcolor)
                canvas.create_oval(245, 100, 255, 110, fill = fillcolor)
                canvas.create_oval(945, 60, 955, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'F':
                ca = Canvas(window)
                canvas.create_oval(145, 180, 155, 190, fill = fillcolor)
                canvas.create_oval(845, 140, 855, 150, fill = fillcolor)
                canvas.create_oval(345, 100, 355, 110, fill = fillcolor)
                canvas.create_oval(1045, 60, 1055, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'F#' or itemsmaj == 'GB':
                ca = Canvas(window)
                canvas.create_oval(245, 180, 255, 190, fill = fillcolor)
                canvas.create_oval(945, 140, 955, 150, fill = fillcolor)
                canvas.create_oval(445, 100, 455, 110, fill = fillcolor)
                canvas.create_oval(1145, 60, 1155, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'G':
                ca = Canvas(window)
                canvas.create_oval(345, 180, 355, 190, fill = fillcolor)
                canvas.create_oval(1045, 140, 1055, 150, fill = fillcolor)
                canvas.create_oval(545, 100, 555, 110, fill = fillcolor)
                canvas.create_oval(45, 60, 55, 70, fill = fillcolor)
                canvas.create_oval(1245, 60, 1255, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmaj == 'G#' or itemsmaj == 'AB':
                ca = Canvas(window)
                canvas.create_oval(445, 180, 455, 190, fill = fillcolor)
                canvas.create_oval(1145, 140, 1155, 150, fill = fillcolor)
                canvas.create_oval(645, 100, 655, 110, fill = fillcolor)
                canvas.create_oval(145, 60, 155, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)

            majcount+=1






    elif key[-3:] == 'MIN' or key[-5:] == 'MINOR':
        mincount = 1
        for itemsmin in MinScale:

            if mincount == 1:
                fillcolor = 'red'
            elif mincount == 3:
                fillcolor = 'yellow'
            elif mincount == 5:
                fillcolor = 'blue'
            elif mincount == 7:
                fillcolor = 'green'
            else:
                fillcolor = 'gray'
            
            if itemsmin == 'A':
                ca = Canvas(window)
                canvas.create_oval(545, 180, 555, 190, fill = fillcolor)
                canvas.create_oval(45, 140, 55, 150, fill = fillcolor)
                canvas.create_oval(1245, 140, 1255, 150, fill = fillcolor)
                canvas.create_oval(745, 100, 755, 110, fill = fillcolor)
                canvas.create_oval(245, 60, 255, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
                
            elif itemsmin == 'A#' or itemsmin =='BB':
                ca = Canvas(window)
                canvas.create_oval(645, 180, 655, 190, fill = fillcolor)
                canvas.create_oval(145, 140, 155, 150, fill = fillcolor)
                canvas.create_oval(845, 100, 855, 110, fill = fillcolor)
                canvas.create_oval(345, 60, 355, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'B':
                ca = Canvas(window)
                canvas.create_oval(745, 180, 755, 190, fill = fillcolor)
                canvas.create_oval(245, 140, 255, 150, fill = fillcolor)
                canvas.create_oval(945, 100, 955, 110, fill = fillcolor)
                canvas.create_oval(445, 60, 455, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'C':
                ca = Canvas(window)
                canvas.create_oval(845, 180, 855, 190, fill = fillcolor)
                canvas.create_oval(345, 140, 355, 150, fill = fillcolor)
                canvas.create_oval(1045, 100, 1055, 110, fill = fillcolor)
                canvas.create_oval(545, 60, 555, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'C#' or itemsmin == 'DB':
                ca = Canvas(window)
                canvas.create_oval(945, 180, 955, 190, fill = fillcolor)
                canvas.create_oval(445, 140, 455, 150, fill = fillcolor)
                canvas.create_oval(1145, 100, 1155, 110, fill = fillcolor)
                canvas.create_oval(645, 60, 655, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'D':
                ca = Canvas(window)
                canvas.create_oval(1045, 180, 1055, 190, fill = fillcolor)
                canvas.create_oval(545, 140, 555, 150, fill = fillcolor)
                canvas.create_oval(45, 100, 55, 110, fill = fillcolor)
                canvas.create_oval(1245, 100, 1255, 110, fill = fillcolor)
                canvas.create_oval(745, 60, 755, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'D#' or itemsmin == 'EB':
                ca = Canvas(window)
                canvas.create_oval(1145, 180, 1155, 190, fill = fillcolor)
                canvas.create_oval(645, 140, 655, 150, fill = fillcolor)
                canvas.create_oval(145, 100, 155, 110, fill = fillcolor)
                canvas.create_oval(845, 60, 855, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'E':
                ca = Canvas(window)
                canvas.create_oval(45, 180, 55, 190, fill = fillcolor)
                canvas.create_oval(1245, 180, 1255, 190, fill = fillcolor)
                canvas.create_oval(745, 140, 755, 150, fill = fillcolor)
                canvas.create_oval(245, 100, 255, 110, fill = fillcolor)
                canvas.create_oval(945, 60, 955, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'F':
                ca = Canvas(window)
                canvas.create_oval(145, 180, 155, 190, fill = fillcolor)
                canvas.create_oval(845, 140, 855, 150, fill = fillcolor)
                canvas.create_oval(345, 100, 355, 110, fill = fillcolor)
                canvas.create_oval(1045, 60, 1055, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'F#' or itemsmin == 'GB':
                ca = Canvas(window)
                canvas.create_oval(245, 180, 255, 190, fill = fillcolor)
                canvas.create_oval(945, 140, 955, 150, fill = fillcolor)
                canvas.create_oval(445, 100, 455, 110, fill = fillcolor)
                canvas.create_oval(1145, 60, 1155, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'G':
                ca = Canvas(window)
                canvas.create_oval(345, 180, 355, 190, fill = fillcolor)
                canvas.create_oval(1045, 140, 1055, 150, fill = fillcolor)
                canvas.create_oval(545, 100, 555, 110, fill = fillcolor)
                canvas.create_oval(45, 60, 55, 70, fill = fillcolor)
                canvas.create_oval(1245, 60, 1255, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)
    
            elif itemsmin == 'G#' or itemsmin == 'AB':
                ca = Canvas(window)
                canvas.create_oval(445, 180, 455, 190, fill = fillcolor)
                canvas.create_oval(1145, 140, 1155, 150, fill = fillcolor)
                canvas.create_oval(645, 100, 655, 110, fill = fillcolor)
                canvas.create_oval(145, 60, 155, 70, fill = fillcolor)
                ca.pack(fill=BOTH, expand=1)

            mincount+=1



root = Tk()
root.geometry('400x300+50+50')

app = Window(root)

root.mainloop()
