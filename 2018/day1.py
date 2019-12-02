

def part_one():
    fin = open('input_day1.txt','r')
    sum = 0
    for line in fin:
        op = line.strip('\n')
        if op[0] == '+':
            sum = sum + int(op[1:])
        elif op[0] == '-':
            sum = sum - int(op[1:])
    return sum


def part_two():
    fin = open('input_day1.txt','r')
    found = False
    freq_list = {}
    sum = 0;
    while not found:
        for line in fin:
            op = line.strip('\n')
            if op[0] == '+':
                sum = sum + int(op[1:])
            elif op[0] == '-':
                sum = sum - int(op[1:])
            if sum in freq_list:
                return sum
            else:
                freq_list[sum] = 1
    
        fin.seek(0)

    return sum

if __name__ == '__main__':
    sum = part_one()
    print('output',sum);
    freq = part_two();
    print('freq', freq);
    