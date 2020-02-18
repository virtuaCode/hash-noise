#!/usr/bin/env python3
import hashlib
import numpy as np
from PIL import Image
import argparse
import sys

def main(args):
    size = 8
    text = args.text or ""
    val = text.encode()
    mode = "RGBA" if args.alpha else "RGB"
    image = Image.new(mode,(size,size))

    hash = hashlib.sha256()
    hash.update(text.encode())
    input_hash = hash.digest()

    for y in range(size):
        hash = hashlib.sha256()
        hash.update(val)
        val = hash.digest()
                 
        for x,rgba in enumerate(np.split(np.frombuffer(val, dtype=np.byte),8)):
            r, g, b, a = rgba.tobytes()
            if args.alpha:
                image.putpixel((x,y), (r,g,b,a))
            else:
                image.putpixel((x,y), (r,g,b))

    image = image.resize((args.width,args.height))

    if args.show:
        image.show(title="Hash Noise \"{}\"".format(input_hash.hex()))

    if sys.stdout.isatty():
        image.save(input_hash.hex() + ".png")
    else:
        image.save(sys.stdout.buffer, format="PNG")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", metavar='TEXT', type=str, nargs="?",
                    help='input text for hashing')
    parser.add_argument("-a","--alpha", action="store_true", default=False, help="generates image with alpha channel")
    parser.add_argument("-s","--show", action="store_true", default=False, help="diplays the image")
    parser.add_argument("--width", default=128, type=int, help="image width (default = 128, use multiples of 8 for best results)")
    parser.add_argument("--height", default=128, type=int, help="image height (default = 128, use multiples of 8 for best results)")

    args = parser.parse_args();

    main(args)