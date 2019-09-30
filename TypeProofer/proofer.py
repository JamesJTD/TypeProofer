from drawBot import *
import random
import sys
import datetime
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/')

from UDHR import *
from MiscWords import *

size('Letter')


w = 612
h = 792


margin = 60
lineGap = -20
marginWidth = w - margin*2
marginHeight = h - margin*2

#==========================================
#Fonts
fontVers = '190928V1'
fontName = 'Elfreth'
myFontLight = 'Elfreth%s-Light' % fontVers
myFontReg = 'Elfreth%s-Regular' % fontVers
myFontBold = 'Elfreth%s-Bold' % fontVers
myFontBlack = 'Elfreth%s-Black' % fontVers

fontFamily = [myFontLight, myFontReg, myFontBold, myFontBlack]

captionFont = 'ArrayMonoV1001-Regular'
captionSize = 9

PageName = fontName

#==========================================
#Misc Functions
            
#Kerning/Spacing Function
def kernGuy(fSize,letter,pageLength):
    newPage(w, pageLength)
    header()
    #logo()
    translate(0, height()-margin)
    save()
    for fontName in fontFamily:

        txtHeight = (marginHeight * 2) / len(fontFamily)
        fs = FormattedString(
            letter,
            font=fontName,
            fontSize=fSize,
            lineHeight=40,
            fill=0,
            align="left"
        )
        translate(0, -txtHeight)
        t = textBox(fs, (margin, (0-(margin / 2)), marginWidth, txtHeight))
    restore()
    captionText = "K"
    caption(0,40)
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
    textBox(fs, (0,9,w,40))  

    
    fsRight = FormattedString(
        '© JTD, LLC 2019', 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="right"
    )
    text(fsRight, (w-margin-90, 40)) 
    
def logo():
    path = '/Users/jtd/Your team Dropbox/JTD/Assets/LogoLibrary/190428/JTD_NoBox.png'
    logo = ImageObject(path)
    
    lW, lH = imageSize(path)
    
    #size((lW-20), (lH-20))
    #image('/Users/jtd/Dropbox/JTD/SharedJTD/Logo/Assets/JTD_Logo.png', (100, 100))

def caption(x,y):
    fs = FormattedString(
        captionText, 
        font=captionFont,
        fontSize=captionSize,
        fill=0,
        align="center"
    ) 
    textBox(fs, (x,y,w,80))
    
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
textBox(fs, (0, 320, w, 158))

fs = FormattedString(
    'Designed By James Hultquist-Todd\n4 Weights\nDesigned in 2019',
    font=captionFont,
    fontSize=captionSize,
    align="center"
    )
textBox(fs, (0, 140, w, 80))

logo()

#==========================================
#Page 3


newPage(w, h) 
PageName = fontName
header()
#logo()

font(myFontReg, 40)
fill(0)

t = textBox(ucWords, (margin, margin, marginWidth, marginHeight))

captionText = "English"
caption(0,760)




#==========================================
#Page 4

PageName = fontName
kernGuy(38,ucAWords,(h * 2))

PageName = fontName
kernGuy(38,ucBWords,(h * 2))

PageName = fontName
kernGuy(38,ucCWords,(h * 2))

PageName = fontName
kernGuy(38,ucDWords,(h * 2))

PageName = fontName
kernGuy(38,ucEWords,(h * 2))

PageName = fontName
kernGuy(38,ucFWords,(h * 2))

PageName = fontName
kernGuy(38,ucGWords,(h * 2))

PageName = fontName
kernGuy(38,ucHWords,(h * 2))

PageName = fontName
kernGuy(38,ucIWords,(h * 2))

PageName = fontName
kernGuy(38,ucJWords,(h * 2))

PageName = fontName
kernGuy(38,ucKWords,(h * 2))

PageName = fontName
kernGuy(38,ucLWords,(h * 2))

PageName = fontName
kernGuy(38,ucMWords,(h * 2))

PageName = fontName
kernGuy(38,ucNWords,(h * 2))

PageName = fontName
kernGuy(38,ucOWords,(h * 2))

PageName = fontName
kernGuy(38,ucPWords,(h * 2))

PageName = fontName
kernGuy(38,ucQWords,(h * 2))

PageName = fontName
kernGuy(38,ucRWords,(h * 2))

PageName = fontName
kernGuy(38,ucSWords,(h * 2))

PageName = fontName
kernGuy(38,ucTWords,(h * 2))

PageName = fontName
kernGuy(38,ucUWords,(h * 2))

PageName = fontName
kernGuy(38,ucVWords,(h * 2))

PageName = fontName
kernGuy(38,ucWWords,(h * 2))

PageName = fontName
kernGuy(38,ucXWords,(h * 2))

PageName = fontName
kernGuy(38,ucYWords,(h * 2))

PageName = fontName
kernGuy(38,ucZWords,(h * 2))

PageName = fontName
kernGuy(38,lcLSpacing,(h * 2))

PageName = fontName
kernGuy(38,lcSSpacing,(h * 2))

PageName = fontName
kernGuy(38,numberWords,(h * 2))





#==========================================
#Page 3
#while len(udhrEng):
    #newPage(w, h)
    #PageName = fontName
    #header()
    #logo()

    #font(myFontReg, 20)
    #fill(0)

    #t = textBox(udhrEng, (0, 0, w-100, w-80))

    #captionText = "English"
    #caption(0,500)



#==========================================
#Export
path = "/Users/jtd/Your team Dropbox/JTD/Drawbot/TypeProofer/GeneratedProof/JTD_Proof_%s.pdf" % fontName
deletePath = "/Users/jtd/Documents/DeleteStuff/JTD_Proof_%s.pdf" % fontName
saveImage(path)
saveImage(deletePath)

# open the animation
import os
os.system(f"open -a Safari {deletePath}")
