rindas, kolonas = 5, 3
m = [[None] * kolonas for i in range(rindas)]
m[0][0] = "A"
m[0][1] = "B"
m[0][2] = "C"
m[1][0] = "D"
m[1][1] = "E"
m[1][2] = "F"
m[2][0] = "G"
m[2][1] = "H"
m[2][2] = "I"
m[3][0] = "J"
m[3][1] = "K"
m[3][2] = "L"
m[4][0] = "M"
m[4][1] = "N"
m[4][2] = "O"

#A
#D
#G

for i in range(rindas):
    #print("")
    for j in range(kolonas):
        print(m[i][j], end=" ")
    print()

for i in range(rindas):
    print(m[i][0], end=" ")
print()

for i in range(rindas):
       print(m[i][0], )  


#for i in range(rindas):
#    for j in range(0, kolonas, 2):
#        print(m[i][j], end="")
#   print()

for i in range(rindas):
    for j in range(kolonas):
        if j % 2 == 0:
            print(m[i][j], end="")
    print()



