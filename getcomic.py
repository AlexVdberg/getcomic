# getcomic.py
# 
# Usage
# Specify the values for the following parameters on separate lines in a
# comic.cfg file on indivitual lines
#   curPage - the page that the script will start on
#   endPage - last page to get searched
#   imgLine - line in the html that includes the comic image
#   nextImg - line in the html that includes reference to the next html page

import os
import re
import argparse

def pullImages(outDir, curPage, endPage, imgLine, nextImg):
    imgNum = 0
    origFiles = os.listdir(outDir)
    
    while curPage != endPage:
        imgNum = imgNum + 1
        print('Current page: ' + curPage)
    
        #Get the raw html of the comic page
        pageGet = 'wget "' + curPage + '" -O page.html'
        os.system(pageGet)
    
        #Search the page for comic image
        f = open('page.html', 'r')
        line = f.readlines()
        searchObj = re.search( r'http[^"]*(jpg|png|gif)', line[imgLine])
        print(searchObj.group())
        rawName = re.search( r'[^"/]*(jpg|png|gif)', line[imgLine])
    
        #Prepend the image with the number to keep them in order
        savedImgName = str(imgNum).zfill(5) + '-' + rawName.group()
        #Check if the img was already saved
        if savedImgName not in origFiles:
            imgGet = 'wget "' + searchObj.group() + '" -O "' + outDir + '/' + savedImgName + '"'
            os.system(imgGet)
    
        #Get the next comic url from the raw html
        searchObj = re.search( r'<a\b[^>]*next\b[^>]*>', line[nextImg])
        if searchObj:
            nextObj = re.search( r'http\b[^"]*', searchObj.group())
            print(nextObj.group())
            curPage = nextObj.group()
        else:
            print('No next comic url found')

def main():
    #Arguments and Options parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Specifies a output directory")
    parser.add_argument("-c", "--config", help="Specifies the configuration file")
    args = parser.parse_args()
    
    #Dealing with the arguments passed in
    if args.directory:
        outDir = args.directory
    else:
        outDir = os.getcwd()

    if args.config:
        cfgFile = args.config
    else:
        cfgFile = outDir + '/comic.cfg'
    
    print('Output Directory: ' + outDir)
    print

    #Variables specific to the website
    cfgFile = open(outDir + '/comic.cfg', 'r')
    cfgLines = cfgFile.readlines()
    curPage = cfgLines[0].replace('\n', '')
    endPage = cfgLines[1].replace('\n', '')
    imgLine = int(cfgLines[2]) - 1
    nextImg = int(cfgLines[3]) - 1

    pullImages(outDir, curPage, endPage, imgLine, nextImg)
    os.system('rm page.html')

#Entry point of the program
if __name__ == '__main__':
    main()
