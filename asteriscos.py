class Asteriscos:

    cantAsteriscos = 0

    def __init__(self, a):
        self.cantAsteriscos = a
    
    def generarPiramide(self):
        i = 1
        for piramide in range(1,self.cantAsteriscos+1):
            print("*" * i)
            i += 1

def main():
    
    num = int(input("Dame un numero: "))
    obj = Asteriscos(num)
    obj.generarPiramide()

if __name__=="__main__":
    main()