from drawBot import *
import random
import sys
import datetime
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

foundryCopyright = '© JTD, LLC 2019'

#==========================================
#Fonts
fontVers = '191001V4'
fontName = 'Elfreth'
myFontLight = 'Elfreth%s-Light' % fontVers
myFontReg = 'Elfreth%s-Regular' % fontVers
myFontBold = 'Elfreth%s-Bold' % fontVers
myFontBlack = 'Elfreth%s-Black' % fontVers

#fontFamily = [myFontLight, myFontReg, myFontBold, myFontBlack]

proofFontSize = 36


captionFont = 'ArrayMonoV1001-Regular'
captionSize = 9

PageName = fontName

fontFamily = []

import os
for file in os.listdir('/Users/jtd/JTD Type Dropbox/JTD/TypeTools/TypeProofer/TypeProofer/prooferFonts'):
    if file.endswith(".otf"):
        fontFamily += [file]
        print(file)

#fontFamily = []


#==========================================
#Misc Functions
             
#Kerning/Spacing Function with uses individual strings for each letter
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


#Kerning/Spacing Function Version 2 which uses tuples instead of individual strings
def kernGuy2(fSize,pageLength):
    t = ''
    for a in ucWords:
        primaryLetter,text = a
        t += f"{text}"
        newPage(width(), pageLength)
        header()
        #logo()
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
            f = textBox(fs, (margin, (0-(margin / 2)), marginWidth, txtHeight))

            
        restore()
        caption(f"{primaryLetter}", 0,0)

#==========================================
#Universal Elements

def header():
    now = datetime.datetime.now()

    fs = FormattedString(
        now.strftime("%Y-%m-%d %H:%M"), 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="left"
    )
    text(fs, (margin, 40))  
    
    fs = FormattedString(
        PageName, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="center"
    )
    textBox(fs, (0,9,width(),40))  

    
    fsRight = FormattedString(
        foundryCopyright, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="right"
    )
    text(fsRight, (width()-margin-90, 40)) 
    
def logo():
    path = '/Users/jtd/Your team Dropbox/JTD/Assets/LogoLibrary/190428/JTD_NoBox.png'
    logo = ImageObject(path)
    
    lW, lH = imageSize(path)
    

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
#Page 1

PageName = ""
header()

fs = FormattedString(
        fontName, 
        font=myFontBlack,
        fontSize=120,
        fill=0,
        align="center"
    )
textBox(fs, (0, 320, width(), 158))

fs = FormattedString(
    'Designed By James Hultquist-Todd\n4 Weights\nDesigned in 2019',
    font=captionFont,
    fontSize=captionSize,
    align="center"
    )
textBox(fs, (0, 140, width(), 80))

logo()


#==========================================
#Page 4

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
