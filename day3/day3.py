import re

data = open('test.txt', 'r').read().splitlines()

total_sum = 0

added_numbers = {}

pattern = re.compile(r'(\d\d\d|\d\d|\d)')
special_characters = re.compile(r'(\$|\*|\+|\#)')

def find_special_chars(rgx:str,lne:str)->int:
    matches = re.finditer(rgx,lne) 
    for i in matches:
        yield i.start(),i.end()

def find_adjacent_numbers(indexes:tuple,line:str,rgx=None):
    global total_sum
    start_index = (indexes[0])-1
    end_index = (indexes[1])

    if start_index < 0:
        start_index = 0
    if end_index > len(line):
        end_index = len(line)
    
    matches = re.finditer(rgx,line])
    for i in matches:
        if int(i) not in added_numbers:
            print('Found numbers to be added :',i)
            total_sum += int(i)
            added_numbers[int(i)] = True
        continue

for counter,data_line in enumerate(data):
    print(data_line)
    for result in find_special_chars(special_characters,data_line):
        print('Found special characters indexes tuples :',result)
        find_adjacent_numbers(result,data_line,pattern)
            
print(total_sum)
