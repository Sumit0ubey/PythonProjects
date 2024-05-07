def have_common_element(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  value = len(set1.intersection(set2))
  if value > 0:
    print("True, they have one or more elements in common.")
  else:
    print("They don't have any elements in common.")


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 4, 9]

have_common_element(list1, list2)
