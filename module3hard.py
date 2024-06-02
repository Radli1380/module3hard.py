def count_numbers_and_strings(data_structure):
    numbers_sum = 0
    strings_length = 0

    def process_item(item):
        nonlocal numbers_sum, strings_length
        if isinstance(item, int):
            numbers_sum += item
        elif isinstance(item, str):
            strings_length += len(item)
        elif isinstance(item, (list, tuple)):
            for element in item:
                process_item(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                process_item(key)
                process_item(value)

    for item in data_structure:
        process_item(item)

    return numbers_sum, strings_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    [{(2, 'Urban', ('Urban2', 35))}]]


numbers_sum, strings_length = count_numbers_and_strings(data_structure)
print("Сумма всех чисел:", numbers_sum)
print("Сумма длин всех строк:", strings_length)

