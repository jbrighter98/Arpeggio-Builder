from tkinter import *
from tkinter import ttk

 
#tutorial = Tk()

toolbar = "Images/toolbar.gif"
chordbuilder = "Images/chordbuilder.gif"
altbuild = "Images/altbuild.gif"
scalebuild = "Images/scalebuild.gif"
helpmenu = "Images/helpmenu.gif"
optionsmenu = "Images/optionsmenu.gif"
tuningmenu = "Images/tuningmenu.gif"
cdotcolorblind = "Images/cdotcolorblind.gif"
cdotdefault = "Images/cdotdefault.gif"
cshapedefault = "Images/cshapedefault.gif"
guitardisplay = "Images/guitardisplay.gif"

def user_tutorial(root):
    tutorial = Toplevel(root)

    tutorial.geometry('1000x550+100+50')
    tutorial.title('Tutorial')

    nbook = ttk.Notebook(tutorial)

    page1 = ttk.Frame(nbook)
    nbook.add(page1, text=' Intro ')
    page2 = ttk.Frame(nbook)
    nbook.add(page2, text=' Toolbar ')
    page3 = ttk.Frame(nbook)
    nbook.add(page3, text='Builder Tab')
    page4 = ttk.Frame(nbook)
    nbook.add(page4, text=' Alternative Build Tab ')
    page5 = ttk.Frame(nbook)
    nbook.add(page5, text=' Scales Tab ')
    page6 = ttk.Frame(nbook)
    nbook.add(page6, text=' Tuning Menu ')
    page7 = ttk.Frame(nbook)
    nbook.add(page7, text=' Options Menu ')
    page8 = ttk.Frame(nbook)
    nbook.add(page8, text=' Help Menu ')
    page9 = ttk.Frame(nbook)
    nbook.add(page9, text=' Chord and Scale Display ')
    nbook.pack(expan = 1, fill = 'both')

    """toolbar.label = "Images/toolbar.gif"
    chordbuilder.label = "Images/chordbuilder.gif"
    altbuild.label = "Images/altbuild.gif"
    scalebuild.label = "Images/scalebuild.gif"
    helpmenu.label = "Images/helpmenu.gif"
    optionsmenu.label = "Images/optionsmenu.gif"
    tuningmenu.label = "Images/tuningmenu.gif"
    cdotcolorblind.label = "Images/cdotcolorblind.gif"
    cdotdefault.label = "Images/cdotdefault.gif"
    cshapedefault.label = "Images/cshapedefault.gif"
    guitardisplay.label = "Images/guitardisplay.gif"""

    labelframe1 = ttk.LabelFrame(page7)
    labelframe1.grid(column=1,row=0,sticky='N')

    labelframe2 = ttk.LabelFrame(page7)
    labelframe2.grid(column=2,row=0,sticky='N')

         
    img1 = PhotoImage(file=toolbar)
    g1 = ttk.Label(page2, image=img1)
    g1.image = img1
    g1.pack(side = 'left')

    img2 = PhotoImage(file=chordbuilder)
    g2 = ttk.Label(page3, image=img2)
    g2.image = img2
    g2.pack(side = 'left')

    img3 = PhotoImage(file=altbuild)
    g3 = ttk.Label(page4, image=img3)
    g3.image = img3
    g3.pack(side = 'left')

    img4 = PhotoImage(file=scalebuild)
    g4 = ttk.Label(page5, image=img4)
    g4.image = img4
    g4.pack(side = 'left')

    img5 = PhotoImage(file=tuningmenu)
    g5 = ttk.Label(page6, image=img5)
    g5.image = img5
    g5.pack(side = 'left')

    img6 = PhotoImage(file=optionsmenu)
    g6 = ttk.Label(labelframe1, image=img6)
    g6.image = img6
    g6.grid(column = 1, row = 1)

    img7 = PhotoImage(file=cdotdefault)
    g7 = ttk.Label(labelframe1, image=img7)
    g7.image = img7
    g7.grid(column = 1, row = 2)

    img8 = PhotoImage(file=cdotcolorblind)
    g8 = ttk.Label(labelframe1, image=img8)
    g8.image = img8
    g8.grid(column = 1, row = 3)

    img9 = PhotoImage(file=cshapedefault)
    g9 = ttk.Label(labelframe1, image=img9)
    g9.image = img9
    g9.grid(column = 1, row = 4)

    img10 = PhotoImage(file=helpmenu)
    g10 = ttk.Label(page8, image=img10)
    g10.image = img10
    g10.pack(side = 'left')

    img11 = PhotoImage(file=guitardisplay)
    g11 = ttk.Label(page9, image=img11)
    g11.image = img11
    g11.pack()


    with open('tutorialtext.txt','r') as help_file:
            lines = help_file.readlines()

    for line1 in lines[:8]:
        line1 = line1.rstrip()
        label1 = ttk.Label(page1, text = line1, font=("Times New Roman", 12, "bold")).pack()

    for line2 in lines[8:27]:
        line2 = line2.rstrip()
        label2 = ttk.Label(page2, text = line2, font=("Times New Roman", 12)).pack()

    for line3 in lines[27:41]:
        line3 = line3.rstrip()
        label3 = ttk.Label(page3, text = line3, font=("Times New Roman", 12)).pack()

    for line4 in lines[41:55]:
        line4 = line4.rstrip()
        label4 = ttk.Label(page4, text = line4, font=("Times New Roman", 12)).pack()

    for line5 in lines[55:69]:
        line5 = line5.rstrip()
        label5 = ttk.Label(page5, text = line5, font=("Times New Roman", 12)).pack()

    for line6 in lines[69:82]:
        line6 = line6.rstrip()
        label6 = ttk.Label(page6, text = line6, font=("Times New Roman", 12)).pack()

    for line7 in lines[82:98]:
        line7 = line7.rstrip()
        label7 = ttk.Label(labelframe2, text = line7, font=("Times New Roman", 12)).pack()

    for line8 in lines[98:109]:
        line8 = line8.rstrip()
        label8 = ttk.Label(page8, text = line8, font=("Times New Roman", 12)).pack()

    for line9 in lines[109:]:
        line9 = line9.rstrip()
        label9 = ttk.Label(page9, text = line9, font=("Times New Roman", 12)).pack()


#tutorial.mainloop()
