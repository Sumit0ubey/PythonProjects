def sort_dict_by_keys(dictionary):
    return dict(sorted(dictionary.items()))

# Test the function
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = sort_dict_by_keys(my_dict)
print("Sorted dictionary by keys:", sorted_dict)
