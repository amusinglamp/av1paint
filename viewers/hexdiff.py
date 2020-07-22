from glob import glob
from termcolor import colored

print(colored('unknown', color="red"), colored('size', 'green'), colored('image data', 'blue'))

hexdata = {}

for file in glob("*.avif"):
    with open(file, 'rb') as f:
        hexdata[f"{file}"] = f.read().hex()


posdiff = dict.fromkeys(hexdata.keys())
# assume there's a bunch of identical crap at the start of each file.
# pick the smallest file, and start comparing it char by char against the other files,
# recording the position of first difference.


for i, char in enumerate(min(hexdata.values())):
    for k in [k for k, v in posdiff.items() if not v]:
        if char != hexdata[k][i]:
            posdiff[k] = i

# the first 126 bytes (252 hex chars) are always the same, there's 1 byte of difference
# then another chunk of similarity, until we hit the canvas size.
# let's get that size

truncdata = {k: v[254:] for (k, v) in hexdata.items()}
truncdiff = dict.fromkeys(truncdata.keys())

for i, char in enumerate(min(truncdata.values())):
    for k in [k for k, v in truncdiff.items() if not v]:
        if char != truncdata[k][i]:
            truncdiff[k] = i

## Next is 140 hex further along - if you're a 512 square, or 142 if you're a smaller square. let's assume it's 70 bytes and has 2 bytes of data,
## let's add a larger image to the dataset so we can compare a reasonable maximum (16384x16384)


truncdata = {k: v[406:] for (k, v) in hexdata.items()}
truncdiff = dict.fromkeys(truncdata.keys())

for i, char in enumerate(min(truncdata.values())):
    for k in [k for k, v in truncdiff.items() if not v]:
        if char != truncdata[k][i]:
            truncdiff[k] = i

# Helpful comprehension to list file contents in order of size after a particular hex digit position, filtered by filename, plus size in bytes
[print(v[283<<1:], k, len(v[290<<1:])>>1, int("0x"+v[289<<1:290<<1], 16)) for (k,v) in sorted(hexdata.items(), key=lambda x: x[1]) if  "grey" in k]



posdiff2 = dict.fromkeys(hexdata.keys())
# lets just focus on a 32x32 solid grey square and see how they differ


for i, char in enumerate(hexdata['32x32 grey.avif']):
    for k in [k for k, v in posdiff2.items() if not v]:
        if char != hexdata[k][i]:
            posdiff2[k] = i