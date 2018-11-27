from tkinter import *
from tkinter import ttk
import webbrowser
from CONSTANTS import *

from buildArp import parse, buildMode
from virtualneck import Neck

DefaultTuning = ['E', 'A', 'D', 'G', 'B', 'E'] # SLOPPY SLOPPY SLOPPY
# called as - global - in retune() and other functions,
# theres absolutely a better way to do this


class Window(Frame):   # this class is the opening window
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

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
                     command=lambda: show_arpeggio(getModeInput(), # STRING name of arp/scale
                                                   numOfStrings = GBV.get(),
                                                   searchNotes = buildMode(note_var.get(), mode_var.get())))
        but.pack()

        hbut = ttk.Button(self.page3, text='Help', command=help_window)
        hbut.pack()



        ###################### CASCADING MENUS #############################
        def donothing():
            print('not doing it.')

        

        def tuningMenu():
            windowWidth = 150
            windowHeight = 300

            tune_window = Toplevel(
                root)  ### <<----------------------------------------------- links window to ROOT app frame
            tune_window.geometry( str(windowWidth) + 'x' + str(windowHeight)  + '+500+50')
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
                        note_choices = note_choices[1:] +[note_choices[0]]



                    note_var = StringVar(tune_window)
                    note_var.set(note_choices[0])
                    notes_Menu = ttk.OptionMenu(tune_window, note_var, *note_choices)
                    notes_Menu.config(width = 8)
                    notes_Menu.place(x = 10 , y = x)
                    menus.append(notes_Menu)
                    selections.append(note_var)
                    x += spacing

            def retune():
                global DefaultTuning
                outp = []
                for note in selections:
                    outp.append(note.get())
                outp.reverse()

                print(outp)

                DefaultTuning = outp[:]
                return outp


            create_dropdown()

            tuneButton = ttk.Button(tune_window, text='Tune', command=retune)
            tuneButton.place(x = windowWidth/2, y = windowHeight-15, anchor = 'center')

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


        filemenu.add_command(label="Standard", command=standardTuning)
        filemenu.add_command(label="Drop D", command=DropDTuning)
        filemenu.add_command(label="Five String", command=fiveStringB)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Custom...", command=tuningMenu)

        #filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Tuning", menu=filemenu)


        """editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)"""
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=help_window)
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
        gbutton = ttk.Button(labelFrame, text='Guitar', command=lambda: show_arpeggio(v.get(), 6, parse(v.get())))
        gbutton.pack()

        bbutton = ttk.Button(labelFrame, text='Bass', command=lambda: show_arpeggio(v.get(), 4, parse(v.get())))
        bbutton.pack()

        hbutton = ttk.Button(labelFrame, text='Help', command=help_window)
        hbutton.pack()

        labelspace = ttk.Label(labelFrame, text = ' ')
        labelspace.pack()

        quitButton = ttk.Button(labelFrame, text = 'Quit', command = self.client_exit)
        quitButton.pack()

        notekey = [['C',0], ['C#',1],['Db',2], ['D',3], ['D#',4],['Eb',5], ['E',6],
                   ['F',7], ['F#',8],['Gb',9], ['G',10], ['G#',11],['Ab',12], ['A',13],
                   ['A#',14],['Bb',15], ['B',16]]

        majmin = [['Major',17],['Minor',18]]

        GorB = [['Guitar',19],['Bass',20],["5 String", 21]]

        mmv = IntVar()
        vv = IntVar()
        GBV = IntVar()
        vv.set(0)
        mmv.set(17)
        GBV.set(19)

        labelFrame2 = ttk.LabelFrame(self.page2)
        labelFrame2.grid(column=0,row=0)

        label2 = ttk.Label(labelFrame2, text = 'In which key would you like to build?')
        label2.pack()

        for keyval,vval in notekey:
            ttk.Radiobutton(labelFrame2, text = keyval, variable = vv, value = vval).pack(anchor=W)

        labelFrame3 = ttk.LabelFrame(self.page2)
        labelFrame3.grid(column=1,row=0,sticky='N')

        label3 = ttk.Label(labelFrame3, text = 'Major or Minor?')
        label3.pack()

        for mmval,vmajmin in majmin:
            ttk.Radiobutton(labelFrame3, text = mmval, variable = mmv, value = vmajmin).pack(anchor=W)


        labelFrame4 = ttk.LabelFrame(self.page2)
        labelFrame4.grid(column=2,row=0,sticky='N')

        label4 = ttk.Label(labelFrame4, text = 'Guitar or Bass?')
        label4.pack()

        for GorBname,val_GB in GorB:
            ttk.Radiobutton(labelFrame4, text = GorBname, variable = GBV, value = val_GB).pack(anchor=W)


        labelFrame5 = ttk.LabelFrame(self.page2)
        labelFrame5.grid(column=0,row=1)
        buildbutton = ttk.Button(labelFrame5, text = 'Build', command = lambda: construct_input(vv.get(),mmv.get(),GBV.get()))

        buildbutton.pack()

        labelFrame6 = ttk.LabelFrame(self.page2)
        labelFrame6.grid(column=2,row=1)

        helpbutton = ttk.Button(labelFrame6, text='Help', command=help_window)
        helpbutton.pack()

        quitbutton = ttk.Button(labelFrame6, text = 'Quit', command = self.client_exit)
        quitbutton.pack()

    def client_exit(self):
         exit()


def construct_input(key_note,key_type,instrument):
    notekey = [['C',0], ['C#',1],['Db',2], ['D',3], ['D#',4],['Eb',5], ['E',6],
                   ['F',7], ['F#',8],['Gb',9], ['G',10], ['G#',11],['Ab',12], ['A',13],
                   ['A#',14],['Bb',15], ['B',16]]

    thekeynote = str(notekey[key_note][0])

    if key_type == 17:
        thekeytype = 'Major'
    elif key_type == 18:
        thekeytype = 'Minor'

    key = thekeynote + thekeytype
    #print(key, 'here')

    if instrument == 19:
        show_arpeggio(key, 6, parse(key))
    if instrument == 20:
        show_arpeggio(key, 4, parse(key))
    if instrument == 21:
        show_arpeggio(key,5, parse(key))


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


def callback6(event):
    webbrowser.open_new(r"https://en.wikipedia.org/wiki/Scale_(music)")


def callback7(event):
    webbrowser.open_new(r"https://outsideshore.com/primer/major-scale-harmony/#MajorScale")


def help_window():

    hwind = Toplevel(root)
    hwind.geometry('400x400+500+50')
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

    link6 = Label(hwind, text="What are Scales?", fg="blue", cursor="hand2")
    link6.pack()
    link6.bind("<Button-1>", callback6)

    link7 = Label(hwind, text="What are the types of Scales for Guitar/Bass?", fg="blue", cursor="hand2")
    link7.pack()
    link7.bind("<Button-1>", callback7)


def about_window():
    awind = Toplevel(root)
    awind.geometry('400x475+500+50')
    awind.title('About')

    with open('about_file.txt','r') as about_file:
        lines = about_file.readlines()

    for line in lines:
        line = line.rstrip()
        label = Label(awind, text = line).pack()

        

def show_arpeggio(key, numOfStrings=6, searchNotes=[]):
    global DefaultTuning
    '''
    Function that:  Generates Display Window,
                    Draws Neck (frets, strings, fretMarkers)
                    Constructs and draws NOTES TO DISPLAY
    :param key: ------------ FULL STRING OF ARP OR CHORD
    :param numOfStrings: --- number of strings, - used in maths to divide evnenly spaced strings
    :param searchNotes: ---- Notes to find/display
    :return: 
    '''


    Flatnotes = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']

    working_notes = []

    W_WIDTH = 1200  # window dimensions
    W_HEIGHT = 200
    buff = 100  # buffer space on sides of Neck display

    C_WIDTH = W_WIDTH - (2 * buff)  # canvas dimensions
    C_HEIGHT = W_HEIGHT - (W_HEIGHT / 3.3)

    window = Toplevel(root)  ### <<----------------------------------------------- links window to ROOT app frame
    window.geometry(str(W_WIDTH) + 'x' + str(W_HEIGHT) + '+50+400')
    window.configure(background=lightGray)
    window.title(key)

    ####  CUT CUT CUT CUT vvvv
    # canvasoutl = Canvas(window, width=C_WIDTH, height=C_HEIGHT, bg=shade(neckColor, 100), borderwidth = 20)  # 4B2D00')
    #
    # canvasoutl.place(x=W_WIDTH /2, y=0, anchor='n')
    ##### CANVAS BEHIND CANVAS^^^^
    canvas = Canvas(window, width=C_WIDTH, height=C_HEIGHT, bg=neckColor, borderwidth = 0, relief = SUNKEN, highlightbackground= black)  # 4B2D00')

    canvas.place(x=W_WIDTH / 2, y=10, anchor='n')
    # canvas.pack(fill=NONE, expand=1)   #### ^^ Limit / restructure


    StringPositions = []

    NotePositions = []
    markerPositions = []

    black_bars = []

    if (searchNotes[0] in Flatnotes):

        nType = 'flat'
    else:
        nType = 'sharp'

    if numOfStrings == 4:
        neck = Neck(searchnotes = searchNotes,
                    instrument = 'bass',
                    sharp_o_flat = nType,
                    tuning = DefaultTuning)
    if numOfStrings == 5:
        # DefaultTuning = ['B', 'E', 'A', 'D', 'G','B']
        neck = Neck(searchnotes=searchNotes,
                    instrument='5string',
                    sharp_o_flat=nType,
                    tuning=DefaultTuning)

    elif numOfStrings == 6:
        neck = Neck(searchnotes = searchNotes,
                    instrument = 'guitar',
                    sharp_o_flat = nType,
                    tuning = DefaultTuning)    #### VARIABLE HOLDING [EADGBE] DEFAULT << CHANGED BY THE "Change Tuning" menu option?

    class NoteDot:
        def __init__(self, x, y, note, color, size=10, shift=2):
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

            self.defaultSize = 10
            self.size = size
            self.shift = shift
            self.note = note
            self.color = color
            self.size2 = size - 2   # size of highlight on note
            self.shadeAmount = 125  # amount to subtract from RGB when run through shade() function

            self.fontColor = black
            self.font = "Arial 15 bold"

            if self.color == gray:
                self.fontColor = darkGray
                self.font = "Arial 10 bold"



            # --- Shaded / outlined base for Note
            self.A = canvas.create_oval(self.x + self.size * 1.5, y - self.size, x - self.size, self.y + self.size,
                                        fill=shade(self.color, self.shadeAmount),
                                        outline=shade(shade(self.color, self.shadeAmount),self.shadeAmount),
                                        width=1)
            # --- 'Highlight' on Note - uses color from preset [r g b y] list
            self.B = canvas.create_oval(self.x + self.size2 * 1.5, self.y - self.size2, self.x - self.size2,
                                        y + self.size2,
                                        fill=self.color,
                                        outline='')
            # self.size2 -=2
            # self.HL = canvas.create_oval((self.x + self.size2 * 1.5)-1, (self.y - self.size2)-2, (self.x - self.size2)-2,
            #                              (y + self.size2)-3,
            #                             fill=lightn(self.color,20),
            #                             outline='')

            # --- Display note text on note
            self.C = canvas.create_text(self.x + self.shift, self.y, text=self.note, font=self.font, fill = self.fontColor)


            # binds whole note dot display to action   ----------VVVVV
            canvas.tag_bind(self.A, '<ButtonPress-1>', lambda x: ALL(self))
            canvas.tag_bind(self.B, '<ButtonPress-1>', lambda x: ALL(self))
            canvas.tag_bind(self.C, '<ButtonPress-1>', lambda x: ALL(self))

        # def shade(self, hexcolor):
        #     working = hex2rgb(hexcolor)
        #     working = [(i - self.shadeAmount) if ((i - self.shadeAmount) >= 0) else 0 for i in
        #                working]  ### ASSURES VALUES DONT GO BELOW 0 #####
        #     c = rgb2hex(working[0], working[1], working[2])
        #     return c

        def replaceDot(self):  # , x, y, note, color, size, shift):
            canvas.delete(self.A)
            canvas.delete(self.B)
            canvas.delete(self.C)

    def GOTCLICK(note_dot, color=red):
        # print(note_dot.note)
        note_dot.replaceDot()
        searchnotes = searchNotes[:]
        x = note_dot.x
        y = note_dot.y
        note = note_dot.note
        size = note_dot.defaultSize
        # print('sss',working_notes)
        if color == gray:
            size -= 1.5
        if x == NotePositions[0]:
            size += 1

        n = note_dot.__init__(x, y, note, color, size, shift=note_dot.shift)

    def ALL(newRoot_Dot, searchnotes=[]):
        newNotes = []
        for n in working_notes:
            if n.note not in newNotes:
                newNotes.append(n.note)

        while newRoot_Dot.note != newNotes[0]:
            newNotes = newNotes[1:] + [newNotes[0]]

        if len(newNotes) <= 4:


            ## add conditions for scale function

            for n in working_notes:
                newColor = color_pallet[newNotes.index(n.note)]

                GOTCLICK(n, newColor)




                ## add conditions for scale function

        #######stump############
        else:

            arp = [newNotes[i] for i in [0, 2, 4, 6]]
            for n in working_notes:
                if n.note in arp:
                    newColor = color_pallet[arp.index(n.note)]
                else:
                    newColor = gray
                GOTCLICK(n, newColor)


        # redraws L and R border -- stylistic only.
        for b in black_bars:

            canvas.delete(b)
        #print(len(black_bars))
        while len(black_bars) != 0:
            black_bars.pop()
        #print(len(black_bars))
        draw_border()
        #print(len(black_bars))


    def genFrets():
        '''
        Hodgepodge of proportional equations relying on 
        W_WIDHT, W_HEIGHT, dimensions, weird equations to make lower frets bigger. << unneccesary
        Also populates NotePositions, and markerPositions
        -- silly equations to place note markers proportionally within respective fret
        :return: 
        '''

        def draw_fret(x, size):
            canvas.create_line(x, 0, x, C_HEIGHT+10, width=size, fill=fretOutline)
            canvas.create_line(x, 0, x, C_HEIGHT+10, width=size - 2, fill=fretColor)
            canvas.create_line(x - 1, 0, x - 1, C_HEIGHT+10, width=1, fill=highlights)

        length = C_WIDTH
        draw_fret(5, 5)  # start neck (open string)
        draw_fret(length, 5)  # end neck (12 fret)

        spacing = (length / 21)   ############################################################### create starting spacing, (smallest fret) based on fraction of neck length

        pos = length - spacing

        NotePositions.append(5)  ###### POSITION OF OPEN STRING NOTES
        markerPositions.append(0)
        NotePositions.append(pos + ((spacing / 7) * 4.5))  ##### POSITION OF 12th FRET NOTE
        markerPositions.append(pos + spacing / 2)

        while pos > 50:  ### keeps frets from being generated too close to TOP of neck
            draw_fret(pos, 4)
            prevpos = pos
            pos -= spacing
            notePos = pos + (((
                                  prevpos - pos) / 7) * 4.5)  ##### INSERTS BETWEEN OPEN STRING and 12Th FRET   ( NOTE 3/5ths of way to next fret )

            NotePositions.insert(1, notePos)
            markerPositions.insert(1, pos + ((prevpos - pos) / 2))
            spacing += 2                                                                                ################# increase spacing to get larger frets at top of neck.


        def single(x, y):
            size = 10
            canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline=markerOutline,
                               width=5)
            canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline='black', width=2.3)

        def drawMarkers():
            single(markerPositions[3], C_HEIGHT / 2)  #### drawing fret markers
            single(markerPositions[5], C_HEIGHT / 2)
            single(markerPositions[7], C_HEIGHT / 2)
            single(markerPositions[9], C_HEIGHT / 2)
            single(markerPositions[12], C_HEIGHT / 3.5)
            single(markerPositions[12], C_HEIGHT - (C_HEIGHT / 3.5))
            single(markerPositions[15], C_HEIGHT / 2)

        drawMarkers()

    def genStrings(n_of_strings):
        top = 15
        bottom = C_HEIGHT - top / 2  ## DUMB CORRECTIONS< BOTTOM HAS EXTRA SPACE
        stringWidth = C_HEIGHT - 2 * (top - 2)  ############### I THIS IS A MESS,    weird math makes it seem to work?

        spacing = (stringWidth / (n_of_strings - 1))

        x = top
        if numOfStrings == 4:
            w = 5
        else:
            w = 3
        while x < bottom + 1:
            StringPositions.append(x)

            canvas.create_line(0, x, C_WIDTH, x, width=w, fill=stringOutline)
            canvas.create_line(0, x, C_WIDTH, x, width=w - 2, fill=stringColor)
            canvas.create_line(0, x - 1, C_WIDTH, x - 1, width=1, fill=stringHighlights)
            x += spacing

    genStrings(numOfStrings)

    genFrets()
    genStrings(numOfStrings)

    def drawArp(searchnotes=[]):
        '''
        :param searchnotes: List of Notes to Display
        iterates through the VirtualNeck object and displays searchnotes, 
        also adjusts the OPEN STRING markers.
        :return: 
        '''
        s = 0
        n = 0

        colors = color_pallet[:]

        for string in neck.NECK:
            for note in string:
                if note in searchnotes:
                    if n == 0:
                        d = NoteDot(NotePositions[n], StringPositions[s], note, colors[searchnotes.index(note)],
                                    size=11, shift=8)
                    else:
                        d = NoteDot(NotePositions[n], StringPositions[s], note, colors[searchnotes.index(note)])
                    working_notes.append(d)

                n += 1
            s += 1
            n = 0

    def drawScale(searchnotes=[]):
        '''
        :param searchnotes: List of Notes to Display
        iterates through the VirtualNeck object and displays searchnotes, 
        also handles the position of OPEN STRING markers.
        :return: 
        '''
        s = 0
        n = 0

        colors = color_pallet[:]
        arpnotes = [searchnotes[i] for i in [0, 2, 4, 6]]

        for string in neck.NECK:
            for note in string:

                if note in searchnotes:
                    color = gray
                    size = 8.5
                    if note in arpnotes:
                        color = colors[arpnotes.index(note)]
                        size = 10

                    if n == 0:
                        d = NoteDot(NotePositions[n], StringPositions[s], note, color, size=11,
                                    shift=7)
                    else:
                        d = NoteDot(NotePositions[n], StringPositions[s], note, color, size = size)
                    working_notes.append(d)

                n += 1
            s += 1
            n = 0

    def draw_border():
        '''
        # attmpting to place border around canvas ---- did not leave room at edges of canvas, and there seems to be extra pixels at bottom.
        # something fucky going on with coordinates/display
        # :return:
        '''

        # TOP BOTTOM
        # canvas.create_line(0, 2, C_WIDTH, 0, width=10, fill='#797367')
        # canvas.create_line(0, C_HEIGHT-3, C_WIDTH, C_HEIGHT-3, width=3, fill='#797367')

        # SIDES
        top = canvas.create_line(3, 0, 3, C_HEIGHT, width=3, fill='black')
        # canvas.create_line(6, 0, 6, C_HEIGHT, width=2, fill=fretColor)
        bottom = canvas.create_line(C_WIDTH, 0, C_WIDTH, C_HEIGHT, width=3, fill='black')
        black_bars.append(top)
        black_bars.append(bottom)



    def draw_color_key(color, replace = False):
        '''
        creates second canvas under the Display canvas.
        shows Colors relating to Root, 3rd, 5th, 7th.
            *** COLORS ACCESSED FROM MASTER LIST AT TOP ***
        :param color:  Color grabbed from color_pallet list
        :return: 
        '''
        def kill_color_key():
            canvas2.forget()
        if replace:
            kill_color_key()
        canvas2 = Canvas(window, width=W_WIDTH - 20, height=W_HEIGHT - (C_HEIGHT +20), bg=lightn(lightGray,20), bd = 0, relief = SUNKEN, highlightbackground = shade(lightGray,50))  # 4B2D00')

        canvas2.place(x=W_WIDTH / 2, y= 20 + C_HEIGHT, anchor='n')



        def block(x, y, color='black', label='', note=''):
            size = 15

            canvas2.create_rectangle(x + size, y + size / 2, x - size, y - size / 3, fill=color)
            canvas2.create_text(x, y + 2, text=note, font='Arial 13 bold')
            canvas2.create_text(x + size + 10, y, text=label, font="Arial 15", anchor='w')

        sections = W_WIDTH / 10
        row_y = 20
        label = 'Notes: - '
        for note in searchNotes:
            label += note + ' - '
        if len(searchNotes) == 7:
            arp = [searchNotes[n] for n in [0, 2, 4, 6]]
        else:
            arp = searchNotes[:]

        # canvas2.create_line(0,3,W_WIDTH,3, width = 4)
        # canvas2.create_line(0, 3, W_WIDTH, 3,fill = 'white' ,width=2)
        # canvas2.create_line(3, 3, 3, W_HEIGHT, fill=black, width=4)
        # canvas2.create_line(3, 3, 3, W_HEIGHT, fill = 'white',width=2)
        # canvas2.create_line(W_WIDTH-20, 3, W_WIDTH-20, W_HEIGHT, fill=black, width=4)
        # canvas2.create_line(W_WIDTH-20, 3, W_WIDTH-20, W_HEIGHT, fill='white', width=2)


        canvas2.create_text(sections*1.5, row_y, text=label, font='Arial 18')
        block(sections * 3, row_y, color_pallet[0], 'Root', note=arp[0])
        # canvas2.create_text(60, 50, text = 'ROOT')

        block(sections * 4, row_y, color_pallet[1], 'Third', note=arp[1])

        block(sections * 5, row_y, color_pallet[2], 'Fifth', note=arp[2])
        block(sections * 6, row_y, color_pallet[3], 'Seventh', note=arp[3])





    def draw_string_labels():
        canvas3 = Canvas(window, width=25, height=C_HEIGHT, bg=lightGray, highlightbackground = lightGray)  # 4B2D00')
        canvas3.place(x= (buff - buff/5 - 10), y=10, anchor='n')

        canvas4 = Canvas(window, width=25, height=C_HEIGHT, bg=lightGray, highlightbackground = lightGray)# 4B2D00')
        canvas4.place(x=(W_WIDTH - (buff / 5) * 4) + 10, y=10, anchor='n')
        n = 0
        for string in neck.NECK:
            canvas3.create_text(15, StringPositions[n], text='- ' + string[0], font='Arial 14 bold')
            canvas4.create_text(15, StringPositions[n], text=string[0] + ' -', font='Arial 14 bold')
            n += 1

    if len(searchNotes) <= 4:
        drawArp(searchNotes)
    if len(searchNotes) >= 7:
        drawScale(searchNotes)
    draw_border()
    draw_color_key('black')
    draw_string_labels()
root = Tk()
root.geometry(str(AppWidth)+'x'+str(AppHeight)+'+50+50')


app = Window(root)

root.mainloop()
