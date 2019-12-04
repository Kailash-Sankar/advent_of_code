
def validate_pwd(p):
    digits = list(map(int,list(str(p))))
   
    # rules
    inc = True
    double = False
    
    # when a valid double is found, skip further checks
    found_d = False    
    
    lmt = len(digits) - 1
    prev = None
    for i in range(lmt):        
        if digits[i] > digits[i+1]:            
            inc = False
        if not found_d and digits[i] == digits[i+1]:
            double = True
            # double rule becomes invalid if the digit is part of a larger group
            if prev is not None and prev == digits[i]:
                double = False
            else:
                prev = digits[i]
        else:
            # reset
            prev= None
            # skip further double rule checks
            if double:
                found_d = True

    if inc and double:        
        return True
        
    
    return False
        


if __name__ == '__main__':
    count = 0
    # test cases
    # for i in (112233, 123444, 111122, 111144, 355556, 355666):
    for i in range(353096,843212+1):    
        out = validate_pwd(i)
        if out:
            count+=1
    print('matching pwds count', count)