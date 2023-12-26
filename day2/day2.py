import re

data = open('input.txt','r')

pattern = re.compile(r'(\d+)\s+(\w+)') 
game_id_pattern = re.compile(r'\d:|\d\d:|\d\d\d:')

id_sum = 0

max_balls = {'blue':14,'green':13,'red':12}

for line in data:
    is_added = True
    game_id = re.findall(game_id_pattern,line)
    matches = re.findall(pattern,line)
    for i in matches:
        if max_balls[i[1]] < int(i[0]):
            is_added = False
            break
    if is_added:
        id_sum += (int(game_id[0][:-1]))
print(id_sum)
