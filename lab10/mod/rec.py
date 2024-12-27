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


#___________________________________________________________________________#

def calculate_a_iterative(n):
    a = [1, 1]
    for i in range(2, n+1):
        a.append(a[i-2] + a[i-1] / (2**(i-1)))
    return a[n]
