import re

data = open('test.txt', 'r').read().splitlines()

total_sum = 0

added_lines = {}

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
    
    matches = re.finditer(rgx,line)
    for i in matches:
        if start_index + 1 in i.span():
            total_sum += int(i.group())
            print(i.group(), 'added to total sum.')
        if end_index in i.span():
            total_sum += int(i.group())
            print(i.group(), 'added to total sum.')

def find_other_lines_numbers(indexes:tuple,line:str,rgx=None):
    global total_sum
    start_index = (indexes[0]) - 1 
    end_index = (indexes[1])

    if start_index < 0:
        start_index = 0
    if end_index > len(line):
        end_index = len(line)

    matches = re.finditer(rgx,line)
    for i in matches:
        if start_index in i.span():
            total_sum += int(i.group())
            print(i.group(), 'added to total sum.')
        if end_index in i.span():
            total_sum += int(i.group())
            print(i.group(), 'added to total sum.')

for indx,data_line in enumerate(data):
    print(data_line)
    for result in find_special_chars(special_characters,data_line):
        print('Found special characters indexes tuples :',result)
        find_adjacent_numbers(result,data_line,pattern)
        if data[indx-1]:
            find_other_lines_numbers(result,data[-1],pattern)
        if data[indx+1]:
            find_other_lines_numbers(result,data[indx+1],pattern)

print(total_sum)
