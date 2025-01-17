def calculate_structure_sum(*args):
    count = 0
    for arg in args:
        if isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
            count += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            count += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            count += len(arg)
        elif isinstance(arg, int):
            count += arg
    return count


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)