#se crea las dos listas CARTAS Y PREMIUM

cartas =  ['Payne' , 'Hendrix' , 'Stone' , 'Coffey' , 'Whitaker' , 'Pope' ,
        'Bleach' , 'Arc' , 'Fleming' , 'Hardin' , 'Robiar' , 'Mccullough' ,
        'Mooney' , 'Reynolds' , 'Short' , 'Stanton' , 'Deadman' , 
        'Stonehammer' , 'Smith' , 'Patrick' , 'Crane' , 'Cargane' , 'Powers' , 
        'Wade' , 'Joseph' , 'Savage' , 'Houston' , 'Merritt' , 'Nuke' , 
        'Barnett' , 'Acosta' , 'Duke' , 'Sellers' , 'Blake' , 'Schneider' , 
        'Stone' , 'Cannon' , 'Garrison' , 'Randall' , 'Leon' , 'Buck' , 
        'Shannon' , 'Delaney' , 'Mckinney' , 'Dodademocles' , 'Flowers' , 
        'Whitehead' , 'Kirby' , 'Park' , 'Shannon' , 'Vlad' , 'Pepin' , 
        'Mcguire' , 'Murray' , 'Rush' , 'Aramis' , 'Fletcher' , 'Mcfadden' , 
        'Deleon' , 'Luke' , 'Lindsay', 'Payne' , 'Gerbvo' , 'Hubbard' , 
        'Burnett' , 'Bryan' , 'Ratliff' , 'Carlson' , 'Parsons' , 'Deadmeat' , 
        'Crimson' , 'Wilson' , 'Terry' , 'Hancock' , 'Hightower' , 'Burns' , 
        'Austin' , 'Nightwalker' , 'Thetis' , 'Owen' , 'Tate' , 'Simmons' , 
        'Grant' , 'Barber' , 'Talos' , 'Ashes' , 'Alston' , 'Clayton' , 
        'Mcbride' , 'Huffman' , 'Lightbringer' , 'Blankenship' , 'Higgins' , 
        'Saint' , 'Graham' , 'Hodor' , 'Ellison' , 'Roberts' , 'Odom' , 'Mann']

premium = ['AIVLIS', 'LEIRBAG', 'NAILUJ', 'SOLRAC', 'ANAID']

#se define la funcion imprimir

def imprimir(lista):
    print('\nElementos:\n\n',lista[:],'\n')
    print('El tamaño de la lista es:', len(lista), '\n')

#se invoca las funciones con las dos listas ya creadas

imprimir(premium)
imprimir(cartas)

#se empieza a crear la funcion generador, para ello se importa random
#pdt antes importe numpy pero me aconsejaron random, es lo mismo pero sen el np

import random

def generador(lista_a,n):
    listar=[]
    cont=0
    while cont<n:
        num=random.randint(0,len(lista_a)-1)
        if cont== 0:
            cart=lista_a[num]
            listar.append(cart)
            cont=cont+1
        else:
            cart=lista_a[num]
            for evaluar in listar:
                if cart==evaluar:
                    llave=0
                else:
                    llave=1
            if llave==1:
                listar.append(cart)
                cont=cont+1
    return listar

#se almacena el retorno en jugador

jugador=generador(cartas,10)

# se suma se utiliza shuffle y salio

def combinador(a,b):
    listaR=a+b
    random.shuffle(listaR)
    return listaR

# se dan los parametros y se almacena el retorno

juego=combinador(cartas,premium)

#se crean los sobres

sobre_uno=generador(juego,5)

sobre_dos=generador(juego,5)

sobre_tres=generador(juego,5)

# se utiliza combinador para crear el paquete

paquete=combinador(sobre_uno,combinador(sobre_dos,sobre_tres))

# se define loteria 

def loteria(tupaq,premio):
    llave=0
    cont=0
    llave2=0
    llave3=0
    for carta in tupaq:
        for carta2 in tupaq:
            if carta==carta2:
                llave=1
    for cartap in tupaq:
        for cartap2 in premio:
            if cartap==cartap2:
                cont=cont+1
    if cont<2:
        llave2=1
        if (llave==1) and (llave2== 1):
            probabilidad=random.randint(1,10)
            if probabilidad==7:
                while llave3==0:
                    i=random.choice(premio)
                    for ii in tupaq:
                        if i!=ii:
                            tupaq.append(i)
                            llave3=1
                            break
    return tupaq

paquete=(loteria(paquete,premium))

#se guarda las cartas del paquete en el jugador

jugador=jugador+paquete

#10.1

def cant_cartasp(jugador,premium):
    cartasp=[]
    for i in jugador:
        for ii in premium:
            if i==ii:
                cartasp.append(i)
    if cartasp!=[]:
        print('si tiene cartas premium y son:',cartasp)
        print()
    else:
        print('no tuvo cartas premium')
        print()

cant_cartasp(jugador,premium)
