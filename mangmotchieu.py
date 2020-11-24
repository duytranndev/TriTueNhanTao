import array


n =0
A=[]

def CreateArr(A,n):
    for i in range(n):
        A.append(int(input("nhap so thu %d: "%(i+1))))
def ViewArr(A,n):
    for j in range(n):
        print(A[j],end = "")
    print("\n")
def ViewDownTo(A,n):
    for i in range(0,n):
        print(A[n-i-1],end = "")
    print("\n")
def SumOfItems(A,n):
    s=0
    for i in range (n):
        s +=int(A[i])
    return s
def DelIteam(A,n,k):
    for i in range(k,n-1):
        A[i]=A[i+1]
    return n-1

def InsertItem(A,n,k,x):
    for i in range(k,n):
        j=n-1-i+k
        A.append(A[j-1])
    A.insert(k,x)
    return n+1

def ReverseArr(A,n):
    i=0
    j=n-1
    while i<j:
        A[i],A[j]=A[j],A[i]
        i+=1
        j-=1
def SortArr(A,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if A[j]<A[i]:
                A[i],A[j]=A[j],A[i]

def main():
    n= int(input("Nhap n: "))
    CreateArr(A,n)
    ViewArr(A,n)
    n=InsertItem(A,n,2,9)
    ViewArr(A,n)
    ReverseArr(A,n)
    ViewArr(A,n)
    SortArr(A,n)
    ViewArr(A,n)

if __name__ == "__main__":
    main()

