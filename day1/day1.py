import re

data = open('input.txt','r')

result = 0

c = 'one two three four five six seven eight nine'.split()
d = '(?=(' + '|'.join(c) + '|\\d))'

def convert(x):
    if x in c:
        return str(c.index(x) + 1)
    return x

for line in data:
    digits = [*map(convert,re.findall(d,line))]
    result += (int(digits[0] + digits[-1]))

print(result)
