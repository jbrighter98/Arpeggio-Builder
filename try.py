import webbrowser
from tkinter import *
from tkinter import ttk

from CONSTANTS import *
from virtualneck import Neck
from buildArp import parse, buildMode
from Display import *
from tutorial import *

DefaultTuning = ['E', 'A', 'D', 'G', 'B', 'E'] # SLOPPY SLOPPY SLOPPY
# called as - global - in retune() and other functions,
# theres absolutely a better way to do this


class Window(Frame):   # this class is the opening window
    def __init__(self, master = None):
        import CONSTANTS

        self.color_pallet = CONSTANTS.Default_Colors[:]

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        self.ColorBlind = False
        self.DotMode = True

    def changeToDefaultColor(self):
        self.ColorBlind = False
    def changeToColorBlind(self):
        self.ColorBlind = True

    def changeToDots(self):
        self.DotMode = True
        # print(self.DotMode)
    def changeToShapes(self):
        self.DotMode = False
        # print(self.DotMode)

    def init_window(self):
        global DefaultTuning

        self.master.title('Chord and Arpeggio Builder')

        nb = ttk.Notebook(root)

        self.page1 = ttk.Frame(nb)
        nb.add(self.page1, text='Builder')
        self.page2 = ttk.Frame(nb)
        nb.add(self.page2, text='Alternative Build')
        self.page3 = ttk.Frame(nb)

        nb.add(self.page3, text='Scales')
        nb.pack(expan = 1, fill = 'both')

        # ##### DONT KNOW WHERE TO PUT BELOW IN ADDWIDGIT

        note_choices = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        note_var = StringVar(self.page3)
        note_var.set('C')
        notes_Menu = ttk.OptionMenu(self.page3, note_var, *note_choices)
        notes_Menu.pack()

        mode_choices = [ 'Ionian (major)',
                         'Dorian',
                         'Phrygian',
                         'Lydian',
                         'Mixolydian',
                         'Aeolian (minor)',
                         'Locrian',
                         'Harmonic minor'
                         ]
        mode_var = StringVar(self.page3)
        mode_var.set('Ionian (major)')
        modes_Menu = ttk.OptionMenu(self.page3, mode_var, *mode_choices)
        modes_Menu.pack()

        GorB = [['Guitar', 6], ['Bass', 4], ["5 String", 5]]
        GBV = IntVar()
        GBV.set(6)

        for GorBname,val_GB in GorB:
            ttk.Radiobutton(self.page3, text = GorBname, variable = GBV, value = val_GB).pack()


        but = ttk.Button(self.page3, text='Build',
                     command=lambda: Display(getModeInput(),
                                             window_root= self,
                                            numOfStrings = GBV.get(),

                                            searchNotes = buildMode(note_var.get(), mode_var.get()),
                                             tuning= DefaultTuning,
                                             colorBlindMode= self.ColorBlind,
                                             DotMode = self.DotMode,
                                             mode = mode_var.get()))
        but.pack()

        spacelab = ttk.Label(text = ' ')
        spacelab.pack()

        quitBut = ttk.Button(self.page3, text = 'Quit', command = self.client_exit)
        quitBut.pack()



        ###################### CASCADING MENUS #############################
        def donothing():
            print('not doing it.')

        def tuningMenu():
            windowWidth = 150
            windowHeight = 425

            tune_window = Toplevel(
                root)  ### <<----------------------------------------------- links window to ROOT app frame
            tune_window.geometry(str(windowWidth) + 'x' + str(windowHeight) + '+500+50')
            tune_window.configure(background='white')
            tune_window.title('Tuning')

            menus = []
            selections = []

            def create_dropdown():

                x = 10
                spacing = (windowHeight - 30) / 6
                newTuning = []

                Tuning = DefaultTuning[:]
                Tuning.reverse()

                for note in Tuning:

                    note_choices = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
                    while note != note_choices[0]:
                        note_choices = note_choices[1:] + [note_choices[0]]

                    note_var = StringVar(tune_window)
                    note_var.set(note_choices[0])
                    notes_Menu = ttk.OptionMenu(tune_window, note_var, *note_choices)
                    notes_Menu.config(width=8)
                    notes_Menu.place(x=10, y=x)
                    menus.append(notes_Menu)
                    selections.append(note_var)
                    x += spacing

            def savetuningwindow():

                savtunwind = Toplevel(root)
                savtunwind.geometry('250x100+500+50')
                savtunwind.title('Save Tuning')

                question = Label(savtunwind, text='What would you like to call this tuning?')
                question.pack()

                name = StringVar()

                ques_entry = ttk.Entry(savtunwind, textvariable=name)
                ques_entry.pack()

                space1 = ttk.Label(savtunwind, text=' ')
                space1.pack()

                savebutton = ttk.Button(savtunwind, text='Save', command=lambda: savetuning(name.get()))
                savebutton.pack()

                def savetuning(tuningname):
                    tempnotestring = ""

                    with open('savedtuningnames.txt', 'a+') as tune_names:
                        tune_names.write(tuningname + '\n')

                    for items in DefaultTuning:
                        tempnotestring += items

                    with open('savedtuningnotes.txt', 'a+') as tune_notes:
                        tune_notes.write(tempnotestring + '\n')

                    filemenu.add_command(label=tuningname, command=lambda: self.open_tuning(tuningname))
                    root.update()

                    savtunwind.destroy()
                    tune_window.destroy()

            def retune():
                global DefaultTuning
                outp = []
                for note in selections:
                    outp.append(note.get())
                outp.reverse()

                # print(outp)

                DefaultTuning = outp[:]

                savebutton1 = ttk.Button(tune_window, text='Save Custom Tuning',
                                         command=savetuningwindow)
                savebutton1.place(x=windowWidth / 2, y=windowHeight - 15, anchor='center')
                return outp

            create_dropdown()

            tuneButton = ttk.Button(tune_window, text='Tune', command=retune)
            tuneButton.place(x=windowWidth / 2, y=windowHeight - 45, anchor='center')

            """savebutton1 = ttk.Button(tune_window, text = 'Save Custom Tuning',
                                     command = savetuningwindow)
            savebutton1.place(x = windowWidth/2, y = windowHeight-15, anchor = 'center')"""

        def standardTuning():
            global DefaultTuning

            DefaultTuning = ['E','A','D','G','B','E']

        def DropDTuning():
            global DefaultTuning

            DefaultTuning = ['D', 'A', 'D', 'G', 'B', 'E']

        def fiveStringB():
            global DefaultTuning

            DefaultTuning = ['B','E','A','D','G','C']

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=1, title = 'Tune')
        choicesMenu = Menu(menubar, tearoff = 1)

        icount = 0


        filemenu.add_command(label="Custom...", command=tuningMenu)

        def ifdeletecustom():

            with open("savedtuningnames.txt", "r") as AA:
                x = AA.readlines()

            if x == []:
                errormessage()
            else:
                deletecustom()

        def errormessage():

            def killerrormessage():
                errorwind.destroy()

            errorwind = Toplevel(root)
            errorwind.geometry('300x50+500+50')
            errorwind.title('Notice')

            error = ttk.Label(errorwind, text='You have no saved custom tunings.')
            error.pack()

            okbutton = ttk.Button(errorwind, text='Ok', command=killerrormessage)
            okbutton.pack()

        def deletecustom():

            def del_cust(vv):

                with open("savedtuningnames.txt", "r") as B:
                    xx = B.readlines()

                deletedname = t[vv] + '\n'
                deletednotes = xx[vv]

                with open("savedtuningnames.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != deletedname:
                            f.write(i)
                    f.truncate()

                with open("savedtuningnotes.txt", "r+") as fx:
                    dx = fx.readlines()
                    fx.seek(0)
                    for ix in dx:
                        if i != deletednotes:
                            fx.write(ix)
                    fx.truncate()

                count = 0
                filemenu.delete(7, 'end')

                with open("savedtuningnames.txt", "r") as W:
                    Q = W.readlines()

                for tnamitem in Q:
                    tnamitem = tnamitem.strip('\n')
                    Q[count] = tnamitem
                    count += 1

                for itemname in Q:
                    def new_command1(itemname=itemname):
                        self.open_tuning(itemname)  ######## scroll down to find this function #######

                    filemenu.add_command(label=itemname, command=new_command1)

                delete_window.destroy()

                # print(vv)

            windowWidth = 300
            windowHeight = 80
            counter11 = 0

            with open("savedtuningnames.txt", "r") as g:
                t = g.readlines()
                for inde in t:
                    inde = inde.strip('\n')
                    t[counter11] = inde
                    counter11 += 1

            for everyname in t:
                windowHeight += 25

            delete_window = Toplevel(root)
            delete_window.geometry(str(windowWidth) + 'x' + str(windowHeight) + '+500+50')
            # delete_window.configure(background='white')
            delete_window.title('Delete Custom')

            index_num = 0
            new_t = t[:]

            for another_var in new_t:
                custom_names = []
                custom_names.append(another_var)
                custom_names.append(index_num)
                new_t[index_num] = custom_names
                index_num += 1

            vv = IntVar()

            label2 = ttk.Label(delete_window, text='Which tunings would you like to delete?')
            label2.pack()

            spacex1 = ttk.Label(delete_window, text=' ').pack()

            for tunenam, tuneval in new_t:
                ttk.Radiobutton(delete_window, text=tunenam, variable=vv, value=tuneval).pack(anchor=W)

            spacex2 = ttk.Label(delete_window, text=' ').pack()

            delbutton = ttk.Button(delete_window, text='Delete', command=lambda: del_cust(vv.get()))
            delbutton.pack()

        filemenu.add_command(label="Delete Custom...", command=lambda: ifdeletecustom())

        filemenu.add_separator()

        filemenu.add_command(label="Standard", command=standardTuning)
        filemenu.add_command(label="Drop D", command=DropDTuning)
        filemenu.add_command(label="Five String", command=fiveStringB)

        ######### Listing saved tunings #########

        with open('savedtuningnames.txt', 'r') as tuning_names:
            thetuningnames = tuning_names.readlines()
            for items0 in thetuningnames:
                items0 = items0.strip('\n')
                thetuningnames[icount] = items0
                icount += 1

        # print(thetuningnames)

        for items1 in thetuningnames:
            def new_command(items1=items1):
                self.open_tuning(items1)  ######## scroll down to find this function #######

            filemenu.add_command(label=items1, command=new_command)



        ######### ^^^^^^^^^^^^^^^^^^^^^ #########


        #filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Tuning", menu=filemenu)

        menubar.add_cascade(label="Options", menu=choicesMenu)



        choicesMenu.add_command(label="Default Colors", command=self.changeToDefaultColor)
        choicesMenu.add_command(label="Colorblind Mode", command=self.changeToColorBlind)

        choicesMenu.add_separator()

        choicesMenu.add_command(label="Dot Mode", command=self.changeToDots)
        choicesMenu.add_command(label="Shape Mode", command=self.changeToShapes)





        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=help_window)
        helpmenu.add_command(label="Tutorial", command=lambda: user_tutorial(root))
        helpmenu.add_command(label="About...", command=about_window)
        menubar.add_cascade(label="Help", menu=helpmenu)



        root.config(menu=menubar)
        ##################### CASCADING MENUS   #################
        def getModeInput():
            outp = note_var.get() + ' ' + mode_var.get()
            #print(outp)
            return outp

        self.addingWidgets()

    def addingWidgets(self):
        labelFrame = ttk.LabelFrame(self.page1, text = 'Builder')
        labelFrame.pack()

        label1 = ttk.Label(labelFrame, text = 'In which key would you like to build?')
        label1.pack()

        v = StringVar()

        entry1 = Entry(labelFrame, textvariable=v)
        entry1.pack()

        # this button sends the input variable to the Build function outside of the class
        gbutton = ttk.Button(labelFrame, text='Guitar', command=lambda: Display(v.get(),self, 6, parse(v.get()), tuning = DefaultTuning, colorBlindMode= self.ColorBlind, DotMode = self.DotMode))
        gbutton.pack()

        bbutton = ttk.Button(labelFrame, text='Bass', command=lambda: Display(v.get(), self, 4, parse(v.get()), tuning = DefaultTuning, colorBlindMode= self.ColorBlind, DotMode = self.DotMode))
        bbutton.pack()

        fivebutton = ttk.Button(labelFrame, text='5 String', command=lambda: Display(v.get(),self, 5, parse(v.get()), tuning = DefaultTuning, colorBlindMode= self.ColorBlind, DotMode = self.DotMode))
        fivebutton.pack()

        labelspace = ttk.Label(labelFrame, text = ' ')
        labelspace.pack()

        quitButton = ttk.Button(labelFrame, text = 'Quit', command = self.client_exit)
        quitButton.pack()

        notekey = [['C',0], ['C#',1],['Db',2], ['D',3], ['D#',4],['Eb',5], ['E',6],
                   ['F',7], ['F#',8],['Gb',9], ['G',10], ['G#',11],['Ab',12], ['A',13],
                   ['A#',14],['Bb',15], ['B',16]]

        majmin = [['Major',17],['Minor',18],['Augmented', 22], ['Diminished', 23]]

        GorB = [['Guitar',19],['Bass',20],["5 String", 21]]

        mmv = IntVar()
        vv = IntVar()
        GBV = IntVar()
        vv.set(0)
        mmv.set(17)
        GBV.set(19)

        labelFrame2 = ttk.LabelFrame(self.page2)
        labelFrame2.grid(column=0, row=0, columnspan = 2)

        label2 = ttk.Label(labelFrame2, text='In which key would you like to build?')
        label2.pack()

        labelFrame2_1 = ttk.LabelFrame(labelFrame2)
        labelFrame2_1.pack(side=LEFT)

        labelFrame2_2 = ttk.LabelFrame(labelFrame2)
        labelFrame2_2.pack(side=TOP)

        cnt = 0
        for keyval, vval in notekey:
            if cnt >= len(notekey)/2:
                ttk.Radiobutton(labelFrame2_2, text=keyval, variable=vv, value=vval, width = 10).pack(anchor=W)
            else:
                ttk.Radiobutton(labelFrame2_1, text=keyval, variable=vv, value=vval, width = 10).pack(anchor=W)
            cnt+=1

        labelFrame3 = ttk.LabelFrame(self.page2)
        labelFrame3.grid(column=2,row=0,sticky='N')

        label3 = ttk.Label(labelFrame3, text = 'Major or Minor?')
        label3.pack()

        for mmval,vmajmin in majmin:
            ttk.Radiobutton(labelFrame3, text = mmval, variable = mmv, value = vmajmin).pack(anchor=W)


        labelFrame4 = ttk.LabelFrame(self.page2)
        labelFrame4.grid(column=3,row=0,sticky='N')

        label4 = ttk.Label(labelFrame4, text = 'Which Instrument?')
        label4.pack()

        for GorBname,val_GB in GorB:
            ttk.Radiobutton(labelFrame4, text = GorBname, variable = GBV, value = val_GB).pack(anchor=W)


        labelFrame5 = ttk.LabelFrame(self.page2)
        labelFrame5.grid(column=0,row=1)
        buildbutton = ttk.Button(labelFrame5, text = 'Build', command = lambda: self.construct_input(vv.get(),mmv.get(),GBV.get()))

        buildbutton.pack()

        labelFrame6 = ttk.LabelFrame(self.page2)
        labelFrame6.grid(column=2,row=1)


        quitbutton = ttk.Button(labelFrame6, text = 'Quit', command = self.client_exit)
        quitbutton.pack()

    def client_exit(self):
         exit()

    def open_tuning(self,tune_name):

        global DefaultTuning
        counter1 = 0
        counter2 = 0

        with open('savedtuningnotes.txt', 'r') as tnot:
            tnotn = tnot.readlines()
            for tnotitem in tnotn:
                tnotitem = tnotitem.strip('\n')
                nestedlist = []
                counter3 = 0
                for character in tnotitem:
                    nestedlist.append(character)
                for characters in nestedlist:
                    if characters == '#':
                        nestedlist[counter3 - 1] += characters
                        nestedlist.pop(counter3)
                        counter3 += 1
                    else:
                        counter3 += 1
                tnotn[counter1] = nestedlist
                counter1 += 1

        with open('savedtuningnames.txt', 'r') as tnam:
            tnamn = tnam.readlines()
            for tnamitem in tnamn:
                tnamitem = tnamitem.strip('\n')
                tnamn[counter2] = tnamitem
                counter2 += 1

        if tune_name in tnamn:
            name_index = tnamn.index(tune_name)
        else:
            None

        chosen_note = tnotn[name_index]

        DefaultTuning = chosen_note

    def construct_input(self, key_note,key_type,instrument):
        notekey = [['C',0], ['C#',1],['Db',2], ['D',3], ['D#',4],['Eb',5], ['E',6],
                       ['F',7], ['F#',8],['Gb',9], ['G',10], ['G#',11],['Ab',12], ['A',13],
                       ['A#',14],['Bb',15], ['B',16]]

        thekeynote = str(notekey[key_note][0])

        if key_type == 17:
            thekeytype = 'Maj7'
        elif key_type == 18:
            thekeytype = 'min7'
        elif key_type == 22:
            thekeytype = 'aug7'
        elif key_type == 23:
            thekeytype = 'dim7'

        key = thekeynote + thekeytype
        #print(key, 'here')

        if instrument == 19:
            Display(key, self, 6, parse(key), tuning = DefaultTuning,colorBlindMode= self.ColorBlind, DotMode = self.DotMode)
        if instrument == 20:
            Display(key, self, 4, parse(key), tuning = DefaultTuning,colorBlindMode= self.ColorBlind, DotMode = self.DotMode)
        if instrument == 21:
            Display(key, self, 5, parse(key), tuning = DefaultTuning,colorBlindMode= self.ColorBlind, DotMode = self.DotMode)


def callback1(event):
    webbrowser.open_new(r"https://en.wikibooks.org/wiki/Guitar/Anatomy_of_a_Guitar")


def callback2(event):
    webbrowser.open_new(r"http://www.gamlinsmusic.co.uk/anatomy-of-an-electric-bass-guitar/")


def callback3(event):
    webbrowser.open_new(r"https://en.wikiversity.org/wiki/Introduction_to_music")


def callback4(event):
    webbrowser.open_new(r"https://en.wikipedia.org/wiki/Major_and_minor")


def callback5(event):
    webbrowser.open_new(r"https://en.wikipedia.org/wiki/Chord_(music)")


def help_window():

    hwind = Toplevel(root)
    hwind.geometry('400x350+500+50')
    hwind.title('Help')


    with open('help_file.txt','r') as help_file:
        lines = help_file.readlines()

    for line in lines:
        line = line.rstrip()
        label = Label(hwind, text = line).pack()

    space1 = Label(hwind, text = ' ')
    space1.pack()

    link1 = Label(hwind, text="Anatomy of a Guitar", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", callback1)

    link2 = Label(hwind, text="Brief Anatomy of Bass Guitar", fg="blue", cursor="hand2")
    link2.pack()
    link2.bind("<Button-1>", callback2)

    link3 = Label(hwind, text="Brief intro to Music Terminology", fg="blue", cursor="hand2")
    link3.pack()
    link3.bind("<Button-1>", callback3)

    link4 = Label(hwind, text="Major and Minor", fg="blue", cursor="hand2")
    link4.pack()
    link4.bind("<Button-1>", callback4)

    link5 = Label(hwind, text="What is a Chord?", fg="blue", cursor="hand2")
    link5.pack()
    link5.bind("<Button-1>", callback5)

def about_window():
    awind = Toplevel(root)
    awind.geometry('400x600+500+50')
    awind.title('About')

    with open('about_file.txt','r') as about_file:
        lines = about_file.readlines()

    for line in lines:
        line = line.rstrip()
        label = Label(awind, text = line, font = ("Times",10)).pack()


root = Tk()
root.geometry(str(AppWidth)+'x'+str(AppHeight)+'+50+50')


app = Window(root)

root.mainloop()

