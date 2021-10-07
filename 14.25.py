A=[]
n=int(input('introdu numarul de linii:'))
if ((n>=2)and(n<=10)):
    print("introdu elementele matricei:")
    for i in range(0,n):
        i=[]
        for j in range(0,n):
            j=int(input())
            i.append(j)
        A.append(i)
    print(A)
    dp=[]
    ds=[]
    ddp=[]
    sdp=[]
    dds=[]
    sds=[]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                dp.append(A[i][j])
            if j+i==(len(A)-1):
                ds.append(A[i][j])
            if i>j:
                ddp.append(A[i][j])
            if i<j:
                sdp.append(A[i][j])
            if i+j<(len(A)-1):
                dds.append(A[i][j])
            if i+j>(len(A)-1):
                sds.append(A[i][j]) 
    print('a)suma elementelor pe diagonala principala:',sum(dp))
    print('b)suma elementelor pe diagonala secundara:',sum(ds))
    print('c)suma elementelor mai sus de diagonala principala:',sum(ddp))
    print('d)suma elementelor mai jos de diagonala principala:',sum(sdp))
    print('e)suma elementelor mai sus de diagonala secundara:',sum(dds))
    print('f)suma elementelor mai jos de diagonala secundara:',sum(sds))