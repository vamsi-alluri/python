def sublist_duplicates(lst):
    sublists = []

    for item in set(lst):
        sublists.append([item] * lst.count(item))

    return sublists

lst_of_duplicates = [1, 2, 10, 3, 4, 1, 's', 2, 3, 1, 4, 's']

print sublist_duplicates(lst_of_duplicates)
