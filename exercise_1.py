import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa')
indice = np.arange(len(musicas))
acessos = [1068254,866216,849895,763652,758198]

plt.bar(indice, acessos, color=["cyan","red","gray","yellow",(0.8,0.5,1.0,1.0)], edgecolor='blue')
plt.xticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Ranking do Spotify 31.dez.2019')
plt.show()