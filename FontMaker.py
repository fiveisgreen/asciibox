import re
from typing import TypeAlias
import pickle
import BigFonts
"""
TODO: 
 - [ ] Testing
"""
inputFileName = "inputter.txt"

FONTENTRY: TypeAlias = list[str]
FONT: TypeAlias = type[BigFonts.Font]

def Parse_Entry_line(line:str) -> FONT:
    ifont = BigFonts.Font()
    parts = re.split(r'[:,=]', line.strip())
    i = -1
    while i < len(parts)-1:
        i+=1
        ipart = parts[i].strip()
        if i>20:
            print("runaway while")
            break
        elif ipart == "ENTRY":
            ifont.name = parts[i+1].strip()
            i += 1
        elif ipart == "lines":
            ifont.lines = int(parts[i+1].strip())
            i += 1
        elif ipart == "space":
            ifont.setSpace(int(parts[i+1].strip()) )
            i += 1
        elif ipart == "glom":
            ifont.setGlom(parts[i+1].strip())
            i += 1
        elif ipart == "slant":
            ifont.setSlant(parts[i+1].strip())
            i += 1
        else:
            print("What is ",parts[i])
    return ifont

def goto_white_cntr(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first whitespace on all lines
    #all lines are equal, no slant
    #starting_position should be the index of the last character on some line
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        start_char_seen = True #
        for line in lines:
            if starting_position >= len(line):
                return starting_position
            start_char_seen &= line[starting_position] == " " #
    return starting_position 

def goto_white_bck(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first non-whitespace on any line given \ slant
    #presume starting_position represents the top line position
    #starting_position should be the index of the last character on some line
    #based on the top position and slant
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        start_char_seen = True #
        for i in range(len(lines)):
            if starting_position+i >= len(lines[i]):
                return starting_position
            start_char_seen &= lines[i][starting_position+i] == " "
    return starting_position 

def goto_white_fwd(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first non-whitespace on any line given / slant
    #presume starting_position represents the top line position
    #starting_position should be the index of the last character on some line
    #based on the top position and slant
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        start_char_seen = True #
        for i in range(len(lines)):
            if starting_position-i >= len(lines[i]):
                return starting_position
            start_char_seen &= lines[i][min(0,starting_position-i)] == " "
    return starting_position 

def goto_nonwhite_cntr(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first non-whitespace on any line
    #all lines are equal, no slant
    #starting_position should be the index of the last character on some line
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        for line in lines:
            if starting_position >= len(line):
                return starting_position
            start_char_seen |= line[starting_position] != " "
    return starting_position 

def goto_nonwhite_bck(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first non-whitespace on any line given \ slant
    #presume starting_position represents the top line position
    #starting_position should be the index of the last character on some line
    #based on the top position and slant
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        for i in range(len(lines)):
            if starting_position+i >= len(lines[i]):
                return starting_position
            start_char_seen |= lines[i][starting_position+i] != " "
    return starting_position 

def goto_nonwhite_fwd(lines:FONTENTRY, starting_position:int = -1) -> int:
    #seek the index of first non-whitespace on any line given / slant
    #presume starting_position represents the top line position
    #starting_position should be the index of the last character on some line
    #based on the top position and slant
    start_char_seen = False
    while(not start_char_seen):
        starting_position += 1
        for i in range(len(lines)):
            if starting_position-i >= len(lines[i]):
                return starting_position
            start_char_seen |= lines[i][min(0,starting_position-i)] != " "
    return starting_position 

def left_pack_whitespace_guard_fwd(lines:FONTENTRY) -> None:
    nlines = len(lines)
    problems = []
    for i in range(nlines-1):
        if lines[i][:nlines-i] != " "*(nlines-1-i):
            problems.append(i)
    if len(problems) == 0:
        return
    offsets = [0,]
    for p in problems:
        wanted_spaces = nlines -1 -p
        for c in range(wanted_spaces):
            if lines[p][c] != ' ':
                offsets.append(wanted_spaces - c)
    maxoffset = max(offsets)
    #Leftpad whitespace
    if maxoffset == 0:
        print("wtf, how cna maxoffset be 0? left_pack_whitespace_guard_fwd")
    spacer = ' '*maxoffset
    for i in range(nlines):
        lines[i] = spacer + lines[i]

def left_pack_whitespace_guard_bck(lines:FONTENTRY) -> None:
    nlines = len(lines)
    problems = []
    for i in range(1,nlines):
        if lines[i][:i] != " "*i:
            problems.append(i)
    if len(problems) == 0:
        return
    offsets = [0,]
    for p in problems:
        wanted_spaces = p
        for c in range(wanted_spaces):
            if lines[p][c] != ' ':
                offsets.append(wanted_spaces - c)
    maxoffset = max(offsets)
    #Leftpad whitespace
    if maxoffset == 0:
        print("wtf, how cna maxoffset be 0? left_pack_whitespace_guard_bck")
    spacer = ' '*maxoffset
    for i in range(nlines):
        lines[i] = spacer + lines[i]

def finalize_font(ifont:FONT,lines:FONTENTRY,char_sequence:str) -> None:
    if len(lines) != ifont.lines:
        print("Warning! Lines is incorrectly set in font ", ifont.name)
        ifont.lines = len(lines)

    if ifont.slant == BigFonts.Slant.cntr:
        starting_position = -1
        ending_position = -1
        for char in char_sequence:
            starting_position = goto_nonwhite_cntr(lines,ending_position)
            ending_position = goto_white_cntr(lines,starting_position)
            ifont.charMap[char] = tuple(line[starting_position:ending_position] for line in lines)
        ifont.charmap["slantstart"] = tuple("" for i in range(ifont.lines))

    elif ifont.slant == BigFonts.Slant.fwd: #/
        starting_position = -1
        ending_position = -1
        left_pack_whitespace_guard_fwd(lines)
        for char in char_sequence:
            starting_position = goto_nonwhite_cntr(lines,ending_position)
            ending_position = goto_white_cntr(lines,starting_position)
            charlines = []
            for i in range(len(lines)):
                charlines.append(lines[i][starting_position-i:ending_position-i])
            ifont.charMap[char] = tuple(charlines)
        ifont.charmap["slantstart"] = tuple(" "*(ifont.lines - i - 1) for i in range(ifont.lines))
    elif ifont.slant == BigFonts.Slant.bck: #\
        starting_position = -1
        ending_position = -1
        left_pack_whitespace_guard_bck(lines)
        for char in char_sequence:
            starting_position = goto_nonwhite_cntr(lines,ending_position)
            ending_position = goto_white_cntr(lines,starting_position)
            charlines = []
            for i in range(len(lines)):
                charlines.append(lines[i][starting_position+i:ending_position+i])
            ifont.charMap[char] = tuple(charlines)
        ifont.charmap["slantstart"] = tuple(" "*i for i in range(ifont.lines))
    elif ifont.slant == BigFonts.Slant.notset:
        print("Error! Trying to parse an ifont with unsent slant")
    ifont.save()

def Parse_file(inputFileName:str) -> None:
    fonts= {} #a map from font names to font pickel file names
    char_sequence = []
    with open(inputFileName, 'r') as file:
        in_header = True
        lines = []
        ifont = None
        for line in file:
            line = line.strip()
            if line.startswith("ENTRY$"):
                finalize_font(ifont,lines,char_sequence)
                fonts[ifont.name] = ifont.getFileName()
                break
            elif line.startswith("ENTRY"):
                if in_header:
                    in_header = False
                else:
                    finalize_font(ifont,lines,char_sequence)
                    fonts[ifont.name] = ifont.getFileName()
                lines = []
                ifont = Parse_Entry_line(line)
            elif in_header:
                char_sequence = line.split(" ")
            else:
                lines.append(line)
    with open("font_file_map.pcl", 'wb') as f:
            pickle.dump(fonts, f)
    print("Number of fonts: ",len(fonts))

                



            


