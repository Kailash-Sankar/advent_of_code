def get_input():
    fin = open('input_day6.txt', 'r')
    inputs = []
    for line in fin:
        inputs.append(line.strip('\n'))
    return inputs


# input format
# COM)B
def build_orbit_map(inputs, om):
    planets = set()
    for i in inputs:
        x,y = i.split(')')
        om[y] = x
        planets.add(x)
        planets.add(y)
    count = 0
    for v in planets:
        key = om.get(v, False)
        while key:
            count+=1
            key  = om.get(key, False)
    return count


def build_path(p,om,p_map):
    path = []
    key = om.get(p,False)
    while key:
        path.append(key)
        p_map[key] = len(path)-1
        key = om.get(key,False)
    return path
        
def find_path(p1,p2,om):
    p_map = {}
    path_1 = build_path(p1,om,p_map)

    # find common ancestor
    key = om.get(p2,False)
    steps = 0
    while key:
        if key in p_map:
            break
        else:
            steps+=1
        key = om.get(key,False)
    # add steps from 1 and 2
    total = p_map[key] + steps
    return total

if __name__ == '__main__':
    inputs = get_input()
    orbit_map = {}
    count = build_orbit_map(inputs,orbit_map)
    print('count',count)
    
    total = find_path('YOU','SAN',orbit_map);
    print('total', total)






