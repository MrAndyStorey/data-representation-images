#!/usr/bin/env python3
import argparse

# Allow the user to pass the output CSV file via a CLI argument.
parser = argparse.ArgumentParser(description='')
parser.add_argument("--file", default="poole-park.jpg", type=str, help="Input filename - default = poole-park.jpg.")
parser.add_argument("--path", default="images", type=str, help="Output file path - default = /images/.")
parser.add_argument("--out", default="index.html", type=str, help="Output file - default = index.html.")

args = parser.parse_args()

if __name__ == '__main__':
  print(args.file)
  print(args.path)
  print(args.out)
  
