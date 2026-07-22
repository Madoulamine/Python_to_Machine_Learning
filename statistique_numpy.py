import numpy as np

# calculons l statistique d'un tableau à 2dimensions avec numpy sur le poids et la taille d'un groupe de personnes

# definition des valeurs avec numpy
poids = np.array([
    [70, 80, 90]
])

taille = np.array([
    [1.70, 1.80, 1.90]
])

print(f"\nLe poids est: {poids}")
print(f"\nLa taille est: {taille}")

np_taille = np.round(np.random.normal(1.80, 0.2, 5000), 2)
np_poids = np.round(np.random.normal(80, 50, 5000), 2)

np_conakry = np.column_stack((taille, poids))

print("\n Le tableau de taille et poids est: \n", np_conakry)

# la taille moyenne de conakry
taille_moyenne = np.nanmean(np_taille)
print(f"\nLa taille moyenne de conakry est: {taille_moyenne}")

# le poids moyen de conakry
poids_moyen = np.nanmean(np_poids)
print(f"\nLe poids moyen de conakry est: {poids_moyen}")

# la mediane de la taille de conakry
taille_mediane = np.nanmedian(np_taille)
print(f"\nLa taille mediane de conakry est: {taille}")