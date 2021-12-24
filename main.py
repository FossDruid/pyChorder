# pyChorder V0.1A -
# Todo.  1 - Supports only Capital characters so far.  2 - Add minor scale and other modes.  3 - Add chord function ( Triads and 7ths)

# Regex for later 
import re

# index 0 Sharps, index 1 Flats
musicalAlphabet = [['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'], ['A','B♭', 'B', 'C♭', 'C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G']]

#  Whole and Half notes presented as 2 & 1, with respect to indicies
W = 2
H = 1

def majorScale(rootNote, mAlphabetList, w, h):
    # W W H W W W H
    mAlphabetLength = (len(mAlphabetList)-1) #  With respect to indicies
    majScaleFormula = [w, w, h, w, w, w, h]
    rootNoteIndex = mAlphabetList.index(rootNote)
    rootMajScale = []
    rootMajScale.append(mAlphabetList[rootNoteIndex])

    prevNoteIndex = rootNoteIndex
    # 0->6 because there are 7 notes in a major scale.
    newIndex = int
    for i in range (0,6):
        prevNoteIndex += majScaleFormula[i]
        if (prevNoteIndex > mAlphabetLength):
            newIndex = (prevNoteIndex - mAlphabetLength)
            prevNoteIndex = (newIndex-1)
        rootMajScale.append(mAlphabetList[prevNoteIndex])
    print(rootMajScale)

rootNote = 'A#'
majorScale(rootNote, musicalAlphabet[0], W, H)
