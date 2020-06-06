#zaimportowac biblioteke bokeh
#pip install bokeh
import math
from bokeh.plotting import figure, show

a=float(input('podaj a='))
b=float(input('podaj b='))
c=float(input('podaj c='))
xp=float(input('podaj granice dolna '))
xk=float(input('podaj granice dolna '))
krok=float(input('podaj krok '))

delta=float(b**2-(4*a*c))       #pobieranie danych i dzialanie delty

wykres=figure(title='Wykres funkcji y='+str(a)+'x^2+'+str(b)+'x+'+str(c),
              plot_width=800, plot_height=600, toolbar_location="above")

if(delta<0):
    print ('Brak rozwiazani rzeczywistych')


if(delta==0):
    x0=float(-b/(2*a))
    print ('Jedno rozwiazanie xo=' + str(x0))
    wykres.circle([x0],[0],size=6, color="red", alpha=0.5, legend="Miejsce zerowe")

if(delta>0):
    x1=float(((-b-math.sqrt(delta))/(2*a)))
    x2=float(((-b+math.sqrt(delta))/(2*a)))
    print('Dwa rozwiazania x1='+str(x1)+' oraz x2=' +str(x2))
    wykres.circle([x1], [0], size=6, color="red", alpha=0.5, legend="Miejsce zerowe")
    wykres.circle([x2], [0], size=6, color="red", alpha=0.5,)
x=xp
if(delta>=0):
    while(x<=xk):
        y=float((a*(x**2))+(b*x)+c)
        wykres.circle([x],[y], size=2, color='black', alpha=0.5)
        x+=krok

show(wykres)