# data-representation-images
I've created this to explain to KS3 and KS4 pupils how image format, resolution and colour depth affect the file size of an image.

It takes the following arguments from the CLI.  
* --file  (Input filename path.  Default: poole-park.jpg)
* --path  (Output file path where all files are created.  Default: images)
* --out   (Output file of a HTML summary of the files created.  Default: index.html)

## Packages Used
The following packages are used:
* [Pillow](https://pillow.readthedocs.io/en/stable/index.html) Pillow is a powerful library that you can use for general purpose image processing.
* [NumPy](https://numpy.org/) NumPy is a scientific computing library for Python and it can be used to speed up some pixel-by-pixel operations that Pillow is a little slow for.

To install these packages, you should use Python's package installer, pip3.  On the MacOS CLI you can use these commands:
```
pip3 install Pillow
pip3 install numpy
```
