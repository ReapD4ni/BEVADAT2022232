# %%
import numpy as np

# %%
def column_swap(arr):
    result = [row[:] for row in arr]
    rows = len(arr)
    cols = len(arr[1])
    for i in range(cols):
        for j in range(rows):
            result[j][i] = arr[j][cols-i-1]
    return result

# %%
def compare_two_array(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            answer.append(i)
    return answer


# %%
def get_array_shape(arr):
    if len(arr.shape)==1:
        print(f"sor: {arr.shape[0]}, oszlop: 1")
    elif len(arr.shape)==2:
        print(f"sor: {arr.shape[0]}, oszlop: {arr.shape[1]}, melyseg: 1")
    elif len(arr.shape)==3:
        print(f"sor: {arr.shape[0]}, oszlop: {arr.shape[1]}, melyseg: {arr.shape[2]}")

# %%
def encode_Y(arr, n):
    answer = []
    for i in arr:
        ones = [0] * n
        if i != 0:
            ones[i] = 1
        answer.append(ones)
    return answer

# %%
def decode_Y(arr):
    answer=[]
    for i in arr:
        if sum(i) == 0:
            answer.append(0)
        else:
            answer.append(i.index(1))
    return answer

# %%
def eval_classification(l, arr):
    index=arr.index(max(arr))
    return l[index]

# %%
def repalce_odd_numbers(arr):
    answer=[]
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            answer.append(-1)
        else:
            answer.append(arr[i])
    return answer

# %%
def replace_by_value(arr, value):
    answer=[]
    for i in range(len(arr)):
        if value > arr[i]:
            answer.append(-1)
        else:
            answer.append(1)
    return answer

# %%
def array_multi(arr):
    return np.prod(arr.flatten())

# %%
def array_multi_2d(arr):
    answer=[]
    for i in range(len(arr)):
        answer.append(np.prod(arr[i]))
    return answer

# %%
def add_border(arr):
    m,n =arr.shape
    answer=np.zeros((m+2,n+2))
    answer[1:-1,1:-1]=arr
    return answer

# %%
from datetime import date, timedelta

def list_days(date1, date2):
    x = date.fromisoformat(date1)
    y = date.fromisoformat(date2)
    delta = timedelta(days=1)
    days = []
    while x <= y:
        days.append(x.isoformat())
        x += delta
    return days

# %%
from datetime import date

def datetime_now():
    x= date.today()
    print(x)

# %%
import time
def sec_from_1970():
    return int(time.time())


