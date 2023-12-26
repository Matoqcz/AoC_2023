import re

data = open('test.txt', 'r').read().splitlines()

total_sum = 0

added_numbers = {}

pattern = re.compile(r'(\d\d\d|\d\d|\d)')
special_characters = re.compile(r'(\$|\*|\+|\#)')

def find_special_chars(rgx:str,lne:str)->int:
    matches = re.finditer(rgx,lne) 
    for i in matches:
        yield i.group()

def find_numbers(indexes:tuple,line:str,rgx=None):
    start = indexes[0]-1
    end = indexes[1]+1
    print(start,end)

for i,j in enumerate(data):
    for i in find_special_chars(special_characters,j):
        print(i)
