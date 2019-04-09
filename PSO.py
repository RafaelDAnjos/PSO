import random
import math

# Determinando número de particulas
from typing import List

numparticula = 20
particulas = []
pbest = []
gbest = []
velocidade = []
bordaInferior = -100
bordaSuperior = 100
melhorapt = 0
fi1 = 0
fi2 = 0
for i in range(numparticula):
    x1 = random.randint(bordaInferior, bordaSuperior)
    x2 = random.randint(bordaInferior, bordaSuperior)
    particulas.append([x1, x2])
    velocidade.append([3, 4])


for i in range(100):
    for j in range(len(particulas)):
        apt = 0.5 + (math.sin(((particulas[j][0] ** 2) + (particulas[j][1] ** 2)) ** 0.5) - 0.5) / ((1 + 0.001 * ((particulas[j][0] ** 2) + (particulas[j][1]))) ** 2)
        if (i == 0):
            particulas[j].append(apt)
            pbest.append([particulas[j][0], particulas[j][1]])
            if i == 0 and j == 0:
                melhorapt = apt
                gbest.append(particulas[0][0])
                gbest.append(particulas[0][1])
            else:
                if (particulas[j][2] < melhorapt):
                    melhorapt = particulas[j][2]
                    gbest[0] = particulas[j][0]
                    gbest[1] = particulas[j][1]

        else:
            if (apt < particulas[j][2]):
                particulas[j][2] = apt
                pbest[j][0] = particulas[j][0]
                pbest[j][1] = particulas[j][1]

            if (particulas[j][2] < melhorapt):
                melhorapt = particulas[j][2]
                gbest[0] = particulas[j][0]
                gbest[1] = particulas[j][1]

        fi1 = random.uniform(0,1)
        fi2 = random.uniform(0,1)


        velocidade[j][0] = velocidade[j][0] + fi1*(pbest[j][0] - particulas[j][0]) + fi2*(gbest[0]-particulas[j][0])
        velocidade[j][1] = velocidade[j][1] + fi1*(pbest[j][1] - particulas[j][1]) + fi2*(gbest[1]-particulas[j][1])

        particulas[j][0] = particulas[j][0] + velocidade[j][0]

        particulas[j][1] = particulas[j][1] + velocidade[j][1]

        if particulas[j][0]> 100:
            particulas[j][0] = 100
            velocidade[j][0] = 0

        if particulas[j][0]<-100:
            particulas[j][0] = 100
            velocidade[j][0] = 0

        if particulas[j][1]> 100:
            particulas[j][1] = 100
            velocidade[j][1] = 0

        if particulas[j][1]< -100:
            particulas[j][1] = 100
            velocidade[j][1] = 0

    print(gbest)