from PIL import Image

im = Image.open("image.png")
pixels = im.load()
x, y = im.size

a = 0
p = 0
v = 0
d = 0
for i in range(x):
    for j in range(y):
        d += 1
        r, g, b = pixels[i, j]
        a += r
        p += g
        v += b
r, g, b = (a // d, p // d, v // d)
