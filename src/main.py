# pyChorder V0.1D - With user input

# Todo.  1 - Supports only Capital characters so far.  2 - Add more modes. 3 - Refactor.  4 - Add all formulas and alphabets to json? 5 - Rename some variales and function parameters

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
ninthChord = [0,2,4,6,8]
rootScale = []

def scaleMaker(rootNote, rootScale,  mAlphabetList, scaleFormula):
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

# Todo. 1-Choose between accidentals. 2-Error handling if a note dosent exist (forex E#)
# Only capital!     -- HARDCODED -- FIX THIS, WORKS FOR NOW
rootNote = input("Enter your wanted root note ( Capital, accidentals: # or ♭)")
usrScale = input("[Major] or [Minor] Scale: ")
if(usrScale == "Major"):
    scaleMaker(rootNote, rootScale, musicalAlphabet[0], majorScaleFormula)
if(usrScale == "Minor"):
    scaleMaker(rootNote, rootScale, musicalAlphabet[0], minorScaleFormula)

# Safe old way
#scaleMaker(rootNote, rootScale,  musicalAlphabet[0], majorScaleFormula)
#chordMaker(rootScale, seventhChord, majorScaleFormula)#< Same variable^
