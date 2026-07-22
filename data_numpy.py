import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
)
print(a+a) # c'est la force de numpy et la differance entre numpy et Liste
print(type(a))
print("\t########################################################\n")

# Faisons la difference entre numpy et Liste
list_python = [2, 4, 6, 8]
list_numpy = np.array([2,4,6,8])

lp = list_python + list_python
ln = list_numpy + list_numpy

print(f"La somme des Listes en Python: {lp}\n")
print(f"La somme des Numpy en Python: {ln}\n")