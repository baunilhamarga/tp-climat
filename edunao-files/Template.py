# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Canevas de code python pour le le TD Climat et transition énergétique du 6 mai 2026.
Ce document vous fournit :
    une liste des modules pythons à importer
    un modèle pour l’import de table de données formatées en .csv selon les habitudes françaises
    les paramètres permettant d’écrire les étiquettes de temps sur l’axe d’une figure avec un pas de temps mensuel sous la forme «Mois»
    un canevas de tracé de  courbes de données indexées sur le temps, avec titres et étiquettes, ainsi qu’une fonction d’export.

@author: Martin Hennebel
"""
# modules utiles à importer
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import locale #pour paramètre locaux de date
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8') # choix des dates en format Français

#%% liens vers les docs de fonctions pandas utiles 
"""
10 minutes d’introduction à pandas
https://pandas.pydata.org/docs/user_guide/10min.html
Un tutoriel pour débuter avec les séries temporelles dans pandas :
https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html    
Notice pour traiter les séries temporelles avec pandas
https://pandas.pydata.org/docs/user_guide/timeseries.html

Notices des fonctions pandas permettant de traiter des tables de données «Dataframe»
https://pandas.pydata.org/docs/reference/frame.html
    
parmi ces fonctions certaines à regarder :
    Indexage :
pandas.DataFrame.index()      pour récupérer l’index des lignes
pandas.DataFrame.columns()    pour récupérer les titres des colonnes    
pandas.DataFrame.dtypes()     pour récupérer les types de données dans la table
pandas.DataFrame.loc()        pour extraire des données localisées par leurs étiquettes
pandas.DataFrame.iloc()       pour extraire des données localisées par leurs positions (nombres entiers)
    traitement des valeurs 
pandas.DataFrame.max()        pour obtenir le maximum (min pour le minimum)
pandas.DataFrame.idxmax()     pour obtenir l’indice du maximum (min pour le minimum)
pandas.DataFrame.nlargest()   pour obtenir les n plus grandes valeurs (nsmallest pour les plus petites)
pandas.DataFrame.sum(numeric_only=True)    pour sommer les contenus des colonnes (nombres uniquement)
pandas.DataFrame.mean()       pour moyenner les contenus des colonnes


    
pandas.DataFrame.to_timestamp()   pour transformer des index en format temporel
pandas.DataFrame.tz_convert()    pour convertir un index temporel d’un fuseau horaire à un autre (Continental European Time pour Paris)
pandas.DataFrame.tz_localize()    pour affecter un fuseau horaire à un index temporel naïf
pandas.to_datetime              pour convertir des arguments en date + heure (datetime)
pandas.DataFrame.sort_values    pour trier les valeurs par ordre

…
"""




#%% Modèle d’import de données en csv formaté à la française (; en séparateur, virgule comme séparteur décimal, formatage des dates)
donnees_importees_Pays_annee=pd.read_csv('Table_Donnees.csv',sep=';',decimal=',',index_col=[0],parse_dates=[0],date_format="ISO8601")

#%% paramètres des étiquettes temporelles pour l’axe du temps dans les figures. 
  # intervalle mensuel pour les étiquettes
Mois=mdates.MonthLocator(bymonthday=1)# chaque mois, le premier jour du mois.
  #format affichage Mois : 
MoisFmt = mdates.DateFormatter('%b')# nom du mois abrégé sur 4 lettres.
#Hours = mdates.HourLocator()   #


#%%Template de Tracé d’une figure
  #On crée le repère        
fig, ax = plt.subplots()
  #tracé de la courbe conso vs temps, avec des valeurs de divisées par 1000, pour une table de données indexée sur le temps.
ax.plot(Table_Donnees.index,(Table_Donnes['Nom_Colonne_Donnees'].values/1000), linewidth=.5)

   #affichage du titre
plt.title('Titre de la figure')
#Limites min et max de l’axe x
ax.set_xlim(Table_Donnees.index[0],Table_Donnees.index[-1])

#positionnement des étiquettes de temps à chaque mois
ax.xaxis.set_major_locator(Mois)
#format des étiquettes de temps
ax.xaxis.set_major_formatter(MoisFmt)
#légende de l'axe des abscisses
plt.xlabel('Mois')

#Limites min max de l’axe y
ax.set_ylim(0,100)
#légende de l'axe des ordonnées
plt.ylabel('Valeurs (Unité)')


# affichage de la grille pour faciliter la lecture des valeurs
plt.grid(True)
# affichage de la figure
plt.show()
#sauvegarde de la figure en .svg :
plt.savefig(r'Adresse\du\Repertoire\' + 'Nom_Fichier.svg')
#les enregistrement de figure doivent être fait en format vectoriel : .svg, .emf, .eps
# Éviter les enregistrements en format matriciels, lourds et flou en agrandissement : .bmp, .jpg …




