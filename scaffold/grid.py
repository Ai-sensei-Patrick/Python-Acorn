def water(player):
    if player.num_water_buckets==1:
        count='bucket'
    else:
        count='buckets'
    return'\nYou have {} water {}.\n'.format(player.num_water_buckets,count)

def grid_to_string(grid,player):
    new_list=[]
    i=0
    while i < len(grid):
        j=0
        grid[i]
        new_list.append([])
        while j < len(grid[i]):
            if i == player.row and j == player.col:
                new_list[i].append('A')
            else:
                new_list[i].append(grid[i][j].display)
            j+=1
        i+=1

    new_list_2=[]
    for i in new_list:
        string=""
        for j in i:
            string+=j
        new_list_2.append(string)

    new_list_3=[]
    for i in new_list_2:
        i+='\n'
        new_list_3.append(i)

    new_list_3.append(water(player))
    final=''
    for i in new_list_3:
        final+=i
    return final
