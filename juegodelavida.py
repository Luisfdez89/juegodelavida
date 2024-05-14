import copy, random, sys, time

# Variables globales
ANCHO = 0   # Ancho de la cuadrícula
ALTO = 0    # Alto de la cuadrícula
VIVO = ''   # Carácter para la celda viva
MUERTO = '' # Carácter para la celda muerta

def inicializar_parametros():
    global ANCHO, ALTO, VIVO, MUERTO
    ANCHO = int(input("Introduce el ancho de la cuadrícula: "))
    ALTO = int(input("Introduce el alto de la cuadrícula: "))
    VIVO = input("Introduce el carácter para la célula viva: ")
    MUERTO = input("Introduce el carácter para la célula muerta: ")

def inicializar_celulas():
    siguientesCelulas = {}
    for x in range(ANCHO):
        for y in range(ALTO):
            if random.randint(0, 1) == 0:
                siguientesCelulas[(x, y)] = VIVO
            else:
                siguientesCelulas[(x, y)] = MUERTO
    return siguientesCelulas

def imprimir_generacion(celulas):
    for y in range(ALTO):
        for x in range(ANCHO):
            print(celulas[(x, y)], end='')
        print()

def calcular_vecinas(x, y, celulas):
    izquierda  = (x - 1) % ANCHO
    derecha = (x + 1) % ANCHO
    arriba = (y - 1) % ALTO
    abajo = (y + 1) % ALTO

    numVecinasVivas = 0
    if celulas[(izquierda, arriba)] == VIVO:
        numVecinasVivas += 1
    if celulas[(x, arriba)] == VIVO:
        numVecinasVivas += 1
    if celulas[(derecha, arriba)] == VIVO:
        numVecinasVivas += 1
    if celulas[(izquierda, y)] == VIVO:
        numVecinasVivas += 1
    if celulas[(derecha, y)] == VIVO:
        numVecinasVivas += 1
    if celulas[(izquierda, abajo)] == VIVO:
        numVecinasVivas += 1
    if celulas[(x, abajo)] == VIVO:
        numVecinasVivas += 1
    if celulas[(derecha, abajo)] == VIVO:
        numVecinasVivas += 1

    return numVecinasVivas

def calcular_siguiente_generacion(celulas):
    siguientesCelulas = {}
    for x in range(ANCHO):
        for y in range(ALTO):
            numVecinasVivas = calcular_vecinas(x, y, celulas)

            if celulas[(x, y)] == VIVO and (numVecinasVivas == 2 or numVecinasVivas == 3):
                siguientesCelulas[(x, y)] = VIVO
            elif celulas[(x, y)] == MUERTO and numVecinasVivas == 3:
                siguientesCelulas[(x, y)] = VIVO
            else:
                siguientesCelulas[(x, y)] = MUERTO

    return siguientesCelulas

def main():
    inicializar_parametros()
    siguientesCelulas = inicializar_celulas()

    while True:
        print('\n' * 50)  # Separación entre generaciones
        imprimir_generacion(siguientesCelulas)
        print('Pulsa Ctrl-C para parar.')

        siguientesCelulas = calcular_siguiente_generacion(siguientesCelulas)

        try:
            time.sleep(1)  # Añadimos un segundo de pausa para evitar parpadeos
        except KeyboardInterrupt:
            print("Juego de la vida de Conway")
            print("https://es.wikipedia.org/wiki/Juego_de_la_vida")
            sys.exit()  # Cuando se pulsa CTRL+C termina el programa

if __name__ == "__main__":
    main()
