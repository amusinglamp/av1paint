from PIL import Image
from pathlib import Path
from os import system
# Create 256 32x32 greyscale pngs
for i in range(0,255,1):
    img = Image.new('RGB', (32,32), (i, i, i))
    img.save(Path.cwd().parent / 'color' / 'grey' / f"32x32 grey {i}.png", "PNG")

# create 216 websafe colour pngs
for r in (0x00, 0x33, 0x66, 0x99, 0xcc,0xff):
    for g in (0x00, 0x33, 0x66, 0x99, 0xcc, 0xff):
        for b in (0x00, 0x33, 0x66, 0x99, 0xcc, 0xff):
            img = Image.new('RGB', (32,32), (r, g, b))
            img.save(Path.cwd().parent / 'color' / 'websafe' / f"32x32 #{r:02x}{g:02x}{b:02x}.png", "PNG")

# convert pngs to avif if no existing image exists
# get full path and filenames but with no suffix for everything in color subfolders
pngs=[p.with_suffix("") for p in (Path.cwd().parent / 'color').rglob('*.png')]
avif=[a.with_suffix("") for a in (Path.cwd().parent / 'color').rglob('*.avif')]

toconvert = [f.with_suffix(".png") for f in (set(pngs) - set(avif))]

for file in toconvert:
    command = f"C:\\Users\\Chris\\Documents\\av1_exploration\\avif-win-x64.exe -e \"{file}\" -o \"{file.with_suffix('.avif')}\""
    system(command)
    print(command, file)


