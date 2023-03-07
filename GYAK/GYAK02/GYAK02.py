# %%
import numpy as np

# %%
def create_array(size=input):
    return np.zeros(size)


# %%
def set_one(arr):
    np.fill_diagonal(arr,1)
    return arr


# %%
def do_transpose(matrix):
    return np.transpose(matrix)

# %%
def round_array(array, n):
    return np.round(array,n)

# %%
def bool_array(arr):
    return arr.astype(bool)


# %%
def invert_bool_array(arr):
    return np.logical_not(arr).astype(bool)

# %%
def flatten(arr):
    return arr.flatten()


