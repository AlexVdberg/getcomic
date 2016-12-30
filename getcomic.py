# getcomic.py
# 
# Modification History
# 27dec2016,aav Added reg expressions
# 28dec2016,aav fixed .jpg reg expr to allow spaces for stupid websites that use spaces
# 29dec2016,aav prepend img names and allow redownloading of sites without duplicates
# 29dec2016,aav Added suport for gif files
#
# Usage
# curpage - the page that the script will start on
# endpage - last page to get searched
# imgline - line in the html that includes the comic image
# nextimg - line in the html that includes reference to the next html page

import os
import re

curpage = 'http://www.supernormalstep.com/archives/8'
endpage = 'http://www.supernormalstep.com/archives/trouble'
imgline = 31 - 1
nextimg = 31 - 1

imgnum = 0
origfiles = os.listdir(os.getcwd())

while curpage != endpage:
    imgnum = imgnum + 1
    print('Current page:' + curpage)

    #Get the raw html of the comic page
    pageget = 'wget "' + curpage + '" -O page.html'
    os.system(pageget)

    #Search the page for comic image
    f = open('page.html', 'r')
    line = f.readlines()
    searchobj = re.search( r'http[^"]*(jpg|png|gif)', line[imgline])
    print(searchobj.group())
    rawname = re.search( r'[^"/]*(jpg|png|gif)', line[imgline])

    #Prepend the image with the number to keep them in order
    savedimgname = str(imgnum).zfill(5) + '-' + rawname.group()
    #Check if the img was already saved
    if savedimgname not in origfiles:
        imgget = 'wget "' + searchobj.group() + '" -O "' + savedimgname + '"'
        os.system(imgget)

    #Get the next comic url from the raw html
    searchobj = re.search( r'<a\b[^>]*next\b[^>]*>', line[nextimg])
    if searchobj:
        nextobj = re.search( r'http\b[^"]*', searchobj.group())
        print(nextobj.group())
        curpage = nextobj.group()
    else:
        print('reached the end')

