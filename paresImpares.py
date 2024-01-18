class Pares:
    cantNumeros = 0
    num = 0
    listaNum = []

    def __init__(self, a):
        self.cantNumeros = a

    def manipularLista(self):

        for lista in range(1, self.cantNumeros + 1):
            self.num = int(input("Agrega un numero: "))
            self.listaNum.append(self.num)

        self.listaNum.sort()
        print(self.listaNum)



def main():
    
    cant = int(input("Cuantos numeros desea introducir? : "))
    obj = Pares(cant)
    obj.manipularLista()

if __name__=="__main__":
    main()