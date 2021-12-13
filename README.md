# data-representation-images
I've created this to explain to KS3 and KS4 pupils how image format, resolution and colour depth affect the file size of an image.

It takes the following arguments from the CLI.  
* --file  (Input filename path.  Default: poole-park.jpg)
* --path  (Output file path where all files are created.  Default: images)
* --out   (Output file of a HTML summary of the files created.  Default: index.html)
* --template (Output file template file.  Default: template.html)

## Packages Used
The following packages are used:
* [Pillow](https://pypi.org/project/Pillow/) Pillow is a powerful library that you can use for general purpose image processing.
* [jinja2](https://pypi.org/project/Jinja2/) Jinja is a templating language for use with Python - commonly used with Flask.
* [exif](https://pypi.org/project/exif/) Python library used to read and modify image EXIF metadata.

To install these packages, you should use Python's package installer, pip3.  On the MacOS CLI you can use these commands:
```
pip3 install Pillow
pip3 install Jinja2
pip3 install exif
```
