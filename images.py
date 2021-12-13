#!/usr/bin/env python3
# General purpose libs
import sys
import os

# Used to read the arguments passed using the CLI
import argparse

# Used for Image Scaling
from PIL import Image, ExifTags

# Used for rendering the html output file.  Jinja2 is used under the hood of Flask, and as it does a nice job, we'll use it again here.
import jinja2

# Used to display the web browser window.
from webbrowser import open_new_tab

def reduceColourDepth(passedInput, passedOutput, passedPaletteData, passedMultipler):  
  #Create a reduced colour palette
  palimage = Image.new('P', (16, 16))
  palimage.putpalette(passedPaletteData * passedMultipler)

  #Open the image that we'll be working with
  oldimage = Image.open(passedInput)
  newimage = oldimage.quantize(palette=palimage, dither=True)  #.convert('RGB')
  
  #Save the new file as a PNG - this will give a more realistic difference in the resultant file sizes.
  newimage.save(passedOutput, format="png")
  return passedOutput


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

  tempfilename = os.path.join(os.getcwd(), passedPath, passedInput)

  # This colour palette has only black and white - only one bit per pixel.
  palettedata_1bit = [0,0,0, 255,255,255]
  
  # 2-bit greyscale, a monochrome 4 colour palette with black, white, dark and then light grey - two bits per pixel.
  palettedata_2bit = [0,0,0, 255,255,255, 102,102,102, 176,176,176]
  
  # 3-bit, 8 colour palette that has black, white, the three RGB primary colours (red, green and blue) and the correspondent complementary cyan, magenta and yellow.
  palettedata_3bit = [0,0,0, 255,255,255, 255,0,0, 0,255,0, 0,0,255, 255,255,0, 0,255,255, 255,0,255] 
  
  # 4-bit, 16 monocrhome palette that is here just to show how less minimal colour monochrome palettes work
  palettedata_4bit_mono = [0,0,0, 24,24,24, 40,40,40, 56,56,56, 71,71,71, 86,86,86, 100,100,100, 113,113,113, 126,126,126, 140,140,140, 155,155,155, 171,171,171, 189,189,189, 209,209,209, 231,231,231, 255,255,255]

  # 4-bit, 16 colour palette that has many of the colours taken from an early version of Windows.
  palettedata_4bit = [0,0,0, 0,85,0, 0,170,0, 0,255,0, 0,0,255, 0,85,255, 0,170,255, 0,255,255, 255,0,0, 255,85,0, 255,170,0, 255,255,0, 255,0,255, 255,85,255, 255,170,255, 255,255,255] 
  
  # 5-bit, 32 colour palette that I have implemented from the following URL: https://lospec.com/palette-list/cheerful-32
  palettedata_5bit = [14,17,18, 43,45,51, 76,80,89, 138,147,153, 194,201,204, 255,249,242, 102,204,255, 46,138,230, 31,72,153, 23,32,77, 15,77,56, 15,153,49, 22,217,22, 140,255,25, 255,255,77, 255,213,0, 242,121,0, 230,35,0, 179,0,30, 128,13,32, 89,9,36, 51,10,51, 102,10,71, 191,0,111, 255,51,153, 255,128,149, 255,187,153, 230,138,92, 179,83,36, 107,43,21, 64,21,13, 43,15,15]

  # 6-bit, 64 colour palette that I have implemented from the following URL: https://lospec.com/palette-list/endesga-64
  palettedata_6bit = [255,0,64, 19,19,19, 27,27,27, 39,39,39, 61,61,61, 93,93,93, 133,133,133, 180,180,180, 255,255,255, 199,207,221, 146,161,185, 101,115,146, 66,76,110, 42,47,78, 26,25,50, 14,7,27, 28,18,28, 57,31,33, 93,44,40, 138,72,54, 191,111,74, 230,155,105, 246,203,159, 249,230,207, 237,172,80, 224,115,56, 198,68,36, 142,37,29, 255,81,0, 237,118,20, 255,161,20, 255,201,37, 255,235,87, 210,252,126, 154,230,95, 91,197,79, 51,152,75, 30,111,80, 19,76,76, 12,46,68, 0,56,109, 0,105,170, 0,150,220, 0,203,249, 12,243,255, 148,253,255, 253,210,237, 243,137,245, 218,63,253, 121,9,250, 49,3,217, 12,2,147, 3,25,63, 59,20,67, 98,36,97, 147,56,142, 202,82,200, 200,80,134, 246,129,135, 245,85,93, 234,50,60, 196,36,47, 137,30,42, 87,28,39]

  filename_1bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-1bit.png"), palettedata_1bit, 128)
  filename_2bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-2bit.png"), palettedata_2bit, 64)
  filename_3bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-3bit.png"), palettedata_3bit, 32)
  filename_4bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-4bit.png"), palettedata_4bit, 16)
  filename_4bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-4bit-mono.png"), palettedata_4bit_mono, 16)
  filename_5bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-5bit.png"), palettedata_5bit, 8)
  filename_6bit=reduceColourDepth(tempfilename, tempfilename.replace(".jpg", "-6bit.png"), palettedata_6bit, 4)

  return os.path.join(os.getcwd(), passedPath)


def extractMetaData(passedInput):
  img = Image.open(os.path.join(os.getcwd(), passedInput))
  img_exif = img.getexif()
  
  exifData = {}
  for tag, value in img_exif.items():
      decodedTag = ExifTags.TAGS.get(tag, tag)
      exifData[decodedTag] = value
  
  return exifData


def createHTML(passedHtmlPath, passedHtmlFile, passedHtmlTemplate, passedFilename, passedMetaData):

  with open(os.path.join(passedHtmlPath,passedHtmlFile), 'w+', encoding='utf-8') as outputFile:
    title = "Data Representation"
    subs = jinja2.Environment( 
                  loader=jinja2.FileSystemLoader('./')      
                  ).get_template(passedHtmlTemplate).render(title=title,filename=passedFilename,metadata=passedMetaData) 

    outputFile.write(subs)

    return passedHtmlFile


# Allow the user to any options via a CLI argument.
parser = argparse.ArgumentParser(description='')
parser.add_argument("--file", default="poole-park.jpg", type=str, help="Input filename - default = poole-park.jpg.")
parser.add_argument("--path", default="images", type=str, help="Output file path - default = images.")
parser.add_argument("--out", default="index.html", type=str, help="Output file - default = index.html.")
parser.add_argument("--template", default="template.html", type=str, help="Output file template file - default = template.html.")

args = parser.parse_args()

if __name__ == '__main__':

  # Create different pixel resolutions of the file.
  createDifferentResolutions(args.file, args.path)

  # Create different colour depth versions of the medium size image  
  createDifferentColourDepths("500-375.jpg", args.path)

  # Extract some (interesting) metadata from the original file.
  createdMetaData = extractMetaData(args.file)
  
  # Open the HTML output file and display it to the user.
  open_new_tab('file://' + os.getcwd() + '/' + args.path + '/' + createHTML(args.path, args.out, args.template, args.file, createdMetaData))

