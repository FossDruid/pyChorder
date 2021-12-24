# pyChorder V0.1B -
# Todo.  1 - Supports only Capital characters so far.  2 - Add more modes.  3 - Add chord formation function ( Triads and 7ths)

# Regex for later 
import re

# index 0 Sharps, index 1 Flats
musicalAlphabet = [['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'], ['A','B♭', 'B', 'C♭', 'C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G']]

#  Whole and Half notes presented as 2 & 1, with respect to indicies
W = 2
H = 1

majorScaleFormula = [W, W, H, W, W, W, H]
minorScaleFormula = [W, H, W, W, H, W, W]

def scaleMaker(rootNote, mAlphabetList, scaleFormula):
    # W W H W W W H
    mAlphabetLength = (len(mAlphabetList)-1) #  With respect to indicies
    rootNoteIndex = mAlphabetList.index(rootNote)
    rootScale = []
    rootScale.append(mAlphabetList[rootNoteIndex])

    prevNoteIndex = rootNoteIndex
    # 0->6 because there are 7 notes in a major scale.
    newIndex = int
    for i in range (0,6):
        prevNoteIndex += scaleFormula[i]
        if (prevNoteIndex > mAlphabetLength):
            newIndex = (prevNoteIndex - mAlphabetLength)
            prevNoteIndex = (newIndex-1)
        rootScale.append(mAlphabetList[prevNoteIndex])
    print(rootScale)

rootNote = 'C'
scaleMaker(rootNote, musicalAlphabet[0], minorScaleFormula)
