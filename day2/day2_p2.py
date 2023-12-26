import re

data = open('input.txt','r')

pattern = re.compile(r'(\d+)\s+(\w+)') 
game_id_pattern = re.compile(r'\d:|\d\d:|\d\d\d:')

id_sum = 0

max_balls = {'blue':14,'green':13,'red':12}
powers_sum = 0

for line in data:
    temp = 1
    is_added = True
    game_id = re.findall(game_id_pattern,line)
    matches = re.findall(pattern,line)
    max_found_values = {'blue':0,'green':0,'red':0}
    for i in matches:
        if max_found_values[i[1]] < int(i[0]):
            max_found_values[i[1]] = int(i[0])
    for i in matches:
        if max_balls[i[1]] < int(i[0]):
            is_added = False
            break
    if is_added:
        id_sum += (int(game_id[0][:-1]))
    for value in max_found_values.values():
        temp *= value
    powers_sum += temp
    print('Temp value is : ',temp)

print(id_sum)
print(powers_sum)
