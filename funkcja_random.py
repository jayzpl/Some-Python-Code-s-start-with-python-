import matplotlib.pyplot as plt
import random

class Funkcja:
    zawartosc = ""
    obszar = 0
    y = []
    x = []
    def wpisz(self):
        #self.zawartosc = input("Wpisz wzor funkcji: ")
        self.obszar = int(input("Wpisz zakres funkcji od zera do: "))
    def wypisz(self):
        print(self.zawartosc)
        print(self.obszar)

    def rysuj(self):
        self.x = range(self.obszar)
        for i in range(self.obszar):
            self.y.append(random.randint(0,9))
        plt.plot(self.x,self.y)
        plt.show()


fun = Funkcja()
fun.wpisz()
fun.rysuj()
