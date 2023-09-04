def list_to_dict(lst):
    return {index: value for index, value in enumerate(lst)}

input_list = ['a', 'b', 'c', 'd', 'e']
output_dict = list_to_dict(input_list)
print(output_dict)