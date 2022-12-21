#izvada tabulu ar cipariem(lieto atstarpes), izvada pirmo rindu un diagonāles
import random

rows, cols = (10, 10)
arr = []
sum = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(random.randrange(0,20))
    arr.append(col)

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print() #lidz seienei izvada ciparu tabulu ar atstarpem

print()
for i in range(rows):
    print(arr[0][i], end="\t")

print()

for i in range(rows):
    for j in range(cols):
        if i == j:
            print(arr[i][j], end="\t")

print()
for i in range(rows):
    for j in range(cols):
        if i+j==9:
            print(arr[i][j], end="\t")
            i+=1
            j+=1
        