A=[[0,6,88,1,7],
   [274,4,19,13,5],
   [11,18,77,35,10],
   [12,20,22,21,8],
   [14,95,46,36,2]]
print(A)
l1=A[0]
l2=A[1]
l3=A[2]
l4=A[3]
l5=A[4]
c1=[]
c2=[]
c3=[]
c4=[]
c5=[]
for i in A:
    c1.append(i[0])
    c2.append(i[1])
    c3.append(i[2])
    c4.append(i[3])
    c5.append(i[4])
print('suma elementelor din linia 1:',sum(l1))
print('suma elementelor din linia 2:',sum(l2))
print('suma elementelor din linia 3:',sum(l3))
print('suma elementelor din linia 4:',sum(l4))
print('suma elementelor din linia 5:',sum(l5))
print('suma elementelor din coloana 1:',sum(c1))
print('suma elementelor din coloana 2:',sum(c2))
print('suma elementelor din coloana 3:',sum(c3))
print('suma elementelor din coloana 4:',sum(c4))
print('suma elementelor din coloana 5:',sum(c5))
dp=[]
ds=[]
for i in range(len(A)):
    dp.append(A[i][i])
    for j in range(len(A[0])):
        if j+i==4:
            ds.append(A[i][j])
print('diagonala principala:',dp)
print('diagonala secundara:',ds)