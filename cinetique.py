import numpy as np
import matplotlib.pyplot as plt


# concentration en masse et temps (en jours) sous formes de listes
Cm=[3.65,2.34,1.43,0.86,0.51,0.28,0.16,0.08,0.03,0.00]
t=[0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

# Tapez l´instruction qui permet de connaitre le nombre de valeurs des tableaux:

# Tapez l´instruction sous forme de boucle qui permet d'afficher toutes les valeurs de la liste t':

# Tapez l´instruction qui ajoute la valeur '10' à la fin de la liste t
# Tapez l´instruction qui efface cette valeur

# avancement: créez la liste des avamcements au cours du temps en utilisant la formule de l´exercice:


# Affichage du graphique:
plt.plot(t,Cm, "b--",label="x(t)")
plt.title("avancement")
plt.legend()
plt.show()


