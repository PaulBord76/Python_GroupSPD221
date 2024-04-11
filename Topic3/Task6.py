s = "book_cover.jpg cover.png Book_cover.jpg illustration.jpg ILLUSTRATION.JPG my_cover.png photo.gif award.jpg Award.jpg award.JPG"

files = []
files1 = []
files2 = []

files = s.lower()

print(files)

files1 = list(files.split(" "))

print(files1)

for a in files1:
    if a.endswith(".jpg") == True:
        if a not in files2:
            files2 += a.split()

files2.sort()

print(files2)