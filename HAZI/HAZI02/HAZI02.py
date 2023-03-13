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
    answer = np.zeros((len(arr), n))
    
    for i in range(len(arr)):
        answer[i, arr[i]] = 1
        
    return answer

# %%
def decode_Y(arr):
    return np.argmax(arr, axis=1)
# %%
def eval_classification(l, arr):
    max_index=np.argmax(arr)
    return l[max_index]

# %%
def replace_odd_numbers(arr):
    return np.where(arr % 2 == 1, -1, arr)

# %%
def replace_by_value(arr, value):
    return np.where(arr < value, -1, 1)

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
from datetime import datetime, timedelta

def list_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m')
    end = datetime.strptime(end_date, '%Y-%m')
    num_days = (end - start).days + 1
    days = np.array([start + timedelta(days=i) for i in range(num_days)])
    days_str = np.array([d.strftime('%Y-%m-%d') for d in days])
    return days_str

# %%
from datetime import datetime

def get_act_date():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    print(np.datetime64(date_str))

# %%
import time
def sec_from_1970():
    return int(time.time())

