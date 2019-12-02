

def get_checksum():
    fin = open('input_day2.txt','r')
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
        
    return count['two'] * count['three']


if __name__ == '__main__':
    checksum = get_checksum()
    print('count', checksum);