from random import randint
from random import choice

n_simulaciones = int(input("Ingrese el número de simulaciones: "))

victorias_count_s1 = 0
victorias_count_s2 = 0


for i in range (n_simulaciones):
    puertas = [1,2,3]
    #Seleccion random de la puerta con premio
    puerta_ganadora = choice(puertas)

    #Puerta elegida por el jugador
    puerta_jugador = choice(puertas)

    #El presentador abre una puerta sin premio
    puertas.remove(puerta_ganadora)
    if puerta_jugador != puerta_ganadora:
        puertas.remove(puerta_jugador)
    
    puerta_presentador = choice (puertas)

    #El jugador mantiene la elección de su puerta
    if puerta_jugador == puerta_ganadora:
        victorias_count_s1 +=1


