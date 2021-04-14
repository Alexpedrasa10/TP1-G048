import random as r

player1 = str(input("Nombre del participante nº 1: "))
player2 = str(input("Nombre del participante nº 2: "))
participantes = [player1, player2]
puntosPlayer1 = 0
puntosPlayer2 = 0
winnerR1 = None

#Ronda nº1
for x in participantes:

    print('=====================================')
    print('Turno de: ', x)
    intentos = 3
    puntos = 0
    puntajes = []
    i = 0

    # Tiran dados
    while i < intentos:
        
        dado = r.randint(1, 6)
        print('Intento nº',(i + 1), ': ', dado)

        if i == 2:
            if puntajes[0] == dado:

                puntajes.pop(1)
                puntajes.append(dado)
                dado2do = r.randint(1, 6)
                print("El primer dado coincidió con el ultimo, tienes otro intento.")
                print('Intento nº',(i + 2), ': ', dado2do)
                puntajes.append(dado2do)

                if dado2do == dado:
                    puntos+=6
                else:
                    puntos+=3

                break;

            elif puntajes[1] == dado:

                puntajes.pop(0)
                puntajes.append(dado)
                dado2do = r.randint(1, 6)
                print("El segundo dado coincidió con el ultimo, tienes otro intento.")
                print('Intento nº',(i + 2), ': ', dado2do)                
                puntajes.append(dado2do)

                if dado2do == dado:
                    puntos+=6
                else:
                    puntos+=3

                break;

            elif puntajes[0] == puntajes[1]:

                dado = r.randint(1, 6)
                print("El primer intento coindició con el segundo, tienes otro intento.")
                print('Intento nº',(i + 2), ': ', dado)
                puntajes.append(dado)

                if dado == puntajes[0]:
                    puntos+=6
                else:
                    puntos+=3
                break;
        
        puntajes.append(dado)
        i+=1
    
    if puntos != 0:
        print("Usted tiene ", puntos, ' puntos!!')
    else:
        print('No has conseguido ningún punto en esta ronda')

    if x == player1:
        puntosPlayer1 = puntos
    else:
        puntosPlayer2 = puntos


if puntosPlayer1 > puntosPlayer2:
    winnerR1 = player1
elif puntosPlayer2 > puntosPlayer1:
    winnerR1 = player2

print('Terminó la primera ronda!')

if winnerR1 != None:
    print('El ganador de la primera ronda es: ', winnerR1)
else:
    print('No hubo ganador. Empate.')
