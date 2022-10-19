# 2 dimensiju saraksta izveides 3. metode

import random

rows, cols = (10, 10)
arr = []
for i  in range(rows):
    col=[]
    for j in range(cols):
        col.append(random.randrange(0,10))
    arr.append(col)
# print(arr)

# izvada kā sakārtotu tabulu bez komatiem un iekavām
"""
for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print()
"""
for i in range(rows):
    #print("")
    for j in range(cols):
        print(arr[i][j], end=" ")
    print()

print()

for i in range(rows):
    print(arr[0][i], end=" ")
print()
print()


