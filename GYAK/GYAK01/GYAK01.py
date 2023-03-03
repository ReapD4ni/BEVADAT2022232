# %%
list=[2,3,4]
def contains_odd(input_list):
    answer=False
    for i in input_list:
        if i%2!=0:
            answer=True
            break
        else:
            answer=False
    print(answer)

contains_odd(list)

# %%
list=[2,3,4]
def is_odd(input_list):
    answer=[]
    for i in input_list:
        if i%2!=0:
            answer.append(True)
        else:
            answer.append(False)
    print(answer)

is_odd(list)

# %%
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
def element_wise_sum(input_list_1, input_list_2):
    if len(input_list_1) != len(input_list_2):
        return None  # lists must be of equal length

    answer=[]
    for i in range(len(input_list_1)):
        answer.append(input_list_1[i] + input_list_2[i])

    return answer
element_wise_sum(list_1, list_2)

# %%
person={
    "first_name":"John",
    "last_name":"Doe",
    "age":25,
    "active":True}
answer=[]
def dict_to_list(input_dict):
    for key, value in input_dict.items():
        answer.append(f"({key}, {value})")
    return answer

dict_to_list(person)

