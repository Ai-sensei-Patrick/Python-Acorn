from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def read_lines(filename):
    file=open(filename,'r')
    lines=file.readlines()
    file.close()
    output=parse(lines)
    return output

def parse(lines):
        i=0
        new_list=[]
        while len(lines)>i:
            string_new=lines[i].split('\n')
            new_list.append(string_new)
            i+=1


        new_list_2=[]
        x=-1
        for i in new_list:
            new_list_2.append([])
            x+=1
            for j in i:
                for k in range(len(j)):
                    new_list_2[x].append(j[k])


        compare=['W','Y',' ','X','*','F','1','2','3','4','5','6','7','8','9']
        for i in new_list:
            for j in i:
                for z in j:
                    if z not in compare:
                        raise ValueError('Bad letter in configuration file: {}.'.format(z))

        total_x=0
        for i in new_list:
            for j in i:
                total_x+=j.count('X')
        if total_x!=1:
            raise ValueError('Expected 1 starting position, got {}.'.format(total_x))

        total_y=0
        for i in new_list:
            for j in i:
                total_y+=j.count('Y')
        if total_y!=1:
            raise ValueError('Expected 1 ending position, got {}.'.format(total_y))

        allow=['1','2','3','4','5','6','7','8','9']
        compare=[]
        for i in new_list:
            for j in i:
                for k in j:
                    if k in allow:
                        compare.append(k)
        total_com=0
        i=0
        while len(compare)>i:
            total_com+=compare.count(compare[i])
            if total_com != 2:
                raise ValueError('Teleport pad {} does not have '\
                'an exclusively matching pad.'.format(compare[i]))
            else:
                total_com=0
            i+=1


        new_list_3=[]
        x=-1
        for i in new_list_2:
            new_list_3.append([])
            allow=['1','2','3','4','5','6','7','8','9']
            for j in i :
                if j == '*':
                    new_list_3[x].append(Wall())
                elif j ==' ':
                    new_list_3[x].append(Air())
                elif j =='X':
                    new_list_3[x].append(Start())
                elif j == 'Y':
                    new_list_3[x].append(End())
                elif j == 'W':
                    new_list_3[x].append(Water())
                elif j == 'F':
                    new_list_3[x].append(Fire())
                elif j in allow:
                    new_list_3[x].append(Teleport(j))

        return new_list_3
