
def parse_input():
    fin = open('input_day3.txt','r')
    inputs = []
    for line in fin:
        inputs.append(line.strip('\n'))
    return inputs
    
def plot_path(inputs, path, find_intersections=False):
    x=0
    y=0
    hits = []
    for i in inputs.split(','):
        (d, v) = (i[0],int(i[1:]))
        fn = lambda x,y,p: (x,y)
        
        if d == 'R':
            fn = lambda x,y: (x + 1, y)
        elif d == 'L':
            fn = lambda x,y: (x - 1, y)
        elif d == 'U':
            fn = lambda x,y: (x, y + 1)
        elif d == 'D':
            fn = lambda x,y: (x, y - 1)
        
        for p in range(1,v+1):
            x,y = fn(x,y)
            if find_intersections:
                key = "{}_{}".format(x,y)
                if key in path:
                    hits.append(key)
            else:
                path["{}_{}".format(x,y)] = 1
    return hits

def find_manhattan_dist(hits):
    md_list = []
    for h in hits:
        (x,y) = map(int,h.split('_'))
        md_list.append(abs(x) + abs(y))
    return md_list

if __name__ == '__main__':
    inputs = parse_input()
    w1_path = {}

    plot_path(inputs[0], w1_path)
    hits = plot_path(inputs[1], w1_path, True)
    print('hits', hits)
    
    md_list = find_manhattan_dist(hits)
    print('manhattan distances', md_list)
    print('Shortest', min(md_list))
    
