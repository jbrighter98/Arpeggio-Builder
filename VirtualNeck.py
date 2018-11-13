class Neck():
    def __init__(self, searchnotes=[], instrument = 'guitar', tuning = ['D','A','D','G','B','E'], sharp_o_flat = 'sharp'):
        #print("print bass neck")
        #print(searchnotes)
        self.tuning = tuning
        self.instrument = instrument
        self.sharpORflat = sharp_o_flat
        self.searchFor = searchnotes[:]



        self.NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        self.USE_FLATS = False
        self.FLATNOTES = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']

        for n in self.tuning:
            if n in self.FLATNOTES:
                self.sharpORflat = 'flat'

        self.create_notes_for_neck()






    def create_notes_for_neck(self, searchnotes = []):

        if self.sharpORflat == 'flat':
            self.NOTES = self.NOTES_FLAT[:]

        else:
            self.NOTES = self.NOTES_SHARP[:]



        self.E_string = self.getString(self.tuning[0], self.NOTES[:])
        self.A_string = self.getString(self.tuning[1], self.NOTES[:])
        self.D_string = self.getString(self.tuning[2], self.NOTES[:])
        self.G_string = self.getString(self.tuning[3], self.NOTES[:])

        self.B_string = self.getString(self.tuning[4], self.NOTES[:])
        self.e_string = self.getString(self.tuning[5],self.NOTES[:])

        self.guitar = [self.e_string,
                       self.B_string,
                       self.G_string,
                       self.D_string,
                       self.A_string,
                       self.E_string]
        self.bass = self.guitar[-4:]

        if self.instrument == 'bass':
            self.NECK = self.bass[:]
        elif self.instrument == 'guitar':
            self.NECK = self.guitar[:]

    def getString(self, string, scale):
        while scale.index(string) > 0:
            scale.append(scale[0])
            scale = scale[1:]
        scale.append(scale[0])
        return scale





    # def display_neck(self, LOOKNOTE=[]):
    #     self.create_notes_for_neck(LOOKNOTE)
    #     for fret in range(len(self.NECK[0])):
    #         print('   ' + str(fret).ljust(5), end='')
    #         for string in self.NECK:
    #             if string[fret] == LOOKNOTE[0]:  # and start<=fret<=end:   ###### CIRCLES ROOT NOTE
    #                 rootnote = '('+string[fret]+')'
    #                 print('|' + rootnote.center(4), end='')
    #             elif string[fret] in LOOKNOTE:  # and start<=fret<=end:
    #                 print('|' + string[fret].center(3), end=' ')
    #             else:
    #                 if fret in [3,5,7,9,12]:
    #                     print('| . ', end=' ')
    #                 else:
    #                     print('|   ', end=' ')
    #
    #         print('|')
    #         print(' ' * 8, end='')
    #         for string in self.NECK:
    #             print('|   ', end=' ')
    #         print('|')
    #         print(' ' * 8 + '------' * len(self.NECK))
    #         print(' ' * 8, end='')
    #         for string in self.NECK:
    #             print('|   ', end=' ')
    #         print('|')


#######################################################

#neck = Neck()

#neck.display_neck(['F'])#,'A','C','E'])
