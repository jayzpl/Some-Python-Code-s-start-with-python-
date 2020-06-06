a = [[1,3,8],[2,2,4,7],[0,1,3]]

def delete(a,i):
    for licznik, k in enumerate(a):
        if licznik==i:
            k.pop(0)
    return a

def multi_merge(a):
    b = []
    c = []
    index = []
    while True:
        dl = len(a)
        b = []
        index = []
        for licznik, i in enumerate(a):
            b.append(i[0])
            index.append(licznik)
        dlugosc = len(b)
        for x in range(dlugosc-1): #tu sie zastanawiam czy moze byc -1
            for z in range(dlugosc-1):
                if b[z] > b[z+1]:
                    b[z] , b[z+1] = b[z+1], b[z] 
                    index[z] , index[z+1] = index[z+1], index[z]
        if b[0]!=None:
            c.append(b[0])
            b.pop(0)
            a = delete(a,index[0])
            for tak, h in enumerate(a):
                if len(h)==0:
                    a.pop(tak)
        else:
            break
        dl = len(a)
        if dl<=0:
            break
    return c

c = multi_merge(a)
print(c)