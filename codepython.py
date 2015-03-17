# TP Loto
#-*-coding:Latin-1 -*
from random import *

# Cette fonction renvoie un tableau rempli de 0 et de 1
# un 0 correspond à un numéro non tiré, un 1 à un numéro tiré
def numeros_tires():
	tab = [0]*49
	nbTirages = 0
	while nbTirages < 6 :
		resultat = randint(1,49)
		if (tab[resultat - 1]==0):
			tab[resultat - 1] = 1     # Le 0 de la case dont l'indice correspond au numéro tiré est changé en 1
			nbTirages = nbTirages + 1
	return tab

# Cette fonction renvoie le tableau donnant les numéros sortis lors du tirage du loto
def resultats():
	tirages = numeros_tires()
	tablo = [0,0,0,0,0,0]
	num = 0
	for i in range(49):
		if tirages[i] == 1:
			tablo[num] = i+1
			num = num+1
	return tablo



loto = resultats()
grille = [0]*6
resultat = [0]*6
m = 1-49
o=0
numero = 0



print("Donnez moi vos n°")
print("Votre n° 1")
for j in range(6):
        n = int(input(""))
        for k in range(6):
                while (n>49) or (n<1) or (n==grille[k]):
                        if (n>49) or (n<1):
                                print("Numéro non valide (il faut un n° entre 1-49)")
                        if (n==grille[k]):
                                 print("Numéro déjà sélectionner")
                        n = int(input(""))
        grille[j] = n
        if (j+2<7):
                print("Votre n° ",j+2)
print("Votre grille est ",grille)
print("La grille sortie au loto est ",loto)

for j in range(6):
        for k in range (6):
                if grille[k] == loto[j]:
                        numero = numero + 1
                        resultat[m] = grille[k]
                        m = m + 1
if (numero<=1):
       print("Vous avez ", numero," numero juste")
elif (numero>1):
        print("Vous avez ", numero," numeros justes")                      


if(numero==6):
        print("Bravo vous avez gagnez au loto, vous aviez une chance sur 13 983 816, jouez maintenant au vrai loto 8DD !!")
elif(numero==0):
        print("Pas de chance aucun numéro, jouer plutôt au morpion :p")
elif(numero==4) or (numero==5):
        print("Presque, mais il en faudra plus pour gagner le loto :D")
else:
        print("Pas mal, mais il en faudra bien plus pour gagner au loto :)")

del resultat[numero:]
if (numero==1):
        print("Voici le numéro juste ",resultat)
elif (numero>1):
        print("Voici les numéros justes ",resultat)
 

