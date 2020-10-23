from random import randint
import sys
import numpy as np
import math

def serieTemp(num):    
    result = math.sin(math.radians(num) + math.pow(math.sin(math.radians(num)),2))
    return result

def gerador (numElementos):
    x = []
    y = []
    
    for i in range(numElementos):
        entrada = []
        saida = []
        
        inteiroAleatorio = randint(0, 500)

        for j in range((inteiroAleatorio - 1), (inteiroAleatorio - 11), -1):
            valor = serieTemp(j)
            entrada.append(valor)
            
        for j in range((inteiroAleatorio + 1), (inteiroAleatorio + 4), 1):
            valor = serieTemp(j)
            saida.append(valor)
        
        x.append(entrada)
        y.append(saida)
        
    np.savetxt('data_x.txt', x, delimiter=',')
    np.savetxt('data_y.txt', y, delimiter=',')
    
gerador(5000)