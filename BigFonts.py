import pickle
from typing import TypeAlias
from enum import Enum, unique, auto

"""
TODO: 
 - [ ] Make a text to bigfonts function makeFontText
"""

STRINGLIST: TypeAlias = list[str]
STRINGTUPLE: TypeAlias = tuple[str]

class Glom(Enum):
    w0 = 0
    w1 = auto()
    W = auto()
    space = auto()
    g0 = auto()
    g_2 = auto()
    notset = auto()

@unique
class Slant(Enum):
    bck = -1
    cntr = 0
    fwd = 1
    notset = auto()

def _append_char_space(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, is_last_char:bool, glomspacestr:str) -> None: 
    for i in range(nlines):
        textOutput[i] += chartuple[i] + glomspacestr*is_last_char 

def _getOT(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, w:int)->int:
    #determine the offset, how far forward (padding=positive output) or back (overlapping = negative output)
    #the two letter in chartuple should be relative to the text in textOutput.
    Deltas = []
    for i in range(nlines):
        L = 0
        for j, c in enumerate(textOutput[i][::-1]):
            L=j
            if c != ' ':
                break
        R = 0
        for j, c in enumerate(chartuple[i]):
            R=j
            if c != ' ':
                break
        Deltas.append(L-R)
    return w - min(Deltas)

def _append_char_w(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, is_last_char:bool, w:int) -> None: 
    #w = 0 is glom=w=w0 #collide white space overlaps, 
    #w=1 is glom=w1 #collide white space overlaps but keep 1 space between non-white space characters
    ot = _getOT(textOutput, chartuple, nlines, w) 
    if ot >= 0:
        for i in range(nlines):
            textOutput[i] += ' '*ot + chartuple[i] 
    else:
        for i in range(nlines):
            for o in range(ot):
                if textOutput[i][o-ot] == ' ':
                    textOutput[i][o-ot] == chartuple[i][o]
            textOutput[i] += chartuple[i][ot:]

def _append_char_W(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, is_last_char:bool, char:str) -> None:
    #glom=W #collide white space overlaps, except for caps
    _append_char_w(textOutput, chartuple, nlines, is_last_char, int(char.isupper()))

def _append_char_g0(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, is_last_char:bool) -> None:
    #glom=g0 #glom with at most 1 differences allowed, prefering the letter to the right
    #TODO
    #This should probably be merged with _append_char_g_2
    pass

def _append_char_g_2(textOutput:STRINGLIST, chartuple:STRINGTUPLE, nlines:int, is_last_char:bool, g_num:int) -> None:
    #glom=g-2 # g_num = -2. glom with at most 2 differences allowed, prefering the letter to the left (except punctuation which keeps right-pref.)
    #so what I had been calling "0" is still 0. What I had been calling 1 is now usually g0 or g1
    #TODO g number can vary, and can be positive or negative.
    
    #My best guess as to what I meant by this was that the integer represetned the number of allowed differences
    #with negative numbers prefering the left letter, and positive numbers prefering the right
    #but the fonts are more complex than that, and can switch. 
    pass

class Font:
    def __init__(self, lines:int=-1, glom:type[Glom]=Glom.notset, slant:type[Slant]=Slant.notset, space:int=-1, name:str="myfont")->None:
        self.lines = lines
        self.setSpace(space)
        self.slant = slant
        self.glom = glom
        self.name = name
        self.charMap = {}
        #charMap is the main container of font data. 
        #It's a a map from characters to tuples (length lines) of strings.
        #charmap has a special character "slantstart" which starts each string, initalizing the slant.
    def getChar(self,char:str) -> STRINGTUPLE:
        if char in self.charMap:
            return self.charMap[char]
        else:
            return tuple('' for _ in range(self.lines))
    def getFileName(self) -> str:
        return self.name+".fontpkl"
    def save(self) -> None:
        with open(self.getFileName(), 'wb') as f:
            pickle.dump(self, f)
    def makeFontText(self, textInput:str) -> STRINGLIST: 
        textOutput = ["",]*self.lines
        textInputLen = len(textInput)
        if textInputLen == 0:
            return textOutput 

        if self.glom == Glom.notset:
            print("Error! Finalizing a font with no Glom set")
            return

        for i in range(self.lines):
            textOutput[i] += self.charMap["slantstart"][i]

        for i, c in enumerate(textInput):
            is_last_char = i==textInputLen-1
            if c in self.charMap:
                chartuple = self.getChar(c)
                if self.glom == Glom.w0:
                    #glom=w=w0 #collide white space overlaps
                    _append_char_w(textOutput, chartuple, self.lines, is_last_char, 0)
                elif self.glom == Glom.w1:
                    #glom=w1 #collide white space overlaps but keep 1 space between non-white space characters
                    _append_char_w(textOutput, chartuple, self.lines, is_last_char, 1)
                elif self.glom == Glom.W:
                    #glom=W #collide white space overlaps, except for caps
                    _append_char_W(textOutput, chartuple, self.lines, is_last_char, c)
                elif self.glom == Glom.space:
                    #trivial case, just put glomspaceStr inbetween letters and everything is even
                    _append_char_space(textOutput, chartuple, self.lines, is_last_char, self.glomspacerStr)
                elif self.glom == Glom.g0:
                    #glom=g0 #glom with at most 1 differences allowed, prefering the letter to the right
                    _append_char_g0(textOutput, chartuple, self.lines, is_last_char)
                elif self.glom == Glom.g_2:
                    #glom=g-2 #glom with at most 2 differences allowed, prefering the letter to the left (except punctuation which keeps right-pref.)
                    #so what I had been calling "0" is still 0. What I had been calling 1 is now usually g0 or g1
                    _append_char_g_2(textOutput, chartuple, self.lines, is_last_char, c, self.g_num)
            elif c == ' ':
                self._addSpace(textOutput)
            else:
                print(f"Warning: unrecognized character '{c}' for this font")
                continue
    def _addSpace(self, textOutput:STRINGLIST) -> None:
        #Append a space for this font to textOutput 
        for i in range(self.lines):
            textOutput[i] += self.spaceStr
    def setGlom(self,glomstr:str) -> None:
        glomdict = { "w":Glom.w-1, "w0":Glom.w0, "w1":Glom.w1, "W":Glom.W}
        if glomstr in glomdict:
            self.glom = glomdict[glomstr]
        elif glomstr.isdigit():
            self.glom = Glom.space
            self.glomspace = int(glomstr)
            self.glomspacerStr = ' '*self.glomspace
        elif glomstr[0]=='g':
            self.glom = Glom.g_2
            self.g_num = int(glomstr[1:])
            if self.g_num == 0:
                self.glom = Glom.g0
        else:
            print("Error, unrecognized glom string ",glomstr)
    def setSlant(self,slantstr:str) -> None:
        slantdict = {"0":Slant.cntr,"1":Slant.fwd,"-1":Slant.bck}
        if slantstr in slantdict:
            self.slant = slantdict[slantstr]
        else:
            print("Error, unrecognized slant string ",slantstr)
    def setSpace(self,space:int) -> None:
        self.space = space
        self.spaceStr = " "*max(0,space)
