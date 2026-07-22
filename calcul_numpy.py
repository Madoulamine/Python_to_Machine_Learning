import numpy as np

# calculons un volume sachant la base(b) et la hauteur(h) avec numpy et liste
#v = b * h

#definition des values with numpy
b = np.array([12.2, 21.0, 31.4, 31.8])
h = np.array([1.7, 2.0, 2.1, 2.7])
v = b * h

#definition des values with list
# b = [12.2, 21, 31.14, 31.80]
# h = [1.72, 2, 2.1, 2.7]
# v = b * h

#J'Affiche les answers de ce calcul
print(f"\nle volume avec NUMPY est: {v}")

