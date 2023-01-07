import string

data = [x for x in range(11)]
data_1 = [y for y in string.ascii_letters + string.printable]
# print(data_1.count('a'))


def get_data(var:str):
    new_data = []
    for i in range(len(data_1)):
        if data_1[i] == var:
            new_data.append(data_1[i])
    return new_data


new_data = get_data('a')
print(new_data)

new_data_0 = get_data('c')
print(new_data_0)


def comp(actual: str, expected = 'd'):
    return actual == expected


newest_data = filter(comp, data)
print(list(newest_data))

