import pygame
import numpy as np
import time

pygame.init()

# Height and Width of the screen
width, height = 760, 760
# Create the screen
screen = pygame.display.set_mode((height, width))
# Backgroud color = nearly black, nearly dark
bg = 25, 25, 25
# Assign the colour to the background
screen.fill(bg)

# Number of cells on X-axis and Y-axis
nxC, nyC = 60, 60

# Dimensions of the cells
dimCW = width / nxC
dimCH = height / nyC


# State of cells. If alive = 1; If dead = 0
gameState = np.zeros((nxC, nyC))

pauseExect = False

# Loop
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # EVENTS
    ev = pygame.event.get()

    for event in ev:
        # Detects if a key is pressed
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        # Detects if mouse is pressed
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                # Calculate the number of near neighbors
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x)     % nxC, (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, (y)     % nyC] + \
                          gameState[(x + 1) % nxC, (y)     % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[(x)     % nxC, (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]

                # Rule #1: A dead cell with exactly 3 living neighbors revives
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Rule #2 A living cell with less than 2 or more than 3 living neighbors dies
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Create the polygon of each cell to be drawn
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Draw the cell for each x and y pair
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Update the status of the game
    gameState = np.copy(newGameState)

    # Refresh the screen
    pygame.display.flip()







