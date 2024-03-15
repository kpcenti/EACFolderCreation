#Ask for CD Info and Make Folder for CD, then launch EAC

import os
#ask for metadata
artist = input("Enter artist name: ")
album = input("Enter album name: ")
year = input("Enter year of release: ")
catno = input("Enter catalogue number: ")
foldername = artist + " - " + album + " (" + year + ") {" + catno + "} [FLAC]"
print(foldername)
#makefolder
os.mkdir(foldername)
print("Folder has been created", foldername)

print("Starting EAC")

import sys
sys.exit()