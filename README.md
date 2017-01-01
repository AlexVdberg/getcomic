# getcomic
Python script for pulling comics from websites

Usage:
 - place the following information on indivitual lines in a file named comic.cfg
   in the desired output directory
    - curpage - the page that the script will start on
    - endpage - last page to get searched
    - imgline - line in the html that includes the comic image
    - nextimg - line in the html that includes reference to the next html page
 - run 'python getcomic.py'
    - add parameter '-d' with a destination directory to specify an alternate
      location
    - add parameter '-c' with a config file to specify alternate webcomic configuration

Notes:
 - Re-running the script will not redownload already downloaded images (unless 
   numbering is different)
 - All images are prepended with a 5 digit (0 padded) number to denote order
