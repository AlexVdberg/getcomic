# getcomic
Python script for pulling comics from websites

Usage:
 - Copy getcomic.py to the desired location of the webcomic images
 - change the following parameters in getcomic.py
    - curpage - the page that the script will start on
    - endpage - last page to get searched
    - imgline - line in the html that includes the comic image
    - nextimg - line in the html that includes reference to the next html page
 - run 'python getcomic.py'

Notes:
 - Re-running the script will not redownload already downloaded images (unless 
   numbering if different)
 - All images are prepended with a 5 digit (0 padded) number to denote order
