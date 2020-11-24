
def Init(path):
    f = open(path)
    while True:
        x = f.read()
        print(x)
        if not x:
            break
    f.close()

def main():
    Init("data.txt")

if __name__ == "__main__":
    main()