def to_str(lst):
    if not lst: 
        return "None" 

    result = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            if current:
                stack.extend(reversed(current[1:]))
                stack.append(current[0])
            else:
                result.append("None")
        else:
            result.append(str(current))
    result.append("None")
    return " -> ".join(result)

nested_list = [1, [2, [3, [4, [5]]]]]

print(to_str(nested_list))
print(to_str([]))
print(to_str([1, [2]]))