import matplotlib.pyplot as plt

class Funkcja:
    wybor = "0"
    obszarA = 0
    obszarB = 0

    def wypisz(self):
        print("1) x^2+x+c ")
        self.wybor = input("Podaj nr funkcji:")
        if self.wybor == "1":
            self.kwadrat()
        else:
            pass    
    def kwadrat(self):
        self.obszarA = int(input("Podaj granice A: "))
        self.obszarB = int(input("Podaj granice B: "))
        x2 = int(input("Podaj wartosc przy x^2: "))
        x1 = int(input("Podaj wartosc przy x: "))
        c = int(input("Podaj c: "))
        self.rysuj(x2,x1,c)

    def rysuj(self,x2,x1,c):
        x = []
        y = []
        for i in range(self.obszarA,self.obszarB+1):
            x.append(i)
            y.append(x2*pow(i,2)+x1+c)
        plt.plot(x,y)
        plt.show()


fun = Funkcja()
fun.wypisz()        