def individual_merge(list1, list2):
    lst = []
    for i in range(len(list1)):
        lst.append((round(list1[i], 3), round(list2[i], 3)))
    return lst
