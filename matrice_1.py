B=[[4,5,6,7,8],
   [7,6,3,9,8],
   [4,9,7,8,5],
   [6,2,0,4,2],
   [9,1,1,4,2]]
print(B)
print('suma elementelor de pe B[0]=',sum(B[0]))
print('suma elementelor de pe B[1]=',sum(B[1]))
print('suma elementelor de pe B[2]=',sum(B[2]))
print('suma elementelor de pe B[3]=',sum(B[3]))
print('suma elementelor de pe B[4]=',sum(B[4]))
c_1=[]
c_2=[]
c_3=[]
c_4=[]
c_5=[]
for i in B:
    c_1.append(i[0])
print('suma elementelor de pe coloana 1=',sum(c_1))
for i in B:
    c_2.append(i[1])
print('suma elementelor de pe coloana 2=',sum(c_2))
for i in B:
    c_3.append(i[2])
print('suma elementelor de pe coloana 3=',sum(c_3))
for i in B:
    c_4.append(i[3])
print('suma elementelor de pe coloana 4=',sum(c_4))
for i in B:
    c_5.append(i[4])
print('suma elementelor de pe coloana 5=',sum(c_5))
d_1=[]
d_2=[]
for i in range (len(B)):
    for j in range (len(B[0])):
        if i==j:
            d_1.append(B[i][j])
        if i+j==4:
            d_2.append(B[i][j])
print('diagonala pricipala:',d_1)
print('diagonala secundara:',d_2)
