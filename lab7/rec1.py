def to_str(input_list, is_outer=True,):
    if not input_list:
        return "None"
    elif isinstance(input_list, list):
        result = [to_str(item, False) for item in input_list]
        if is_outer:
            return ' -> '.join(result) + ' -> None' 
        else:
            return ' -> '.join(result)
    else:
        return str(input_list) if input_list is not "None" else 'None'


result = to_str([1, [2, [3, [4, [5]]]]])
result2 = to_str([])
result3 = to_str([1, [2]])


print(result)
print(result2)
print(result3)