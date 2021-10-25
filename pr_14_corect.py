
a=[]
n=int(input('dati n:'))
if n>=2 and n<=10:
    for x in range (0,n):
        x=[]
        for k in range (0,n):
          k=int(input('dati elementul :'))
          x.append(k)
        a.append(x)
print(a)
d_1=[]
d_2=[]
deasuprad_1=[]
deasuprad_2=[]
subd_1=[]
subd_2=[]
for i in range (len(a)):
    for j in range (len(a[0])):
        if i==j:
            d_1.append(a[i][j])
        if i+j==(len(a)-1):
            d_2.append(a[i][j])
        if i<j:
            deasuprad_1.append(a[i][j])
        if i>j:
            subd_1.append(a[i][j])
        if (i+j)<(len(a)-1):
            deasuprad_2.append(a[i][j])
        if (i+j)>(len(a)-1):
            subd_2.append(a[i][j])
        
print('suma elementelor de pe diagonala pricipala:',sum(d_1))
print('suma elementelor de pe diagonala secundara:',sum(d_2))
print('suma elementelor care se afla deasupra diagonalei principale:',sum(deasuprad_1))
print('suma elementelor care se afla deasupra diagonalei secundare:',sum(deasuprad_2))
print('suma elementelor care se afla sub diagonala principala:',sum(subd_1))
print('suma elementelor care se afla sub diagonala secundara:',sum(subd_2))
    