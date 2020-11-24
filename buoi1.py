# def tong(a,b):
#     return a+b
# def main():
#     a = int(input("nhap a: "))
#     b= int(input("nhap b: "))
#     c = tong(a,b)
#     print("c = %d"%c,end ="\n")
# if __name__ == "__main__":
#     main()



def InputData():
    a= float(input("a = "))
    b= float(input("b = "))
    return a,b
def SolveEqual(a,b):
    if a==0:
        if b==0:
            print("phuong trinh vo so nghiem...")
        else:
            print("phuong trinh vo nghiem")
    else:
        x=-b/a
        print("nghiem x= %.3lf"%x,end = "\n")
def main():
    a,b = InputData()
    SolveEqual(a,b)
if __name__ == "__main__":
    main()


