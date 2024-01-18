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
        print("Lista completa:", self.listaNum)

        pares = [num for num in self.listaNum if num % 2 == 0]
        impares = [num for num in self.listaNum if num % 2 != 0]

        print("Números pares:", pares)
        print("Números impares:", impares)


        repeticiones = {}
        for num in set(self.listaNum):
            cantidad = self.listaNum.count(num)
            if cantidad > 1:
                repeticiones[num] = cantidad

        if repeticiones:
            print("Números que se repiten y cantidad de repeticiones:")
            for num, cantidad in repeticiones.items():
                print(f"{num}: {cantidad} veces")
        else:
            print("Ningún número se repite.")



def main():
    
    cant = int(input("Cuantos numeros desea introducir? : "))
    obj = Pares(cant)
    obj.manipularLista()

if __name__=="__main__":
    main()