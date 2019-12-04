
# d1 = {'a': 2, 'b': 3, 'c': 4}
# d2 = {'d': 2, 'e': 3, 'f': 4}
# d3 = {'g': 2, 'h': 3, 'd': 4}
# d4 = {'a': 2, 'b': 3, 'c': 4}
#
#
# l = [d1, d2, d3, d4]

def reduce(listdict):
    res = {}
    for dic in listdict:
        for key, value in dic.items():
            if key in res.keys():
                res[key] = res[key] + value
            else:
                res[key] = value
    return res
