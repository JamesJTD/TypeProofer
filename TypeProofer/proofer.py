from drawBot import *
import sys
import datetime
import os
from fontTools.ttLib import TTFont
from vanilla.vanillaWindows import *
from vanilla import *
from vanilla.dialogs import *

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

#==========================================
#Foundry

foundryName = 'JTD, LLC'

#==========================================
#Fonts

#font size for the proofs
proofFontSize = 36

#caption font & font size
captionFont = 'ArrayMonoV1001-Regular'    
captionSize = 9

#==========================================
#Save Location

savePath = "/Users/jtd/Documents/DeleteStuff/"


#######NOTHING BELOW HERE NEEDS TO BE CHANGED##########


#==========================================
#Misc Variables

h = height()

now = datetime.datetime.now()
year = now.strftime("%Y")
w,h = width(), height()

#==========================================
#Misc Functions
             
#Kerning/Spacing Function with uses individual lists for each letter
def kernGuy(fSize,letterString,pageLength):
    newPage(width(), pageLength)
    header()
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
        f = textBox(fs, (margin, (0-(margin / 2)), marginWidth, txtHeight))

    restore()

'''Kerning/Spacing Function Version 3 which uses tuples instead of individual lists

Creates a page where the length of the page is based on the length of text'''

def kernGuy3(fSize):
    for a in ucWords:
        primaryLetter,text = a
        t = ''
        if allCaps == 1:

            t += f"{text}".upper()

        else:

            t += f"{text}"


        class proofPage:

            def __init__(self, h):
                self.h = h
                self.pageLength = h

            def addText(self):

                

                '''This needs work to adjust get the th variable to show up properly
                
                textSize(t)[1] only shows the height for one line, unless they are 
                explicitly declared in the MiscWords.py file as multi-line. Therefore, 
                we are using the width of the line and dividing it to get our usable 
                line height.'''

                for fName in fontFamily:

                    
                    font(fName, fSize)
                    lineHeight(fSize * 1.1)
                    tw, th = textSize(t)

                    pp.p = (tw / 2.4) + (fSize* 2)

                    #print(tw)

                    pp.p += margin * len(fontFamily)

                    if pp.p < self.h:
                        break

                    else:
                        pp.pageLength = pp.p

                    return(pp.pageLength)

            def pageText(self):

                translate(0, pp.pageLengthMargin)
                save()
                for fName in fontFamily:

                    pp.getName(fName)

                    caption(f"{pp.weight}", 0,50)

                    th = pp.pageLengthMargin / len(fontFamily)
                    fs = FormattedString(
                        t,
                        font=fName,
                        fontSize=fSize,
                        lineHeight=fSize * 1.1,
                        fill=0,
                        align="left"
                    )
                    translate(0, -th)

                    list
                    f = textBox(fs, (margin, margin, marginWidth, th))

                    

                restore()


            def getName(self,fName):

                tt = TTFont(fName)

                # nameID: https://docs.microsoft.com/en-us/typography/opentype/spec/name#name-ids
                # platformID (1 or 3)
                # platEncID (0 or 1)
                # langID (0 or 0x409)

                pp.weight = tt["name"].getName(17, 3, 1, 0x409)

                #Attempt to remove "None" from generated PDF. Not working yet
                if pp.weight == "":

                    pp.weightName = tt["name"].getName(2, 3, 1, 0x409)

                else:

                    pp.weightName = pp.weight

                print(pp.weightName)
                return(pp.weightName)



            def makePage(self):

                pp.addText()

                print(pp.pageLength)


                newPage(width(), pp.pageLength)
                header()
                caption(f"{primaryLetter}", 0,50)

                pp.pageLengthMargin = pp.pageLength - (margin * 4)

                pp.pageText()


   


        pp = proofPage(h)

        pp.makePage()

#==========================================
#Universal Elements For Each Page

#location of the fonts which you want to proof
fontFamily = getFile('Choose you fonts',None,None,None,True)

#make dialog box to get all caps
allCaps = askYesNo("All Caps?")

print(allCaps)

'''
Use this if you are hardcoding the fontPath variable to a directory

fontFamily = []


#Get the font from the specified folder and prep it
for files in glob.glob(f'{fontPath}*.otf'):
    fontFamily.append(files)
    fontFamily.sort()
    print(fontFamily)
'''

def name():
    for fName in fontFamily:
        tt = TTFont(fName)
        fn = tt["name"].getName(16, 3, 1, 0x409)

        fn = f"{fn}"
        return(fn)

fontName = name()


print(fontName)



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


titleFont = fontFamily[0]

fs = FormattedString(
        fontName, 
        font=titleFont,
        fontSize=1,
        fill=0,
        align="center"
    )

textWidth, textHeight = textSize(fs)   
myFontSize = marginWidth / textWidth
fs = FormattedString(
        fontName,
        font=titleFont,
        fontSize=myFontSize,
        lineHeight=myFontSize, 
        fill=0,
        align="center")
translate(0, -myFontSize)
textBox(fs, (0, 340, width(), 158))


#==========================================
#Proofing Pages

PageName = fontName
kernGuy3(proofFontSize)

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



#==========================================
#Export
path = f"{savePath}Proof_{fontName}.pdf"
saveImage(path)

# open the in Safari
os.system(f"open -a Safari {path}")