from PIL import Image
from pathlib import Path
from os import system
import random
# Create 256 32x32 greyscale pngs

def RGBtoYCbCr(R=0, G=0, B=0):
    Kry = 0.2126
    Kby = 0.0722
    Kgy = 1-(Kry+Kby)

    Kru = -Kry
    Kgu = - Kgy
    Kbu = 1-Kby
    Krv = 1-Kry
    Kgv = -Kgy
    Kbv = -Kby

    Y = Kry*R + Kgy * G + Kby * B
    Cb = 128- Kru*R - Kgu* G + Kbu * B
    Cr = 128+Krv*R - Kgv* G - Kbv * B
    return(f"{int(Y):02x}{int(Cb):02x}{int(Cr):02x}")



for i in range(0,255,1):
    img = Image.new('RGB', (32,32), (i, i, i))
    img.save(Path.cwd().parent / 'color' / 'grey' / f"32x32 grey {i}.png", "PNG")

# create 216 websafe colour pngs
for r in (0x00, 0x33, 0x66, 0x99, 0xcc,0xff):
    for g in (0x00, 0x33, 0x66, 0x99, 0xcc, 0xff):
        for b in (0x00, 0x33, 0x66, 0x99, 0xcc, 0xff):
            img = Image.new('RGB', (32,32), (r, g, b))
            img.save(Path.cwd().parent / 'color' / 'websafe' / f"32x32 #{r:02x}{g:02x}{b:02x}.png", "PNG")

# create various sizes of cyan pngs
for s in (1,2,4,6,8,12,16,24,32,48,64,96,128,196,256,384,512,768,1024,1566,2048,3072,4096):
    img = Image.new('RGB', (s,s), (0,255,255))
    img.save(Path.cwd().parent / 'size' / 'cyan squares' / f"{s}x{s} cyan.png", "PNG")

# create random colours in the 1-8 px square range
#
# for s in (1,2,4,6,8):
#     gr = random.randint(0,255)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     #r,g,b = gr, gr, gr
#     YCC = RGBtoYCbCr(r,g,b)
#     img = Image.new('RGB', (s,s), (r,g,b))
#     imagename = Path.cwd().parent / 'random' / '1x1 to 8x8 solid colours' / f"{s}x{s} #{r:02x}{g:02x}{b:02x} YCC {YCC}.png"
#     print("creating:" +str(imagename))
#     img.save(imagename, "PNG")

# convert pngs to avif if no existing image exists
# get full path and filenames but with no suffix for everything in color subfolders
for folder in ['color','size','random']:

    pngs=[p.with_suffix("") for p in (Path.cwd().parent / folder).rglob('*.png')]
    avif=[a.with_suffix("") for a in (Path.cwd().parent / folder).rglob('*.avif')]

    toconvert = [f.with_suffix(".png") for f in (set(pngs) - set(avif))]

    for file in toconvert:
        command = f"C:\\Users\\Chris\\Documents\\av1_exploration\\avif-win-x64.exe -e \"{file}\" -o \"{file.with_suffix('.avif')}\""
        system(command)
        print(command, file)



