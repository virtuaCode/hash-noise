# Hash Noise
Generates a "random" image based on the sha256 hash of an input text.

## Usage

```
$ ./main.py -h
usage: main.py [-h] [-a] [-s] [--width WIDTH] [--height HEIGHT] [TEXT]

positional arguments:
  TEXT             input text for hashing

optional arguments:
  -h, --help       show this help message and exit
  -a, --alpha      generates image with alpha channel
  -s, --show       diplays the image
  --width WIDTH    image width (default = 128, use multiples of 8 for best
                   results)
  --height HEIGHT  image height (default = 128, use multiples of 8 for best
                   results)
```

## Examples

![Input text: "virtuaCode"](examples/821a4b7be24fd450a44d31cad3a1686472daeca8f1e7ce5b3700559e12264ff0.png) 

Output for text: "virtuaCode"


![Input text: ""](examples/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.png) 

Output for text: ""
