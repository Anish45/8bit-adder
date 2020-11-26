def convert_decimal(a):
    decimal_value = 0
    b = 0
    for i in range(len(a)-1,-1,-1):
        decimal_value += int(a[i])* (2**b)
        b = b + 1
    return decimal_value

def convert_binary(a):
    s = ""
    if(a == 0):
        s = "0"
    else:
        while(a != 0):
            b = a%2
            a //=  2
            s = str(b)+s
    eightbitbinary = convert_eightbit(s)
    return eightbitbinary

def convert_eightbit(s):
    eightbit = s
    if(len(s) != 8):
        for i in range(len(s),8):
            eightbit = "0" + eightbit
    return eightbit

convert_decimal("10")
    

    
    
    
