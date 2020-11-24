import math
def Input():
    a = float(input("a= "))
    b= float(input("b= "))
    c= float(input("c= "))
    return a,b,c
def PT(a,b,c):
    if a==0 and b==0 and c==0:
        print("phuong trinh vo so nghiem")
    elif a==0 and b==0 and c!=0:
        print("phuong trinh vo nghiem")
    elif a==0 and b!=0:
        x=-c/b
        print("phuong trinh bac 1 x= ",str(x))
    else:
        delta = math.pow(b,2)-4*a*c
        if delta>0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            print("nghiem phan biet:\n")
            print("x1= %.3lf"%x1,"x2= %.3lf"%x2)
        elif delta ==0:
            x0=-b/(2*a)
            print("nghiem kep") 
            print("x0= %.2f"%x0)
        else:
            print("vo nghiem thuc")

def main():
    a,b,c=Input()
    PT(a,b,c)

if __name__ == "__main__":
    main()    




