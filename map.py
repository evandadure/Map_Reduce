import re

def map(input_str):
    res = [word.casefold() for word in re.findall(r'\w+', input_str)]
    dict={}
    for word in res:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return(dict)



