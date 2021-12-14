def split_list(lst):
    mn = (lst[0] + lst[1]) / 2
    return [lst[0], mn], [mn, lst[1]]
