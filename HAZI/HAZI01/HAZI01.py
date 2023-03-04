# %%
def subset(input_list,start_index,end_index):
    answer=[]
    i=start_index
    while i<end_index+1:
        answer.append(input_list[i])
        i=i+1
    return answer

# %%
def every_nth(input_list,step_size):
    answer=[]
    for i in range(0,len(list),step_size):
        answer.append(input_list[i])
    return answer

# %%
def unique(input_list):
    return len(input_list) == len(set(input_list))

# %%
def flatten(input_list):
    result = []
    for element in input_list:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

# %%
def merge_lists(*args):
    answer = []
    for lst in args:
        answer += lst
    return answer

# %%
def reverse_tuples(input_list):
    answer=[]
    for i in input_list:
        answer.append(tuple(reversed(i)))
    return answer

# %%
def remove_tuplicates(input_list):
    answer=set(input_list)
    return answer

# %%
def transpose(input_list):
    return [list(i) for i in zip(*input_list)]

# %%
def split_into_chunks(input_list, chunk_size):
    answer = []
    for i in range(0, len(input_list), chunk_size):
        answer.append(input_list[i:i+chunk_size])
    return answer

# %%
def merge_dicts(*dicts):
    answer = {}
    for d in dicts:
        answer.update(d)
    return answer

# %%
def by_parity(input_list):
    even = []
    odd = []
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return {"even": sorted(even), "odd": sorted(odd)}


