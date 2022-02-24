import numpy as np
import random
import time

print("Bienvenido!! \nEste es el mitico juego de Hundir la flota. Estas preparado para jugar?")
nombre = str(input("Introduce tu nombre: "))

class Tablero:

    def __init__(self,nombre):
        self.nombre = nombre

    def tablero_maquina(self): 
        tablero_maquina1 = np.full((11,11),' ') #La W indica que hay agua
        return tablero_maquina1

    def tablero_jugador (self):
        tablero_jugador1 = np.full((11,11),' ')
        return tablero_jugador1

    def invisible (self):
        tablero_jugador1 = np.full((11,11),' ')
        return tablero_jugador1   


maquina_tablero = Tablero("Maquina") #Tablero maquina que se ve
jugador_tablero = Tablero("Jugador") #Tablero maquina invisible
maquina_tablero_invisible = Tablero("MaquinaInvisible") #Tablero jugador que se ve
nacho_invisible = Tablero("JugadorInvisible") #Tablero jugador invisible


tablero_maquina = maquina_tablero.tablero_maquina()
tablero_maquina_inv = maquina_tablero_invisible.invisible()

tablero_jugador = jugador_tablero.tablero_jugador()
tablero_jugador_inv = nacho_invisible.invisible()


def barcos_en_coordenadas(): #Aniadimos tanto los barcos de la maquina como los mios

    barcos =[4,3,3,2,2,2,1,1,1,1]  
    # POSICIONAMIENTO BARCOS DEL JUGADOR
    for longitud in barcos:

        direccion = random.choice(["NS", "EO"])
        longitud
        barco=True

        while barco:
            random_fila_barco = random.randint(0,9)
            random_columna_barco = random.randint(0,9)


            if direccion == "NS" and random_fila_barco + longitud -1 <= 9 and len(tablero_jugador[np.where(tablero_jugador[ random_fila_barco : random_fila_barco + longitud, random_columna_barco] == "O")]) == 0:
                tablero_jugador[random_fila_barco, random_columna_barco] = "O"
                tablero_jugador[random_fila_barco : random_fila_barco + longitud, random_columna_barco] = "O"
                barco=False
            elif direccion == "EO" and random_columna_barco + longitud -1 <=9 and len(tablero_jugador[np.where(tablero_jugador[random_fila_barco, random_columna_barco:random_columna_barco+longitud] =="O")]) == 0:
                tablero_jugador[random_fila_barco, random_columna_barco] = "O"
                tablero_jugador[random_fila_barco, random_columna_barco:random_columna_barco+longitud] ="O"
                barco=False
    print("Nombre del jugador:",nombre,"\n", tablero_jugador)

    
    #POSICIONAMIENTO BARCOS DE LA MAQUINA
    for longitud in barcos:

        direccion = random.choice(["NS", "EO"])
    
        barco = True  

        while barco:
            random_fila_barco = random.randint(0,9)
            random_columna_barco = random.randint(0,9)


            if direccion == "NS" and random_fila_barco + longitud -1 <= 9 and len(tablero_maquina[np.where(tablero_maquina[ random_fila_barco : random_fila_barco + longitud, random_columna_barco] == "O")]) == 0:
                tablero_maquina[random_fila_barco, random_columna_barco] = "O"
                tablero_maquina[random_fila_barco : random_fila_barco + longitud, random_columna_barco] = "O"
                barco=False
            elif direccion == "EO" and random_columna_barco + longitud -1 <=9 and len(tablero_maquina[np.where(tablero_maquina[random_fila_barco, random_columna_barco:random_columna_barco+longitud] =="O")]) == 0:
                tablero_maquina[random_fila_barco, random_columna_barco] = "O"
                tablero_maquina[random_fila_barco, random_columna_barco:random_columna_barco+longitud] ="O"
                barco=False

    print("Tablero de la maquina","\n", tablero_maquina_inv)

barcos_en_coordenadas()

#Aqui creamos una lista de coordenadas para la maquina
lista_coordenadas_maquina = [(0, 0), (0, 1), (0, 2), (0, 3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
                        (1, 0), (1, 1), (1, 2), (1, 3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
                        (2, 0), (2, 1), (2, 2), (2, 3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
                        (3, 0), (3, 1), (3, 2), (3, 3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
                        (4, 0), (4, 1), (4, 2), (4, 3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
                        (5, 0), (5, 1), (5, 2), (5, 3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
                        (6, 0), (6, 1), (6, 2), (6, 3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
                        (7, 0), (7, 1), (7, 2), (7, 3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
                        (8, 0), (8, 1), (8, 2), (8, 3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
                        (9, 0), (9, 1), (9, 2), (9, 3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9),]  #SON LAS QUE USA LA MAQUINA PARA DISPARAR AL JUGADOR


#DISPARO JUGADOR A MAQUINA
def disparo_jugador(): #Funcion para pedir coordenadas
    filas = int(input("Introduce la fila: "))
    columnas = int(input("Introduce la columna: "))
    
    coordenada_tablero = (filas-1,columnas-1) #Coordenada que va de 0 al 9 para que entre en el tablero
    coordenada_tablero_print = (filas,columnas) #Coordenadas que salen en la ejecucion del 1 al 10

    time.sleep(0.3)
    if filas <= 0 or filas > 10 or columnas <= 0 or columnas > 10: #No elijas un numero menor que 0 o mayor que 10
        print("Del 1 al 10, el mapa es de 10x10. Te dejo repetir anda")
    else:
        if tablero_maquina[coordenada_tablero] == ' ':
            tablero_maquina[coordenada_tablero] = '-'
            tablero_maquina_inv[coordenada_tablero] = '-'
            print("No hay barco en -> ", coordenada_tablero_print ," \nTurno de la maquina.") #Es agua asi que cambia el turno
            print(tablero_maquina_inv)
            return "Agua"
        elif tablero_maquina[coordenada_tablero] == 'O':
            tablero_maquina[coordenada_tablero] = '*' #Tocado, sigue tu turno
            tablero_maquina_inv[coordenada_tablero] = "*"
            print("TOCADO en la posicion -> ", coordenada_tablero_print)
            print(tablero_maquina_inv)
            return "Tocado"
        elif tablero_maquina[coordenada_tablero] == '-' or tablero_maquina[coordenada_tablero] == '*': #Si no es ni agua ni barcos es que la coordenada esta repetida
            print ("Coordenada repetida")




#DISPARO MAQUINA A JUGADOR
def disparo_maquina():
    disparo_machine = random.choice(lista_coordenadas_maquina)
    lista_coordenadas_maquina.remove(disparo_machine)#Disparo aleatorio de la maquina
    time.sleep(0.3)
    if tablero_jugador[disparo_machine] == ' ':
        tablero_jugador[disparo_machine] = '-' #Es agua asi que cambia el turno
        print("La maquina ha fallado. \nNo hay barco en :" ,disparo_machine, "ES TU TURNO")
        print(tablero_jugador)
        return "Agua"
            
    elif tablero_jugador[disparo_machine] == 'O':
        tablero_jugador[disparo_machine] = '*' #Tocado, sigue el turno de la maquina
        print("La maquina ha acertado. \nTocado en :", disparo_machine)
        print(tablero_jugador)
        return "Tocado"


cambio_turno = True 
final = False

while final == False:

    while len(tablero_jugador[np.where(tablero_jugador == "O")]) and len(tablero_maquina[np.where(tablero_maquina == "O")]) > 0:#Saber si hay barcos en el mapa o no
    #Para saber si se ha ganado y sino se cambia de turno
        while cambio_turno == True:
            if len(tablero_maquina[np.where(tablero_maquina=="O")]) == 0:
                print("HAS GANADO! GRANDE CAMARADA!")
                break

            elif disparo_jugador() == "Tocado":
                continue

            else:
                cambio_turno = False
                continue
            
        time.sleep(0.3)

        while cambio_turno == False:
            if len(tablero_jugador[np.where(tablero_jugador == "O")]) == 0:
                print("HAS PERDIDO! LA PROXIMA VEZ SERA")
                break       

            elif disparo_maquina() == "Tocado":
                continue

            else:
                cambio_turno = True #Si fallas pasa a ser True
                continue 
        time.sleep(0.3)