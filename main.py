# pyChorder V0.1C -
# Todo.  1 - Supports only Capital characters so far.  2 - Add more modes.

# Regex for later 
import re

# index 0 Sharps, index 1 Flats
musicalAlphabet = [['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'], ['A','B♭', 'B', 'C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭']]

#  Whole and Half notes presented as 2 & 1, with respect to indicies
W = 2
H = 1

# Scale formulas
majorScaleFormula = [W, W, H, W, W, W, H]
minorScaleFormula = [W, H, W, W, H, W, W]

# Chord formulas
triadChord = [0,2,4]
seventhChord = [0,2,4,6]

rootScale = []
def scaleMaker(rootNote, rootScale,  mAlphabetList, scaleFormula):
    # W W H W W W H
    mAlphabetLength = (len(mAlphabetList)-1) #  With respect to indicies
    rootNoteIndex = mAlphabetList.index(rootNote)
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

def chordMaker(rootScale, chordFormula, scaleFormula):
    print(f"root note: {rootScale[0]} \nNotes:")
    
    chordFormulaLen = len(chordFormula)

    for i in chordFormula:
        print(rootScale[i])

    if (chordFormulaLen == 3):
            print(f"Chord: {rootScale[0]}")
    elif (chordFormulaLen == 4 and scaleFormula == minorScaleFormula):
            print(f"Chord: {rootScale[0]}m7")
    elif (chordFormulaLen == 4 and scaleFormula == majorScaleFormula):
            print(f"Chord: {rootScale[0]}maj7")


    print("\n")

# Only capital!
rootNote = 'C'                  # # or ♭ (0#, 1♭)    minor or major
scaleMaker(rootNote, rootScale,  musicalAlphabet[0], majorScaleFormula)
chordMaker(rootScale, seventhChord, majorScaleFormula)#< Same variable^
