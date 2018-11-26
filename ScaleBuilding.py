
NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOTES_FLAT =  ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
#               0    1     2    3     4    5    6     7    8     9    10    11

CHROMATIC = []

major_scale_index = [0,2,4,5,7,9,11]
minor_scale_index = [0,2,3,5,7,8,10]
harmonic_minor_scale_index = [0,2,3,5,7,8,11]

maj_arp_index = [0,4,7,11]
min_arp_index = [0,3,7,10]
dom_arp_index = [0,4,7,10]
harm = [0,3,7,11]


def rotate(lst):
    return lst[1:] + [lst[0]]

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
        print(root)
        notes = []

        types = {'maj' : maj_arp_index,
                 'major' : maj_arp_index,
                 'maj7' : maj_arp_index,

                 'min' : min_arp_index,
                 'minor' : min_arp_index,
                 'min7' : min_arp_index,

                 'dom' : dom_arp_index,
                 '7' : dom_arp_index}



        if root in NOTES_SHARP:
            notes = NOTES_SHARP[:]
        elif root in NOTES_FLAT:
            notes = NOTES_FLAT[:]
        else:
            print('INVALID TONIC ERROR')
        def build(r, type, lst):
            while lst[0] != r:
                lst = rotate(lst)

            if type in types.keys():
                return [ lst[i] for i in types[type] ]
            else:
                print('something went sideways')


        return build(root,name, notes)

    return construct_arp(root, name)



x = parse('G7')
print(x)

def get_arpeggio(rootNote, arpType):
    '''
    
    #:param scale:  ======  [LIST] of chromatic notes to be used (sharps or flats)
    :param rootNote: ====  "String" root note of arpeggio ('C' 'D#' 'Eb')
    :param arpType:  ====  [LIST] of indexes to be used on CHROMATIC SCALE
    :return: ------- [LIST] of notes of arppeggio
    '''

    NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    scale = NOTES_SHARP[:]
    arp = []
    def useSharps():
        chrom_notes = NOTES_SHARP[:]
        while rootNote != chrom_notes[0]:
            chrom_notes = rotate(chrom_notes)

        arp = []
        for i in arpType:
            arp.append(chrom_notes[i])

        return arp

    def useFlats():
        chrom_notes = NOTES_FLAT[:]

        while rootNote != chrom_notes[0]:
            chrom_notes = rotate(chrom_notes)

        arp = []
        for i in arpType:
            arp.append(chrom_notes[i])

    def NoDups(arpeggio):
        #print('checking')
        check = []
        for note in arpeggio:
            if note not in check:
                check.append(note[0])
            else:

                return False

        return True

    if rootNote in NOTES_SHARP:
        arp = useSharps()
        #print(arp)
        if NoDups(arp):
            return arp
        else:
            #arp = useFlats()
            #print('no')
            return arp


    elif rootNote in NOTES_FLAT:
        arp = useFlats()
        if NoDups(arp):
            #print(arp)
            return arp
        else:
            #arp = useSharps()
            #print('no')
            return arp



    else:
        print('invalid input')



    return arp









#print(go)