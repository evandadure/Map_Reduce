f = open('data/text.txt', 'r')
text = f.read()

with open('data/text.txt', 'w') as f:
    f.write(text+text)
f.close()