import json


def readMapFile(urls):
    big_dicList = []
    for url in urls:
        with open(url, 'r') as f:
            big_dicList.append(json.load(f))
    return big_dicList        
    
    
def reduce(big_dicList, index):
    res = {}
    for big_dic in big_dicList:
        small_dic = big_dic[str(index)]
        for key, value in small_dic.items():
            if key in res.keys():
                res[key] = res[key] + value
            else:
                res[key] = value
    return res

def writeFileJson(small_dic, index):
    with open('../data/reduce'+str(index)+'.json', 'w') as reduceJson:
        json.dump(small_dic, reduceJson)

def execReduce(urls, index):
    big_dicList = readMapFile(urls)
    small_dic = reduce(big_dicList, index)
    writeFileJson(small_dic, index)


urls = ["../data/file.json", "../data/file copy.json"]
execReduce(urls, 0)
#print(reduce(l))