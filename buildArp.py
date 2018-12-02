def parse(string):
    NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    #               0    1     2    3     4    5    6     7    8     9    10    11

    CHROMATIC = []

    major_scale_index = [0, 2, 4, 5, 7, 9, 11]
    minor_scale_index = [0, 2, 3, 5, 7, 8, 10]
    harmonic_minor_scale_index = [0, 2, 3, 5, 7, 8, 11]

    maj_arp_index = [0, 4, 7, 11]
    min_arp_index = [0, 3, 7, 10]
    dom_arp_index = [0, 4, 7, 10]
    dim7_arp_index = [0, 3, 6, 9]
    d7b5_arp_index = [0, 4, 6, 10]
    min7b5_arp_index = [0, 3, 6, 10]

    harm = [0, 3, 7, 11]
    def rotate(lst):
        return lst[1:] + [lst[0]]
    root = ''
    name = ''
    if (string[1] == '#') or (string[1] == 'b'):
        root = string[:2]
        name = string[2:]
    else:
        root = string[:1]
        name = string[1:]


    def construct_arp(root, name):

        notes = []
        name = name.lower()
        root = root.capitalize()



        types = {
            'maj': maj_arp_index,
            'major': maj_arp_index,
            'maj7': maj_arp_index,

            'min': min_arp_index,
            'minor': min_arp_index,
            'min7': min_arp_index,

            'dom': dom_arp_index,
            '7': dom_arp_index,

            'dim7': dim7_arp_index,
            'dim': dim7_arp_index,

            '7b5' : d7b5_arp_index,
            'min7b5': min7b5_arp_index
                 }



        if root in NOTES_SHARP:
            notes = NOTES_SHARP[:]
        elif root in NOTES_FLAT:
            notes = NOTES_FLAT[:]
        else:
            print('INVALID TONIC ERROR')
        def build(r, type, lst):
            while lst[0] != r:
                lst = rotate(lst)

            type = type.strip()

            if type in types.keys():
                return [ lst[i] for i in types[type] ]
            else:
                print('something went sideways')


        return build(root,name, notes)

    return construct_arp(root, name)


def rotate(lst):
    return lst[1:] + [lst[0]]
def buildMode(note, mode):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    ionian = [0, 2, 4, 5, 7, 9, 11]
    dorian = [0,2,3,5,7,9,10]
    phrygian = [0,1,3,5,7,8,10]
    lydian = [0, 2, 4, 6, 7, 9, 11]
    mixolydian = [0, 2, 4, 5, 7, 9, 10]
    aeolian = [0, 2, 3, 5, 7, 8, 10]
    locrian = [0, 1, 3, 5, 6, 8, 10]
    harm_minor = [0, 2, 3, 5, 7, 8, 11]

    while notes[0] != note:
        notes = rotate(notes)

    modes = {'Ionian (major)' :ionian,
             'Dorian' :dorian,
             'Phrygian' :phrygian,
             'Lydian' :lydian,
             'Mixolydian' :mixolydian,
             'Aeolian (minor)' :aeolian,
             'Locrian' :locrian,
             'Harmonic minor': harm_minor}

    outp = [notes[i] for i in modes[mode]]

    return outp

def buildScale(note, scale):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    ionian = [0, 2, 4, 5, 7, 9, 11]
    dorian = [0,2,3,5,7,9,10]
    phrygian = [0,1,3,5,7,8,10]
    lydian = [0, 2, 4, 6, 7, 9, 11]
    mixolydian = [0, 2, 4, 5, 7, 9, 10]
    aeolian = [0, 2, 3, 5, 7, 8, 10]
    locrian = [0, 1, 3, 5, 6, 8, 10]
    harm_minor = [0, 2, 3, 5, 7, 8, 11]

    while notes[0] != note:
        notes = rotate(notes)

    modes = {'Ionian (major)' :ionian,
             'Dorian' :dorian,
             'Phrygian' :phrygian,
             'Lydian' :lydian,
             'Mixolydian' :mixolydian,
             'Aeolian (minor)' :aeolian,
             'Locrian' :locrian}

    outp = [notes[i] for i in modes[scale]]

    return outp

#print(buildMode('D',"Dorian"))
