#Izveidosim 2dimensiju srakstu n aizpildīsim to ar vērtībām no klases piemēra
"""
m = [0][0] = "A"
m = [0][1] = "B"
m = [0][2] = "C"
m = [1][0] = "A"
m = [1][1] = "B"
m = [1][2] = "C"
m = [2][0] = "A"
m = [2][1] = "B"
m = [2][2] = "C"
m = [3][0] = "A"
m = [3][1] = "B"
m = [3][2] = "C"
m = [4][0] = "A"
m = [4][1] = "B"
m = [4][2] = "C"

print(m[2][2])


r, k = (4, 2) #rindu un kolonnu skaits(saraksta lielums)
m = [[""]*k]*r #piešķir saraksta elementiem simboliskas vērtības, kas patiesībā ir nekas "", jo pretējā gadījumā Python nezina cik liels būs saraksts
m = [0][0] = "A"
m = [0][1] = "B"
m = [0][2] = "C"
m = [1][0] = "D"
m = [1][1] = "E"
m = [1][2] = "F"
m = [2][0] = "G"
m = [2][1] = "H"
m = [2][2] = "I"
m = [3][0] = "J"
m = [3][1] = "K"
m = [3][2] = "L"
m = [4][0] = "M"
m = [4][1] = "N"
m = [4][2] = "O"

m[0][0]="r"
m
print(m[0][0])
"""
#st.darbs. 

#1.variants.divdimensiju saraksts
#m = [None] * rindas
#for i in range(rindas):
 #   m[i] = [None] * kolonas
#print(m)
rindas, kolonas = 5, 3
#2.variants
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
#for i in range(rindas):
#    print(m[i])
#print(m[2][2])
#A B C
#D E F
#.....
for i in range(rindas):
    #print("")
    for j in range(kolonas):
        print(m[i][j], end=" ")
    print("")