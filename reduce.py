import json


d1 = {'a': 2, 'b': 3, 'c': 4}
d2 = {'d': 2, 'e': 3, 'f': 4}
d3 = {'g': 2, 'h': 3, 'd': 4}
d4 = {'a': 2, 'b': 3, 'c': 4}


l = [d1, d2, d3, d4]


def readMapFile(urls):
    for url in urls:
        
    with open('file.json', 'r') as f:
        distros_dict = json.load(f)
        print(distros_dict["fruit"])
    
    
    
def reduce(listdict):
    res = {}
    for dic in listdict:
        for key, value in dic.items():
            if key in res.keys():
                res[key] = res[key] + value
            else:
                res[key] = value
    return res


readMapFile(1)

#print(reduce(l))