from tkinter import *
from tkinter import ttk
import webbrowser

from buildArp import parse, buildMode
from VirtualNeck import Neck


AppHeight = 600
AppWidth = 500

### origonal ###  color_pallet = ['#BA4141', '#95FA92', '#4196C0', '#DCEF8F'] ### for NOTES R, 3, 5, 7
color_pallet = ['#FF5151', '#B1F69C', '#A4EBF0', '#F6F9A3']
####           [  'red'     'green'     'blue'    'yellow']
####            [   1         3           5          7    ]

neckColor =     '#C9B5A4'

fretColor =     '#666666'
fretOutline =   '#000000'

stringOutline = '#444444'
stringColor =   '#757575'

markerCenter = '#FCFFEB'
markerOutline = '#797367'

highlights = '#FFFFFF'
stringHighlights = '#D0D0D0'

class Window(Frame):   # this class is the opening window
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Chord and Arpeggio Builder')

        nb = ttk.Notebook(root)

        self.page1 = ttk.Frame(nb)
        nb.add(self.page1, text='Builder')
        self.page2 = ttk.Frame(nb)
        nb.add(self.page2, text='Alternative Build')
        self.page3 = ttk.Frame(nb)




        nb.add(self.page3, text='Scales')
        nb.pack(expan = 1, fill = 'both')





        ###### DONT KNOW WHERE TO PUT BELOW IN ADDWIDGIT



        note_choices = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        note_var = StringVar(self.page3)
        note_var.set('C')
        notes_Menu = OptionMenu(self.page3, note_var, *note_choices)
        notes_Menu.pack()


        mode_choices = [ 'Ionian (major)',
                         'Dorian',
                         'Phrygian',
                         'Lydian',
                         'Mixolydian',
                         'Aeolian (minor)',
                         'Locrian',
                         ]
        mode_var = StringVar(self.page3)
        mode_var.set('Ionian (major)')
        modes_Menu = OptionMenu(self.page3, mode_var, *mode_choices)
        modes_Menu.pack()

        but = Button(self.page3, text='go', command=lambda: show_arpeggio(getModeInput(), numOfStrings = 6, searchNotes = buildMode(note_var.get(),mode_var.get())))
        but.pack()


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

        #this button sends the input variable to the Build function outside of the class
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

        GorB = [['Guitar',19],['Bass',20]]

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
    print(key, 'here')

    if instrument == 19:
        show_arpeggio(key, 6, parse(key))
    if instrument == 20:
        show_arpeggio(key, 4, parse(key))


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


def show_arpeggio(key, numOfStrings = 6, searchNotes = []):
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




    W_WIDTH = 1200                              # window dimensions
    W_HEIGHT = 200
    buff = 100                                   # buffer space on sides of Neck display

    C_WIDTH = W_WIDTH - (2 * buff)              # canvas dimensions
    C_HEIGHT = W_HEIGHT - (W_HEIGHT / 4)


    window = Toplevel(root) ### <<----------------------------------------------- links window to ROOT app frame
    window.geometry(str(W_WIDTH) + 'x' + str(W_HEIGHT) +'+50+400')
    window.configure(background='white')
    window.title(key)
    canvas = Canvas(window, width = C_WIDTH, height = C_HEIGHT, bg = neckColor)#4B2D00')



    canvas.place(x = W_WIDTH/2, y= 10, anchor = 'n')
    #canvas.pack(fill=NONE, expand=1)   #### ^^ Limit / restructure


    StringPositions = []

    NotePositions = []
    markerPositions = []

    if (searchNotes[0] in Flatnotes):
        nType = 'flat'
    else:
        nType = 'sharp'


    if numOfStrings == 4:
        neck = Neck(searchnotes = searchNotes, instrument = 'bass', sharp_o_flat= nType)

    elif numOfStrings == 6:
        neck = Neck(searchnotes = searchNotes, instrument = 'guitar', sharp_o_flat= nType)





    class NoteDot:
        def __init__(self, x, y, note, color, size = 10, shift = 2):
            '''
            
            :param x: x location of center(ish) of dot
            :param y: y location of center(ish) of dot
            :param note: String value - name of note
            :param color: Color (hex or keyword) corresponding to keytone
            :param size: Size of the dot (radius'ish')
            :param shift: SHIFT NOTE NAME DISPLAY RIGHT(+) or LEFT (-)
            '''

            self.note = note
            self.color = color
            canvas.create_oval(x + size*1.5, y - size, x - size, y + size, fill=color)
            canvas.create_text(x +shift, y, text=note, font="Arial 15 bold")


    def genFrets():
        '''
        Hodgepodge of proportional equations relying on 
        W_WIDHT, W_HEIGHT, dimensions, weird equations to make lower frets bigger. << unneccesary
        
        Also populates NotePositions, and markerPositions
        -- silly equations to place note markers proportionally within respective fret
        :return: 
        '''


        def draw_fret(x, size):

            canvas.create_line(x, 0, x, C_HEIGHT, width=size, fill = fretOutline)
            canvas.create_line(x, 0, x, C_HEIGHT, width=size -2, fill= fretColor)
            canvas.create_line(x-1, 0, x-1, C_HEIGHT, width=1, fill=highlights)

        length = C_WIDTH
        draw_fret(5,5)    # start neck (open string)
        draw_fret(length, 5)    # end neck (12 fret)

        spacing = (length / 16.5)

        pos = length - spacing

        NotePositions.append(5) ###### POSITION OF OPEN STRING NOTES
        markerPositions.append(0)
        NotePositions.append(pos + ((spacing/7)*4.5)) ##### POSITION OF 12th FRET NOTE
        markerPositions.append(pos+spacing/2)

        while pos > 50:   ### keeps frets from being generated too close to TOP of neck
            draw_fret(pos, 4)
            prevpos = pos
            pos -= spacing
            notePos = pos + (((prevpos - pos)/7)*4.5)  ##### INSERTS BETWEEN OPEN STRING and 12Th FRET   ( NOTE 3/5ths of way to next fret )


            NotePositions.insert(1,notePos)
            markerPositions.insert(1, pos + ((prevpos-pos)/2))
            spacing += 4.6

        '''for n in NotePositions:
            canvas.create_line(n, 0, n, 10, width = 10)   ### DOTS AT TOP/bottom   --------------------------------TESTING
            canvas.create_line(n, C_HEIGHT, n, C_HEIGHT-10, width=10)'''

        def single(x, y):
            size = 10
            canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline = markerOutline, width = 5)
            canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline = 'black', width = 2.3)
        def drawMarkers():


            single(markerPositions[3], C_HEIGHT / 2)            #### drawing fret markers
            single(markerPositions[5], C_HEIGHT / 2)
            single(markerPositions[7], C_HEIGHT / 2)
            single(markerPositions[9], C_HEIGHT / 2)
            single(markerPositions[12], C_HEIGHT / 3.5)
            single(markerPositions[12], C_HEIGHT-(C_HEIGHT / 3.5 ))

        drawMarkers()

    def genStrings(n_of_strings):
        top = 15
        bottom = C_HEIGHT - top/2  ## DUMB CORRECTIONS< BOTTOM HAS EXTRA SPACE
        stringWidth = C_HEIGHT - 2*(top-2) ############### I THIS IS A MESS,    weird math makes it seem to work?




        spacing = (stringWidth / (n_of_strings - 1))

        x = top
        if numOfStrings == 4:
            w = 5
        else:
            w = 3
        while x < bottom +1:
            StringPositions.append(x)

            canvas.create_line(0,x,C_WIDTH,x, width = w, fill = stringOutline)
            canvas.create_line(0, x, C_WIDTH, x, width=w-2, fill= stringColor)
            canvas.create_line(0, x-1, C_WIDTH, x-1, width= 1, fill= stringHighlights)
            x += spacing
    genStrings(numOfStrings)

    genFrets()
    genStrings(numOfStrings)

    def drawArp(searchnotes = []):
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
                        NoteDot(NotePositions[n], StringPositions[s], note, colors[searchnotes.index(note)], size = 11, shift = 8)
                    else:
                        NoteDot(NotePositions[n], StringPositions[s], note, colors[searchnotes.index(note)])


                n += 1
            s+=1
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
                    color = 'gray'
                    if note in arpnotes:
                        color = colors[arpnotes.index(note)]

                    if n == 0:
                        NoteDot(NotePositions[n], StringPositions[s], note, color, size=11,
                                shift=8)
                    else:
                        NoteDot(NotePositions[n], StringPositions[s], note, color)

                n += 1
            s += 1
            n = 0


    def draw_border():
        '''
        attmpting to place border around canvas ---- did not leave room at edges of canvas, and there seems to be extra pixels at bottom.
        something fucky going on with coordinates/display
        :return: 
        '''

        #TOP BOTTOM
        #canvas.create_line(0, 2, C_WIDTH, 0, width=10, fill='#797367')
        #canvas.create_line(0, C_HEIGHT-3, C_WIDTH, C_HEIGHT-3, width=3, fill='#797367')

        # SIDES
        canvas.create_line(3, 0, 3, C_HEIGHT, width=8, fill='black')
        #canvas.create_line(6, 0, 6, C_HEIGHT, width=2, fill=fretColor)
        canvas.create_line(C_WIDTH, 0, C_WIDTH, C_HEIGHT, width=3, fill='black')


    def draw_color_key(color):
        '''
        creates second canvas under the Display canvas.
        shows Colors relating to Root, 3rd, 5th, 7th.
         
            *** COLORS ACCESSED FROM MASTER LIST AT TOP ***
            
        :param color:  Color grabbed from color_pallet list
        :return: 
        '''
        canvas2 = Canvas(window, width=W_WIDTH, height=W_HEIGHT - C_HEIGHT, bg='white')  # 4B2D00')

        canvas2.place(x=W_WIDTH / 2, y=10 + C_HEIGHT, anchor='n')
        def block(x,y,color = 'black', label = '', note = ''):
            size = 15

            canvas2.create_rectangle(x + size, y + size/2, x - size, y- size/3, fill = color)
            canvas2.create_text(x,y+2,text = note, font = 'Arial 13 bold')
            canvas2.create_text(x+size + 10, y, text = label, font = "Arial 15", anchor = 'w')

        sections = W_WIDTH / 6
        row_y = 20
        label = 'Notes: - '
        for note in searchNotes:
            label += note +' - '
        canvas2.create_text(sections, row_y, text = label, font = 'Arial 20')
        block(sections*2,row_y,color_pallet[0], 'Root',note = searchNotes[0])
        #canvas2.create_text(60, 50, text = 'ROOT')

        block(sections*3,row_y, color_pallet[1], 'Third',note = searchNotes[1])

        block(sections*4, row_y, color_pallet[2], 'Fifth',note = searchNotes[2])
        block(sections*5, row_y, color_pallet[3], 'Seventh',note = searchNotes[3])

    def draw_string_labels():
        canvas3 = Canvas(window, width=30, height=C_HEIGHT, bg='white')  # 4B2D00')
        canvas3.place(x=buff- (buff/5), y=10, anchor='n')



        canvas4 = Canvas(window, width=30, height=C_HEIGHT, bg='white')  # 4B2D00')
        canvas4.place(x=W_WIDTH - (buff/5)*4, y=10, anchor='n')
        n = 0
        for string in neck.NECK:
            canvas3.create_text(15,StringPositions[n],text = '- ' + string[0], font = 'Arial 14 bold')
            canvas4.create_text(15, StringPositions[n], text = string[0] + ' -', font='Arial 14 bold')
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