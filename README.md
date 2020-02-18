# Hash Noise
Generates a "random" image based on the sha256 hash of an input text.

## Usage

```
$ ./main.py -h
usage: main.py [-h] [--alpha] [--show] [TEXT]

positional arguments:
  TEXT        input text for hashing

optional arguments:
  -h, --help  show this help message and exit
  --alpha     generates image with alpha channel
  --show      diplays the image
```

## Examples

Output for text: "virtuaCode"
![Input text: "virtuaCode"](examples/821a4b7be24fd450a44d31cad3a1686472daeca8f1e7ce5b3700559e12264ff0.png) 

Output for text: ""
![Input text: ""](examples/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.png)