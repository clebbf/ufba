#Código escrito por Cleber B. Figueiredo em 23/11/2022
#Matrícula: 220115472
#FISD37 - UFBA - 2022

#Libraries utilizadas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter

#Dados coletados em sala de aula
tempoSegundos = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1350, 1380, 1440, 1500, 1560, 1620, 1680, 1740, 1800, 1860, 1920, 1980, 2040, 2100, 2160, 2220, 2280, 2340]
temperaturaCelsius = [28.4,31.4,34.2,37,39.7,42.6,45,47.6,49.9,52.5,54.9,57.1,59.5,61.6,63.8,66,68,70.2,72.4,74.5,76.8,78,80,80.5,80.4,80.2,79.9,79.7,79.3,74.8,74.6,74.3,73.9,73.5,73.2,72.9,72.5,72.3,72,71.8]

#Código referente à criação do gráfico
fig, ax = plt.subplots()
plt.scatter(tempoSegundos, temperaturaCelsius, color='blue', s=15.0)
plt.title('Gráfico de Temperatura (°C) X Tempo (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.xticks([0, 500, 1000, 1350, 1680, 2000, 2340])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

#Indica a cor diferente dos pontos
for i in range(0, len(tempoSegundos)):
    if tempoSegundos[i] == 1350 and temperaturaCelsius[i] == 80:
        plt.scatter(tempoSegundos[i], temperaturaCelsius[i], color = 'red', s=30)
    if tempoSegundos[i] == 1680 and temperaturaCelsius[i] == 79.3:
        plt.scatter(tempoSegundos[i], temperaturaCelsius[i], color = 'orange', s=30)
        
ax.set_xlim(0, 2340)
ax.set_ylim(0, 90)

#Legenda
vermelho = mpatches.Patch(color='red', label='Momento em que T = 80°C')
amarelo = mpatches.Patch(color='orange', label='Momento em que a barra foi\ninserida e T = 79.3°C')
azul = mpatches.Patch(color='blue', label='Demais pontos')
ax.legend(handles=[vermelho, amarelo, azul])

#Grid do gráfico
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax.grid(axis="x", color="black", alpha=.3, linewidth=1, linestyle=":")
ax.grid(axis="y", color="black", alpha=.3, linewidth=1, linestyle=":")


plt.show()
plt.savefig("figure.png")
