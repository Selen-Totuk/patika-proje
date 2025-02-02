#1.sorunun cevabı
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten_list(input_list)
print(output_list)  



#2.sorunun cevabı
def reverse_list(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    reversed_list.reverse()
    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)  # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]
