# getcomic.py
# 
# Usage
# curPage - the page that the script will start on
# endPage - last page to get searched
# imgLine - line in the html that includes the comic image
# nextImg - line in the html that includes reference to the next html page

import os
import re
import argparse

def pullImages(outDir, curPage, endPage, imgLine, nextImg):
    imgNum = 0
    origFiles = os.listdir(outDir)
    
    while curPage != endPage:
        imgNum = imgNum + 1
        print('Current page:' + curPage)
    
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
            print('reached the end')

def main():
    #Default output directory
    outDir = os.getcwd()

    #Variables specific to the website
    curPage = 'http://www.supernormalstep.com/archives/8'
    endPage = 'http://www.supernormalstep.com/archives/trouble'
    imgLine = 31 - 1
    nextImg = 31 - 1

    #Arguments and Options parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Specifies a output directory")
    args = parser.parse_args()
    
    #Dealing with the arguments passed in
    if args.directory:
        outDir = args.directory
    
    print('Output Directory: ' + outDir)
    print()

    pullImages(outDir, curPage, endPage, imgLine, nextImg)
    os.system('rm page.html')

#Entry point of the program
if __name__ == '__main__':
    main()
