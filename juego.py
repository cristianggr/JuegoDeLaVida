# JUEGO DE LA VIDA DE CONWAY BASADO EN TUTORIAL DE DotCSV

import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantalla.
width, height = 1000, 1000
# Creación de la pantalla.
screen = pygame.display.set_mode((width, height))

# Colordel fondo = Casi negro.
bg = 25, 25, 25
# Pintamos el fondo con el color elegido.
screen.fill(bg)

nxC, nyC = 100, 100

dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0;
gameState = np.zeros((nxC, nyC))


# Estado incial provocado: Autómata palo
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

# Control de la ejecución del juego
pauseExect = False

#Bucle de ejecución.
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        # Detercamos si se presiona el ratón.
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0,nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1) % nxC, (y - 1) % nxC] + \
                            gameState[(x)     % nxC, (y - 1) % nxC] + \
                            gameState[(x + 1) % nxC, (y - 1) % nxC] + \
                            gameState[(x - 1) % nxC, (y)     % nxC] + \
                            gameState[(x + 1) % nxC, (y)     % nxC] + \
                            gameState[(x - 1) % nxC, (y + 1) % nxC] + \
                            gameState[(x)     % nxC, (y + 1) % nxC] + \
                            gameState[(x + 1) % nxC, (y + 1) % nxC]

                # Regla 1: Una célula muerta con exactemente 3 vecinas vivas, "resucita".
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

                # Regla 2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere".
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0



            # Creamos el plígono de cada celda a dibujar
            poly = [((x)   * dimCW, y     * dimCH),
                    ((x+1) * dimCW, y     * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Se dibuja la celda para cad apar de x e y.
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Se actualiza el estado del juego.
    gameState = np.copy(newGameState)

    # Se actualiza la pantalla.
    pygame.display.flip()

