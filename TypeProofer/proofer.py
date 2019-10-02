from drawBot import *
import random
import sys
import datetime
import os
import glob
from fontTools import ttLib

sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/')

#This document doesn’t need to be included yet
#from UDHR import *

from MiscWords import *


#==========================================
#Document Size and Margin information

size('Letter')

margin = 40
lineGap = -20
marginWidth = width() - margin*2
marginHeight = height() - margin*2
h = height()

#==========================================
#Foundry

foundryName = 'JTD, LLC'

#==========================================
#Fonts

#location of the fonts which you want to proof
fontPath = '/Users/jtd/JTD Type Dropbox/JTD/TypeTools/TypeProofer/prooferFonts/'

#name of the font being proofed
fontName = 'Elfreth'

#font size for the proofs
proofFontSize = 36

fontVers = '191001V4'
titleFont = 'Elfreth%s-Black' % fontVers


captionFont = 'ArrayMonoV1001-Regular'
captionSize = 9

fontFamily = []

for files in glob.glob(f'{fontPath}*.otf'):
    fontFamily.append(files)
    fontFamily.sort()
    print(fontFamily)


#==========================================
#Misc Variables

now = datetime.datetime.now()
year = now.strftime("%Y")

#==========================================
#Misc Functions
             
#Kerning/Spacing Function with uses individual lists for each letter
def kernGuy(fSize,letterString,pageLength):
    newPage(width(), pageLength)
    header()
    #logo()
    translate(0, height()-margin)
    save()
    for fName in fontFamily:

        txtHeight = (marginHeight * 2) / len(fontFamily)
        fs = FormattedString(
            letterString,
            font=fName,
            fontSize=fSize,
            lineHeight=40,
            fill=0,
            align="left"
        )
        translate(0, -txtHeight)
        t = textBox(fs, (margin, (0-(margin / 2)), marginWidth, txtHeight))

    restore()


#Kerning/Spacing Function Version 2 which uses tuples instead of individual lists
def kernGuy2(fSize,pageLength):
    for a in ucWords:
        primaryLetter,text = a
        t = ''
        t += f"{text}"
        newPage(width(), pageLength)
        header()
        caption(f"{primaryLetter}", 0,50)

        translate(0, height()-margin)
        save()
        for fName in fontFamily:

            txtHeight = (marginHeight * 2) / len(fontFamily)
            fs = FormattedString(
                t,
                font=fName,
                fontSize=fSize,
                lineHeight=fSize * 1.1,
                fill=0,
                align="left"
            )
            translate(0, -txtHeight)
            f = textBox(fs, (margin, ((margin / 4)), marginWidth, txtHeight))            
        restore()

#==========================================
#Universal Elements For Each Page

def header():

    fs = FormattedString(
        now.strftime("%Y-%m-%d %H:%M"), 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="left"
    )
    text(fs, (margin, 40))  
    
    fs = FormattedString(
        fontName, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="center"
    )
    textBox(fs, (0,9,width(),40))  

    foundryCopyright = f'© {foundryName} {year}'
    
    fsRight = FormattedString(
        foundryCopyright, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="right"
    )
    text(fsRight, (width()-margin-90, 40)) 
    
    

def caption(captionText,x,y):
    fs = FormattedString(
        captionText, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="center"
    ) 
    textBox(fs, (x,y,width(),20))
    
#==========================================
#Title Page

PageName = ""
header()

fs = FormattedString(
        fontName, 
        font=titleFont,
        fontSize=120,
        fill=0,
        align="center"
    )
textBox(fs, (0, 330, width(), 158))


#==========================================
#Proofing Pages

PageName = fontName
kernGuy2(proofFontSize,(height() * 2))

PageName = fontName
kernGuy(proofFontSize,lcASpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcLSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcSSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcTSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcUSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcVSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcWSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcXSpacing,(h* 2))

PageName = fontName
kernGuy(proofFontSize,lcYSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,lcZSpacing,(h * 2))

PageName = fontName
kernGuy(proofFontSize,numberWords,(h * 2))



#==========================================
#Export
path = "/Users/jtd/Documents/DeleteStuff/JTD_Proof_%s.pdf" % fontName
saveImage(path)

# open the in Safari
import os
os.system(f"open -a Safari {path}")
