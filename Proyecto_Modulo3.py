import random
import matplotlib.pyplot as plot

lista = []

def maquina_galton():
    """
    Función que imita el comportamiento de la maquina galto.
    """


    for i in range(3000):
    
        x = 6
        for i in range(12): #Suponiendo la maquina de dalto con 12 obstaculos
            a = (random.randint(0,1)) #aleatoriedad con valor de 0 a 1 es decir con valor binario
            if a == 1:
                x = x+1
            else: 
                x = x-1
        # print(x)
        lista.append(x)

def impresion_histograma(lista):
    """"
    Función que imprime el histrograma
    """
    intervalos = range(min(lista),max(lista))#Cálculo de los extremos
    plot.hist(x = lista, bins = intervalos, color = 'red')
    plot.title("Muestra")
    plot.xlabel("Intervalo")
    plot.ylabel("Conteo")
    plot.show()

maquina_galton()
impresion_histograma(lista)