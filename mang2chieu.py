a=[]
b=[]
c=[]
d=[]
m=2
n=2

def CreateMatrix(a,m,n,c):
    for i in range(m):
        a.append([])
        for j in range(n):
            x = int(input("%c[%d] [%d]= "%(c,i+1,j+1)))
            a[i].append(x)

def ViewMatrix(a,m,n):
    for i in range(m):
        for j in range(n):
            print("%d" %a[i][j],end = " ")
        print()

def SumMatrix(a,b,m,n):
    c=[]
    for i in range(m):
        c.append([])
        for j in range(n):
            x = a[i][j]+b[i][j]
            c[i].append(x)
    return c


def MulMatrix(a,b,m,n):
    d =[]
    for i in range(m):
        d.append([])
        for j in range(n):
            x=0
            for k in range(m):
                x = x +a[i][k]*b[k][j]
            d[i].append(x)
    return d

def main():
    print("tao ma tran A: ",end="\n")
    CreateMatrix(a,m,n,"A")
    print("xem ma tran A: ",end="\n")
    ViewMatrix(a,m,n)
    print("tao ma tran B: ",end="\n")
    CreateMatrix(b,m,n,"B")
    print("xem ma tran B: ",end="\n")
    ViewMatrix(b,m,n)
    c=SumMatrix(a,b,m,n)
    print("xem ma tran C: ",end="\n")
    ViewMatrix(c,m,n)
    d=MulMatrix(a,b,m,n)
    print("xem ma tran D: ",end="\n")
    ViewMatrix(d,m,n)

if __name__ == "__main__":
    main()