import random 
import os
import time
from colorama import *

cad1 = "    " + time.strftime("%d-%m-%Y %H:%M", time.gmtime()) + """    
    Asignatura:         LÓGICA DE PROGRAMACIÓN
    Institución:        UNIVERSIDAD PONTIFICIA BOLIVARIANA
    Hehcho por:         Daniel Cadena y Diego Vivas
    Fecha:              Mayo 8 de 2020
    codigo:             BLACKJACK - Parte b de los ejercicios """

ponderado = {'A':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10} 
simbolos = ['(C)','(D)','(T)','(P)']
baraja = {}
cjugador = []
ctallador = []
ganadas = 0 
perdidas = 0
x = 0



ponderado = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10} 
simbolos = ['(C)','(D)','(T)','(P)']



def combinar(A,B): 
    R = {}
    for cA in A.keys():
        for i in range(0,len(B)):
            R.setdefault(cA + B[i],A[cA])
    return R



def revolver(A):  
    C = []
    R = {}
    C = [key for key in A]
    random.shuffle(C,random.random)
    for i in range(0,len(C)):
        a = C[i]
        R.setdefault(a,A[a])
    return R



def sumar_cartas(B):
    j = 0
    k = 0
    for i in range(0,len(B)):
        j += baraja.get(B[i])
        if baraja.get(B[i]) == 1:
            k = 10
    if j <= 11:
        j += k
    return j



def repartir(A):
    global ganadas
    global perdidas
    global win
    global loose
    C = []
    C = [key for key in A]
    b = 1
    if len(cjugador) == 0:
        for i in range(0,2):
            cjugador.append(C[i])
            print('\t ' + cjugador[i]," *\n")
    if sumar_cartas(cjugador) == 21:
        ganadas += 1
        print("\t FELICITACIONES, GANASTEE!!, TIENES 21 PUNTOS!!! \n")
        b = 0
    while b == 1:
        print("\t Deseas más cartas? ")
        print()
        b = int(input('\t 1. Si     0. No, me quedo : '))
        if b == 1:
            cjugador.append(C[len(cjugador)])
            print('\t ' + cjugador[len(cjugador)-1]," *\n")
        if sumar_cartas(cjugador) > 21:
            perdidas += 1
            print("\t Lo lamento, perdiste, tienes más  de 21 puntos! \n")
            b = 0
        if sumar_cartas(cjugador) == 21:
            ganadas += 1
            print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, TIENES 21 PUNTOS!!! \n")
            b = 0


print()


def repartir_tallador():
    D = []
    D = [key for key in baraja]
    if win == ganadas and loose == perdidas: 
        if len(ctallador) == 0:
            for i in range(0,2):
                ctallador.append(D[len(cjugador)+i])
                print('\t ' + ctallador[i]," $\n")
            while sumar_cartas(ctallador) <= sumar_cartas(cjugador):
                ctallador.append(D[len(cjugador)+len(ctallador)])
                print('\t ' + ctallador[len(ctallador)-1]," $\n")
                


print()

def mostrar():
    global ganadas
    global perdidas
    suma_jugador = sumar_cartas(cjugador)
    suma_tallador = sumar_cartas(ctallador)
    print("\t Total Jugador: ", suma_jugador, " \n")
    print("\t Total Tallador: ", suma_tallador, " \n")
    if suma_tallador != 0:
        if suma_tallador > 21:
            ganadas += 1
            print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, el Tallador tiene más de 21 puntos!!! \n")
        else:
            if suma_jugador > suma_tallador:
                ganadas += 1
                print("\t FELICITACIONES, GANASTE!!!, tienes más puntos que el Tallador!!! \n")
            else:
                perdidas += 1
                print("\t Lo lamento, perdiste, el tallador tiene mas puntos \n")
    input('\t Pulsa una tecla para continuar...')


print()


def menu_principal():
    os.system('cls')
    print(cad1," \n")
    print('\t 1.  NUEVO JUEGO\n')
    print('\t 2.  MOSTRAR BARAJAS\n')
    print('\t 3.  REVOLVER DE NUEVO\n')
    print('\t 4.  MOSTRAR ESTADÍSTICAS  DEL JUEGO\n')
    print('\n\t 9.  SALIR\n')
    print('\n\t Opción: ',sep='', end=" ")

print()

while True:
    menu_principal()
    win = ganadas
    loose = perdidas
    x = input()
    if x == '1':
        cjugador = []
        ctallador = []
        baraja = combinar(ponderado,simbolos)
        baraja = revolver(baraja)
        repartir(baraja)
        repartir_tallador()
        mostrar()
    elif x == '2':
        baraja = combinar(ponderado,simbolos)
        print("\t Baraja ordenada: ",len(baraja),"\n",baraja,"\n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '3':
        baraja = revolver(baraja)
        print("\t Baraja revuelta: ",len(baraja),"\n",baraja,"\n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '4':
        print("\t ESTADÍSTICAS DEL JUGADOR: ganadas = ",ganadas,"   perdidas = ",perdidas," \n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '9':
        break
    else:
        print("")
        input("\t Opción invalida...pulsa nuevamente ")

