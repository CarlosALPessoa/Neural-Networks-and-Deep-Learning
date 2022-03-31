
import os
import numpy as np
import pandas as pd

from pathlib import Path



#?Create a Numpy array filled with all zeros
zeros = np.zeros(3)
print("\n\n", zeros)

#?Create a Numpy array filled with all ones
v_uns = np.ones(3)
print("\n\n", v_uns)

#?Check whether a Numpy array contains a specified row
list_row = np.array([[0, 0, 0], 
                    [1, 1, 1],
                    [2, 2, 2]])

print("\n\n", [0, 0, 0] in list_row.tolist())
print([3, 3, 3] in list_row.tolist())

#?How to Remove rows in Numpy array that contains non-numeric values?
list_row2 = np.array([[0.1, 0.2, 0.3], [1.1, 1.2, 1.3], [np.nan, np.nan, np.nan]])
print("\n\nRemove rows in Numpy array that contains non-numeric values?\n", list_row2)

list_row2 = list_row2[~np.isnan(list_row2).any(axis=1)]
print("\nThat no contains non-numeric values\n", list_row2)

#Remove single-dimensional entries from the shape of an array

array = 