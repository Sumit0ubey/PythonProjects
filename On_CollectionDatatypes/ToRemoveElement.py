def remove_elements(lst):
    indices_to_remove = [0, 2, 4, 5]
    return [elem for i, elem in enumerate(lst) if i not in indices_to_remove]

# Test the function
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", original_list)
modified_list = remove_elements(original_list)
print("Modified list:", modified_list)
