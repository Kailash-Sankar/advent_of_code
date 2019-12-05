
def get_input():
    # Tests
    #input = '3,0,4,0,99'
    #input = '1002,4,3,4,33'
    #input = '1101,100,-1,4,0'
    #input = '3,3,1107,-1,8,3,4,3,99'
    #input = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
    
    fin = open('input_day5.txt', 'r')
    input = fin.readline().strip('\n')
    return list(map(int,input.split(',')))

def get_fields(n,i,attrs,inst):
    values = []
    for x in range(1,n+1):
        values.append( i+x if attrs[1+x] else inst[i+x] )
    return values

def intcode_compiler(noun, verb, inst):
    i = 0
    noi = len(inst)
    #inst[1] = noun
    #inst[2] = verb

    while i <= noi:
        action = inst[i]
        attrs = list(map(int, list(str(action))[::-1]))
        attrs = attrs + [0]*(5-len(attrs))
               
        op = attrs[0] if attrs[1] == 0 else int('{}{}'.format(attrs[1],attrs[0]))
        step = 0

        if op == 1:
            # add and store           
            (v1,v2,v3) = get_fields(3,i,attrs,inst)          
            inst[v3] = inst[v1] + inst[v2]
            step = i + 4
        elif op == 2:
            # multiply and store
            (v1,v2,v3) = get_fields(3,i,attrs,inst)  
            inst[v3] = inst[v1] * inst[v2]
            step = i + 4
        elif op == 3:
            # read input
            (v1,) = get_fields(1,i,attrs,inst)  
            x = int(input('Enter a value: '))
            inst[v1] = x
            step = i + 2
        elif op == 4:
            # print output
            (v1,) = get_fields(1,i,attrs,inst) 
            print('-->', inst[v1])
            step = i + 2
        elif op == 5:
            # jump if true
            (v1,v2) = get_fields(2,i,attrs,inst)             
            step = inst[v2] if inst[v1] != 0 else i + 3
        elif op == 6:
            # jump if false
            (v1,v2) = get_fields(2,i,attrs,inst)  
            step = inst[v2] if inst[v1] == 0 else i + 3
        elif op == 7:
            # less than
            (v1,v2,v3) = get_fields(3,i,attrs,inst) 
            inst[v3] = 1 if inst[v1] < inst[v2] else 0
            step = i + 4
        elif op == 8:
            # equals
            (v1,v2,v3) = get_fields(3,i,attrs,inst) 
            inst[v3] = 1 if inst[v1] == inst[v2] else 0
            step = i + 4
        elif op == 99:
            # halt
            break
        else:
            print('unknonw op')
            break
        i = step
    
    return inst[0]

if __name__ == '__main__':
    inst = get_input()
    intcode_compiler(0, 0,inst[:])

