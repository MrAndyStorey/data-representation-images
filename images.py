#!/usr/bin/env python3
import os
import argparse

import sys
from PIL import Image


from webbrowser import open_new_tab

def scaleImage(passedInput, passedOutput, width=None, height=None, createFilename=False):  
  #Open the image that we'll be working with and get it's existing height and width
  image = Image.open(passedInput)
  w, h = image.size

  # You can specify the width and/or height that you want to scale the image down to
  if width and height:
    max_size = (width, height)
  elif width:
    max_size = (width, h)
  elif height:
    max_size = (w, height)
  else:
    # No width or height specified
    sys.exit("Width or height required!")
  
  #Now resize the image.  Using the Image.ANTIALIAS flag applies a high quality downsampling filter which results in a better image.
  image.thumbnail(max_size, Image.ANTIALIAS)
  
  #If we've been asked to (by the setting of createFilename) create the new filename based on the NEW height and width
  if createFilename:
    createdFilename = str(image.size[0]) + "-" + str(image.size[1]) + ".jpg"
    image.save(os.path.join(os.getcwd(), passedOutput, createdFilename))
  else:
    createdFilename = passedOutput
    image.save(passedOutput)

  # Close the image
  image.close

  return createdFilename


def createDifferentResolutions(passedInput, passedPath):
  # First up, we've created a list of maximum widths that we'd like to create
  widthRanges = (100, 500, 1000, 2000)

  # For each fo those, create a new smaller version of the file using the scaleImage function
  for currentWidth in widthRanges:
    print(scaleImage(passedInput=passedInput,passedOutput=passedPath,width=currentWidth, createFilename=True))

  return os.path.join(os.getcwd(), passedPath)


def createDifferentColourDepths(passedInput, passedPath):
  print("Colour depth files will be created in: " + passedPath)

  return os.path.join(os.getcwd(), passedPath)


def extractMetaData(passedInput):
  print("Metadata inpout file is: " + passedInput)

  return os.path.join(os.getcwd(), passedInput)


def createHTML(passedHtmlPath, passedHtmlFile):
  print("Filename to be created: " + passedHtmlFile)

  with open(os.path.join(passedHtmlPath,passedHtmlFile), 'w+', encoding='utf-8') as outputFile:
    outputFile.write('<html>\n<head>\n</head>\n<body>\n<p>\n')

    outputFile.write('\n</p>\n</body>\n</html>')
    outputFile.close

    return passedHtmlFile


# Allow the user to any options via a CLI argument.
parser = argparse.ArgumentParser(description='')
parser.add_argument("--file", default="poole-park.jpg", type=str, help="Input filename - default = poole-park.jpg.")
parser.add_argument("--path", default="images", type=str, help="Output file path - default = images.")
parser.add_argument("--out", default="index.html", type=str, help="Output file - default = index.html.")

args = parser.parse_args()

if __name__ == '__main__':

  # Create different pixel resolutions of the file.
  createDifferentResolutions(args.file, args.path)

  # Create different colour depth versions of the medium size image  
  createDifferentColourDepths(args.file, args.path)

  # Extract some (interesting) metadata from the original file.
  extractMetaData(args.file)

  # Open the HTML output file and display it to the user.
  #open_new_tab('file://' + os.getcwd() + '/' + args.path + '/' + createHTML(args.path, args.out))

