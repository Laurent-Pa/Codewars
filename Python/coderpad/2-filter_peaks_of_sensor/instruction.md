VOtre entreprise fabrique des capteurs de radioactivité. VOus êtes responsable de leur processus de vérification. Vous savez que lorsqu'un capteur est ddéfaillant, la valeur qu'il délivre présente de grandes variations sur de courtes périodes.
Le paramètre d'entrée values, une liste de nombres décimaux, contient la radioactivité mesurée par le capteur chaque seconde, en unité arbitraire.

Vous voulez comper la quantité de pics dans ces valeurs, ce qui vous aidera à déterminer si le capteur est défectueux.
Lorsqu'une valeur es supérieure d'au moins 5 unités à ses deux voisines, il s'agit d'un pic supérieur
Lorsqu'une valeur est inférieure d'au moins 5 unités à ses deux voisines, il s'agit d'iun pic inférieur.

TESTS A VALIDER

[8, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7] --> valeur de retour 3
2 pics de 5 unités exactement --> retour 2
