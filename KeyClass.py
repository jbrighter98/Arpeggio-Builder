class BassNeck():
    def __init__(self, searchnotes=[]):
        print("print bass neck")
        print(searchnotes)

        self.NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

        self.NOTES = self.NOTES_SHARP[:]

        self.E_string = self.getString('E', self.NOTES[:])
        self.A_string = self.getString('A', self.NOTES[:])
        self.D_string = self.getString('D', self.NOTES[:])
        self.G_string = self.getString('G', self.NOTES[:])

        self.B_string = self.getString('B', self.NOTES[:])

        self.guitar = [self.E_string,
                       self.A_string,
                       self.D_string,
                       self.G_string,
                       self.B_string,
                       self.E_string]
        self.bass = self.guitar[:4]

        self.NECK = self.bass[:]

    def getString(self, string, scale):
        while scale.index(string) > 0:
            scale.append(scale[0])
            scale = scale[1:]
        scale.append(scale[0])
        return scale

    def display_neck(self, LOOKNOTE=[]):
        for fret in range(len(self.NECK[0])):
            print('   ' + str(fret).ljust(5), end='')
            for string in self.NECK:
                if string[fret] in LOOKNOTE:  # and start<=fret<=end:
                    print('|' + string[fret].center(3), end=' ')
                else:
                    print('|   ', end=' ')

            print('|')
            print(' ' * 8, end='')
            for string in self.NECK:
                print('|   ', end=' ')
            print('|')
            print(' ' * 8 + '-----' * len(self.NECK))
            print(' ' * 8, end='')
            for string in self.NECK:
                print('|   ', end=' ')
            print('|')


#######################################################

class Key():
    def __init__(self, root):

        
        self.root = root

        self.NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        
        self.NOTES = []                     # CHROMATIC notes to be used

        self.Scale = []                     # Current Working Scale
        self.Arpeggios = []                 # list of 7th arpeggios for current scale
        ## set to use SHARPS or FLATS
        ## CIRCLE OF 5ths LOGIC
        
        if self.root in self.NOTES_SHARP:
            self.NOTES = self.NOTES_SHARP[:]
        elif self.root in self.NOTES_FLAT:
            self.NOTES = self.NOTES_FLAT[:]

        else:
            print("INVALID NOTE") ### HANDLE WRONG NOTE ENTRY
        ##

        while self.root != self.NOTES[0]:
            self.NOTES = self.rotate(self.NOTES)
        



    def rotate(self, lst):      #working
        #lst.append(lst[0])
        #lst = lst[1:]
        return lst[1:] + [lst[0]]

    def SET_AS_major_scale(self):

        major_intvl_indx = [0, 2, 4, 5, 7, 9, 11]
        self.Scale = [self.NOTES[i] for i in major_intvl_indx]

        self.construct_7th_arpeggios() # AUTOMATICALLY UPDATES ARP LIST
        return self.Scale

    def construct_7th_arpeggios(self):
        temp_scale = self.Scale[:]

        intervals = [0,2,4,6]

        arp = [temp_scale[i] for i in intervals]
        self.Arpeggios.append(arp)
        temp_scale = self.rotate(temp_scale)

        while self.root != temp_scale[0]:
            arp = [temp_scale[i] for i in intervals]
            self.Arpeggios.append(arp)
            temp_scale = self.rotate(temp_scale)

    def get_arpeggios(self):
        self.construct_7th_arpeggios()
        return self.Arpeggios







'''

class Major(Key):
    def __init__(self, root):
        Key.__init__(self, root)
        major_intvl_indx = [0,2,4,5,7,9,11]
        self.Scale = [self.NOTES[i] for i in major_intvl_indx]

    def get_scale(self):
        return self.Scale
    '''
        
            

c = Key('C')
print(c.NOTES)
c.SET_AS_major_scale()



for i in c.Arpeggios:
    print(i)

def chart(notelst):
    major_intvl_indx = [0,2,4,5,7,9,11]
    for note in notelst:
        print(note.ljust(5,'-'), end = '')
    i = 0
    print()
    for note in notelst:
        print(str(i).ljust(5,'-'), end = '')
        i += 1
#chart(c.NOTES)


inp = ''
neck = BassNeck()



for i in c.Arpeggios:
    print("########################################\n"
          "########################################\n"
          "########################################\n"
          "########################################\n"
          "----------------------------------------"
          )
    neck.display_neck(i)
    print(i[0])
    input()





        
