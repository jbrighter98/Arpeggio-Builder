from tkinter import *
from CONSTANTS import *
from virtualneck import *
from NoteDot import *
import SHAPES






class Display:
    def __init__(self, key, window_root, numOfStrings = 6, searchNotes = [], tuning = ['E','A','D','G','B','E'], colorBlindMode = False, DotMode = True, mode = ''):
        '''
        Function that:  Generates Display Window,
                        Draws Neck (frets, strings, fretMarkers)
                        Constructs and draws NOTES TO DISPLAY
        :param key: ------------ FULL STRING OF ARP OR CHORD
        :param numOfStrings: --- number of strings, - used in maths to divide evnenly spaced strings
        :param searchNotes: ---- Notes to find/display
        :return: 
        '''

        # ------------------------------------------------------------------------------------------------------------ #
        ### Window Variables ###
        import CONSTANTS

        self.W_WIDTH = 1200             # window dimensions
        self.W_HEIGHT = 200
        buff = 80  # buffer space on sides of Neck display -  lower num = stretch neck
        self.buff = buff

        self.C_WIDTH = self.W_WIDTH - (2 * buff)                # canvas x dimension
        self.C_HEIGHT = self.W_HEIGHT - (self.W_HEIGHT / 3)    # proportion of y of window



        if colorBlindMode:
            self.color_pallet = ColorBlind_Colors[:]
        else:
            self.color_pallet = Default_Colors[:]

        # ------------------------------------------------------------------------------------------------------------ #

        # ------------------------------------------------------------------------------------------------------------ #
        ### Instrument Variables ###

        self.num_strings = numOfStrings
        self.tuning = tuning[:]


        self.StringPositions = []                   # Y coordinates of strings
        self.NotePositions = []                     # X coordinates of note locations - proportion between frets
        self.MarkerPositions = []                   # X coordinates of marker locations - 1/2 between frets

        self.KeyNotes = searchNotes[:]              # Notes to search for --- keep in order
        self.search_notes = searchNotes[:]          # current arpeggio notes -- rotate with selection

        self.p_notes = searchNotes[:]
        self.arp_names = []
        if mode != '':

            if mode != 'Harmonic minor':
                self.arp_names = [ ['maj7', 'Ionian (major)'],
                            ['min7', 'Dorian'],
                            ['min7', 'Phrygian'],
                            ['maj7', 'Lydian'],
                            ['7', 'Mixolydian'],
                            ['min7', 'Aeolian (minor)'],
                            ['min7b5', 'Locrian'],
                            ]
                while mode != self.arp_names[0][1]:
                    self.arp_names = self.arp_names[1:] + [self.arp_names[0]]

            elif mode == 'Harmonic minor':
                self.arp_names = [ ['min(maj7)', 'Harmonic minor'],
                            ['m7b5', 'Locrian #6'],
                            ['maj7#5', 'Ionian #5'],
                            ['m7', 'Dorian #4'],
                            ['7', 'Phrygian Dominant'],
                            ['maj7', 'Lydian #2'],
                            ['dim7', 'Superlocrian'],
                            ]





        self.note_object_list = []


        self.OpenStringNoteSize = 11

        self.colorNoteSize = 10

        self.grayNoteSize = self.colorNoteSize - 1 # adjust size of greynotes in NoteDot Class ( f(size-x) )





        self.colorBlindMode = colorBlindMode
        self.DotMode = DotMode


        # ------------------------------------------------------------------------------------------------------------ #


        # --------- Drawing empty Fretboard --------- #

        root = window_root
        window = Toplevel(root)  ### <<----------------------------------------------- links window to ROOT app frame
        self.window = window # for use within functions
        window.geometry(str(self.W_WIDTH) + 'x' + str(self.W_HEIGHT) + '+50+400')
        window.configure(background=lightGray)
        window.title(key)

        self.canvas = Canvas(window, width=self.C_WIDTH, height=self.C_HEIGHT, bg=neckColor, bd = 0, highlightbackground = shade(lightGray, 150))  # 4B2D00')

        self.canvas.place(x=self.W_WIDTH / 2, y=5, anchor='n')

        # Draw neck (without notes)
        self.genFrets()

        self.drawMarkers()
        self.genStrings(self.num_strings)


        # ------------------------------



        # ------------------------------
        #  creating virtual neck/ drawing notes

        self.neck = self.CreateVneck()
        if len(self.search_notes) == 7:
            self.drawScale(searchnotes = self.search_notes)
        if len(self.search_notes) == 4:
            self.drawArp(searchnotes = self.search_notes)


        # ------- Drawing extra windows/ lower half ------- #
        self.draw_string_labels()
        self.draw_color_key()
        self.draw_arp_name()


    # -------- Virtual Neck Creation --------- #
    # ################################### #

    def CreateVneck(self):
        if (self.search_notes[0] in ['Db', 'Eb', 'Gb', 'Ab', 'Bb']):  # notes that trigger use of Flat Notes

            nType = 'flat'
        else:
            nType = 'sharp'

        if self.num_strings:
            self.neck = Neck(searchnotes = self.search_notes,
                             instrument = self.num_strings,
                             sharp_o_flat = nType,
                             tuning = self.tuning)
        # if self.num_strings == 5:
        #
        #     self.neck = Neck(searchnotes=self.working_notes,
        #                 instrument='5string',
        #                 sharp_o_flat=nType,
        #                 tuning=self.tuning)
        #
        # elif self.num_strings == 6:
        #     self.neck = Neck(searchnotes = self.working_notes,
        #                 instrument = 'guitar',
        #                 sharp_o_flat = nType,
        #                 tuning = self.tuning )

        return self.neck


    # -------- Neck Graphics Methods --------- #
    # ################################### #

    def genFrets(self):
        '''
        Hodgepodge of proportional equations relying on 
        W_WIDHT, W_HEIGHT, dimensions, weird equations to make lower frets bigger. << unneccesary

        Also populates NotePositions, and markerPositions
        -- silly equations to place note markers proportionally within respective fret
        :return: 
        '''

        def draw_fret(self,x, size):
            self.canvas.create_line(x, 0, x, self.C_HEIGHT + 10, width=size, fill=fretOutline)
            self.canvas.create_line(x, 0, x, self.C_HEIGHT + 10, width=size - 2, fill=fretColor)
            self.canvas.create_line(x - 1, 0, x - 1, self.C_HEIGHT + 10, width=1, fill=highlights)

        length = self.C_WIDTH
        draw_fret(self, 5, 5)  # start neck (open string)
        draw_fret(self, length, 5)  # end neck (12 fret)

        spacing = (
        length / 21)  ############################################################### create starting spacing, (smallest fret) based on fraction of neck length

        pos = length - spacing

        self.NotePositions.append(5)  ###### POSITION OF OPEN STRING NOTES
        self.MarkerPositions.append(0)
        self.NotePositions.append(pos + ((spacing / 7) * 4.5))  ##### POSITION OF 12th FRET NOTE
        self.MarkerPositions.append(pos + spacing / 2)

        while pos > 50:  ### keeps frets from being generated too close to TOP of neck
            draw_fret(self, pos, 4)
            prevpos = pos
            pos -= spacing
            notePos = pos + (((
                                  prevpos - pos) / 7) * 4.5)  ##### INSERTS BETWEEN OPEN STRING and 12Th FRET   ( NOTE 3/5ths of way to next fret )

            self.NotePositions.insert(1, notePos)
            self.MarkerPositions.insert(1, pos + ((prevpos - pos) / 2))
            spacing += 2  ################# increase spacing to get larger frets at top of neck.

    def single_marker(self, x, y):
        size = 10
        self.canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline=markerOutline,
                           width=5)
        self.canvas.create_oval(x + size, y - size, x - size, y + size, fill=markerCenter, outline='black',
                           width=2.3)

    def drawMarkers(self):
        self.single_marker(self.MarkerPositions[3], self.C_HEIGHT / 2)  #### drawing fret markers
        self.single_marker(self.MarkerPositions[5], self.C_HEIGHT / 2)
        self.single_marker(self.MarkerPositions[7], self.C_HEIGHT / 2)
        self.single_marker(self.MarkerPositions[9], self.C_HEIGHT / 2)
        self.single_marker(self.MarkerPositions[12], self.C_HEIGHT / 3.5)
        self.single_marker(self.MarkerPositions[12], self.C_HEIGHT - (self.C_HEIGHT / 3.5))
        self.single_marker(self.MarkerPositions[15], self.C_HEIGHT / 2)

    def genStrings(self, n_of_strings):
        if n_of_strings >= 4:
            top = 15
            bottom = self.C_HEIGHT - top / 2  ## DUMB CORRECTIONS< BOTTOM HAS EXTRA SPACE
            stringWidth = self.C_HEIGHT - 2 * (
            top - 2)  ############### I THIS IS A MESS,    weird math makes it seem to work?
        else:
            top = (self.C_HEIGHT/ (n_of_strings + 1))
            bottom = self.C_HEIGHT - top  ## DUMB CORRECTIONS< BOTTOM HAS EXTRA SPACE
            stringWidth = (bottom - top)   ############### I THIS IS A MESS,    weird math makes it seem to work?

        spacing = (stringWidth / (n_of_strings-1))

        x = top
        if self.num_strings <= 4:
            w = 5
        else:
            w = 3
        while x <= bottom + 1:
            self.StringPositions.append(x)

            self.canvas.create_line(0, x, self.C_WIDTH, x, width=w, fill=stringOutline)
            self.canvas.create_line(0, x, self.C_WIDTH, x, width=w - 2, fill=stringColor)
            self.canvas.create_line(0, x - 1, self.C_WIDTH, x - 1, width=1, fill=stringHighlights)
            x += spacing


    # -------- Neck Populating Methods --------- #
    # ################################### #




    def drawArp(self, searchnotes=[]):
        '''

        :param searchnotes: List of Notes to Display
        iterates through the VirtualNeck object and displays searchnotes, 
        also adjusts the OPEN STRING markers.
        :return: 
        '''
        s = 0
        n = 0

        if self.colorBlindMode:
            colors = ColorBlind_Colors[:]
        else:
            colors = Default_Colors[:]

        for string in self.neck.NECK:
            for note in string:
                if note in searchnotes:
                    if n == 0:
                        if self.DotMode:
                            d = NoteDot(self.NotePositions[n],
                                        self.StringPositions[s],
                                        note,
                                        colors[searchnotes.index(note)],
                                        size=self.OpenStringNoteSize, shift=8,
                                        canvas = self.canvas,
                                        Display = self)
                        else:
                            d = SHAPES.genShape(self.NotePositions[n], self.StringPositions[s], Display=self,
                                                note=note, size=self.colorNoteSize, fill= colors[searchnotes.index(note)])

                    else:
                        if self.DotMode:

                            d = NoteDot(self.NotePositions[n],
                                        self.StringPositions[s],
                                        note,
                                        colors[searchnotes.index(note)],
                                        size = self.colorNoteSize,
                                        canvas = self.canvas,
                                        Display = self)
                        else:
                            d = SHAPES.genShape(self.NotePositions[n], self.StringPositions[s], Display = self, note = note, size =  self.colorNoteSize, fill = colors[searchnotes.index(note)])
                    self.note_object_list.append(d)
                    # self.note_object_list.append(shape)

                n += 1
            s += 1
            n = 0

    def drawScale(self, searchnotes=[]):
        '''

        :param searchnotes: List of Notes to Display
        iterates through the VirtualNeck object and displays searchnotes, 
        also handles the position of OPEN STRING markers.
        :return: 
        '''
        s = 0
        n = 0
        if self.colorBlindMode:
            colors = ColorBlind_Colors[:]
        else:
            colors = Default_Colors[:]
        arpnotes = [searchnotes[i] for i in [0, 2, 4, 6]]

        for string in self.neck.NECK:
            for note in string:

                if note in searchnotes:
                    color = gray
                    size = self.grayNoteSize
                    if note in arpnotes:
                        color = colors[arpnotes.index(note)]
                        size = self.colorNoteSize

                    if n == 0:
                        if self.DotMode:
                            d = NoteDot(self.NotePositions[n],
                                        self.StringPositions[s],
                                        note,
                                        color,
                                        Display = self,
                                        size= self.OpenStringNoteSize,
                                        shift=7,
                                        canvas = self.canvas)
                        else:

                            d = SHAPES.genShape(self.NotePositions[n], self.StringPositions[s], Display=self,
                                                 note=note, size=self.colorNoteSize, fill=color)
                    else:
                        if self.DotMode:
                            d = NoteDot(self.NotePositions[n],
                                        self.StringPositions[s],
                                        note,
                                        color,
                                        Display = self,
                                        size = size,
                                        canvas = self.canvas)
                        else:
                            d = SHAPES.genShape(self.NotePositions[n], self.StringPositions[s], Display=self,
                                                 note=note, size=self.colorNoteSize, fill=color)
                    self.note_object_list.append(d)
                    # self.note_object_list.append(shape)

                n += 1
            s += 1
            n = 0



    # -------- Creating Display details/lower half --------- #
    # ################################### #

    def draw_string_labels(self):
        canvas3 = Canvas(self.window, width=25, height=self.C_HEIGHT, bg=lightGray, highlightbackground = lightGray)  # 4B2D00')
        canvas3.place(x= (self.buff - self.buff/5 - 10), y=10, anchor='n')

        canvas4 = Canvas(self.window, width=25, height=self.C_HEIGHT, bg=lightGray, highlightbackground = lightGray)# 4B2D00')
        canvas4.place(x=(self.W_WIDTH - (self.buff / 5) * 4) + 10, y=10, anchor='n')
        n = 0
        for string in self.neck.NECK:
            canvas3.create_text(15, self.StringPositions[n], text='- ' + string[0], font='Arial 14 bold')
            canvas4.create_text(15, self.StringPositions[n], text=string[0] + ' -', font='Arial 14 bold')
            n += 1

    def draw_color_key(self, replace=False):
        '''
        creates second canvas under the Display canvas.
        shows Colors relating to Root, 3rd, 5th, 7th.
            *** COLORS ACCESSED FROM MASTER LIST AT TOP ***
        :param color:  Color grabbed from color_pallet list
        :return: 
        '''



        self.canvas2 = Canvas(self.window, width=self.W_WIDTH - 20, height=self.W_HEIGHT - (self.C_HEIGHT + 20), bg=lightn(lightGray, 20),
                         bd=0, relief=SUNKEN, highlightbackground=shade(lightGray, 50))  # 4B2D00')

        self.canvas2.place(x=self.W_WIDTH / 2, y=20 + self.C_HEIGHT, anchor='n')

        def block(x, y, color='black', label='', note=''):
            size = 15

            self.canvas2.create_rectangle(x + size, y + size / 2, x - size, y - size / 3, fill=color)
            self.canvas2.create_text(x, y + 2, text=note, font='Arial 13 bold')
            self.canvas2.create_text(x + size + 10, y, text=label, font="Arial 15", anchor='w')

        sections = self.W_WIDTH / 10
        row_y = 20
        label = 'Notes: - '
        for note in self.KeyNotes:
            label += note + ' - '
        if len(self.KeyNotes) == 7:
            arp = [self.KeyNotes[n] for n in [0, 2, 4, 6]]
        else:
            arp = self.KeyNotes[:]

        # canvas2.create_line(0,3,W_WIDTH,3, width = 4)
        # canvas2.create_line(0, 3, W_WIDTH, 3,fill = 'white' ,width=2)
        # canvas2.create_line(3, 3, 3, W_HEIGHT, fill=black, width=4)
        # canvas2.create_line(3, 3, 3, W_HEIGHT, fill = 'white',width=2)
        # canvas2.create_line(W_WIDTH-20, 3, W_WIDTH-20, W_HEIGHT, fill=black, width=4)
        # canvas2.create_line(W_WIDTH-20, 3, W_WIDTH-20, W_HEIGHT, fill='white', width=2)


        color = 'black'
        for n in self.note_object_list:
            if n.note.capitalize() == arp[0]:
                color = n.color
                
                break


        self.canvas2.create_text(sections * 1.5, row_y, text=label, font='Arial 13')
        block(sections * 3, row_y, color, 'Root', note=arp[0])
        # canvas2.create_text(60, 50, text = 'ROOT')

        for n in self.note_object_list:
            if n.note.capitalize() == arp[1]:
                color = n.color

                break

        block(sections * 4, row_y, color, 'Third', note=arp[1])

        for n in self.note_object_list:
            if n.note.capitalize() == arp[2]:
                color = n.color

                break

        block(sections * 5, row_y, color, 'Fifth', note=arp[2])

        for n in self.note_object_list:
            if n.note.capitalize() == arp[3]:
                color = n.color

                break
        block(sections * 6, row_y, color, 'Seventh', note=arp[3])

    def replace_color_key(self):
        self.canvas2.delete()
        self.draw_color_key(replace = True)

    def draw_arp_name(self):

        self.canvas4 = Canvas(self.window, width=self.W_WIDTH/4, height=self.W_HEIGHT - (self.C_HEIGHT + 30),
                         bg=lightn(lightGray, 20),
                         bd=0, relief=SUNKEN, highlightbackground=lightn(lightGray,20))  # 4B2D00')
        self.canvas4.place( x = self.W_WIDTH - self.W_WIDTH/6, y = self.W_HEIGHT - 40, anchor = 'n')
        if len(self.search_notes) == 7:
            text = self.p_notes[0].capitalize() + self.arp_names[self.KeyNotes.index(self.p_notes[0])][0] + ' -- ' + self.arp_names[self.KeyNotes.index(self.p_notes[0])][1]


            self.canvas4.create_text(10, 20, text=text, font='Arial 20 bold', fill = 'black', anchor = 'w')
        else:
            pass ##### --------- HANDLE 7th ARP INVERSIONS ------- #


    def refresh_arp_name(self):
        self.canvas4.delete()
        self.draw_arp_name()






    # refresh -- ALL

    def GOTCLICK(self, note_dot, color=red):
        # print(note_dot.note)
        note_dot.replaceDot(self.canvas)
        searchnotes = self.search_notes[:]
        x = note_dot.x
        y = note_dot.y
        note = note_dot.note
        size = note_dot.defaultSize

        # print('sss',working_notes)
        if color == gray:
            size = self.grayNoteSize
        else:
            size = self.colorNoteSize
        if x == self.NotePositions[0]:
            size = self.OpenStringNoteSize

        if type(note_dot) == NoteDot:
            note_dot.__init__(x, y, note, color, size = size, Display = self, shift=note_dot.shift, canvas = self.canvas)
        else:

            s = SHAPES.genShape(x, y, note, color, size = size, Display = self, shift=note_dot.shift, canvas = self.canvas)
            self.note_object_list.insert(self.note_object_list.index(note_dot), s)
            self.note_object_list.remove(note_dot)


    def ALL(self, newRoot_Dot):




        newNotes = []
        # print(len(self.note_object_list))
        for n in self.note_object_list:

            if n.note not in newNotes:


                newNotes.append(n.note)


        while newRoot_Dot.note != newNotes[0]:
            newNotes = newNotes[1:] + [newNotes[0]]

        if len(newNotes) <= 4:

            for n in self.note_object_list:
                newColor = self.color_pallet[newNotes.index(n.note)]

                self.GOTCLICK(n, newColor)

        else:

            arp = [newNotes[i] for i in [0, 2, 4, 6]]
            for n in self.note_object_list:
                if n.note in arp:
                    newColor = self.color_pallet[arp.index(n.note)]
                else:
                    newColor = gray
                self.GOTCLICK(n, newColor)

        self.p_notes = newNotes[:]
        self.draw_color_key(replace = True)
        self.refresh_arp_name()

        '''
        # redraws L and R border -- stylistic only.
        for b in black_bars:

            canvas.delete(b)
        #print(len(black_bars))
        while len(black_bars) != 0:
            black_bars.pop()
        #print(len(black_bars))
        draw_border()
        #print(len(black_bars))
        '''






#
#
# S = ['C','D','E','F','G','A','B']
# A = ['C','E','G','B']
#
# root = Tk()
#
# c = Display('C', window_root = root, numOfStrings= 6, searchNotes= S, colorBlindMode= False)
#
#
#
# #d = SHAPES.DIAMOND(100, 100, c.canvas, 10, 'red')
#
#
#
#
# root.mainloop()
