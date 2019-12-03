
def get_checksum():
    fin = open('input.txt','r')
    count ={ 'two': 0, 'three': 0 }
    
    for line in fin:
        l = line.strip('\n')
        
        # build map of characters
        cmap = {}                   
        for x in l:
            cmap[x] = cmap.get(x,0) + 1
        
        # check for 2 or 3 occurances
        vlist = cmap.values()
        if 2 in vlist:
            count['two']+=1
        if 3 in vlist:
            count['three']+=1
    
    fin.close()
    return count['two'] * count['three']

def find_seq():
    fin = open('input.txt','r')
    inputs = []
    for line in fin:
        inputs.append(line.strip('\n'))
    noi = len(inputs)

    # brute force comparison
    for i in range(0,noi): 
        for j in range(i+1,noi):
            x = inputs[i]
            y = inputs[j]
            counter = 0
            for a,b in zip(x,y):
                if a != b:
                    counter+=1
                    if counter > 1:
                        break
            if counter <= 1:
                print('matches', x , y)
                z = ""
                for a,b in zip(x,y):
                    if a == b:
                        z+=a
                return z

if __name__ == '__main__':
    checksum = get_checksum()
    print('count', checksum)
    seq = find_seq()
    print('sequence', seq)
