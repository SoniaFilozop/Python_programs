from PIL import Image

im = Image.open("image.png")
pixels = im.load()
x, y = im.size
p = pixels[0, 0]
t, f, le, f1 = y + 1, 0, x + 1, 0
for i in range(x):
    for j in range(y):
        if pixels[i, j] != p:
            if j < t:
                t = j
            if j > f:
                f = j
            if i > f1:
                f1 = i
            if i < le:
                le = i
im2 = im.crop((le, t, f1 + 1, f + 1))
im2.save('res.png')