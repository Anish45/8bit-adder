from Conversion import *

def user_input():
    binarylist = []
    flag = False
    alphabet = ["a","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","(",")","-","+","<",">",",",".","/","?","'",":",";","|","}","{","]","["]
    print("Welcome to the 8bit adder program!!!")
    print("The rules for binary addition are : ")
    print("    0 + 0 = 0   sum = 0  carryout = 0")
    print("    0 + 1 = 1   sum = 1  carryout = 0")
    print("    1 + 0 = 1   sum = 1  carryout = 0")
    print("    1 + 1 = 10  sum = 0  carryout = 1")
    print()
    while ( flag == False):
        value = input("press b or B for binary and d or D for decimal : ")
        if (value.lower() == "d"):
            correctvalue = False
            correctvalue1 = False
            correctvalue2 = False
            while (correctvalue == False):
                while(correctvalue1 == False):
                    num1 = input("Enter first decimal number : ")
                    try:
                        if(num1 == ""):
                            print("Empty values not accepted as input")
                            continue
                        d1 = int(num1)
                        if(0>d1 or d1>255):
                            print("Note : The value cannot be greater than 255 and smaller than 0")
                            continue
                        else:
                            correctvalue1 = True
                    except:
                        try:
                            float(num1)
                            print("Number with float and double values are not accepted as input")
                            continue
                        except:
                            print("Alphabet or special characters not accepted as input")
                            continue
                while(correctvalue2 == False):
                    num2 = input("Enter second decimal number : ")
                    try:
                        if(num2 == ""):
                            print("Empty values not accepted as input")
                        d2 = int(num2)
                        if(0>d2 or d2>255):
                            print("Note : The value cannot be greater than 255 and smaller than 0")
                            continue
                        else:
                            correctvalue2 = True
                    except:
                        try:
                            float(num2)
                            print("Number with float and double values are not accepted as input")
                            continue
                        except:
                            print("Alphabets or special character not accepted as input")
                            continue
                correctvalue = isValueCorrect(d1,d2,value)
                if(correctvalue == False):
                    print("Please input the values in such a way that their sum is not greater than 255")
                    correctvalue2 = False 
            binarylist.append(convert_binary(d1))
            binarylist.append(convert_binary(d2))
            flag = True
            return binarylist

        elif(value.lower() == "b"):
            correctvalue = False
            validvalue = False
            correctvalue1 = False
            correctvalue2 = False
            while(correctvalue == False): 
                while(correctvalue1 == False):                        
                    b1 = input("Enter the  first binary number : ")
                    if(validBinaryValue(b1)):
                        if(convert_decimal(b1) < 0 or convert_decimal(b1) > 255):
                            print("Note  :the value cannot be grater than 11111111 or the value cannot be smaller then 00000000")
                            continue
                        else:
                            correctvalue1 = True
                    elif(b1 == ""):
                        print("The empty value is not accepted")
                    elif(b1.lower() in alphabet):
                        print("The alphabets or any special characters are not accepted")
                    else:
                        print("The entered number is not a binary number")
                        print("Note : Binary number contains only 0 and 1 without decimal")
                        continue
                while(correctvalue2 == False):
                    b2 = input("Enter the  second binary number : ")
                    if(validBinaryValue(b2)):
                        if(convert_decimal(b2) < 0 or convert_decimal(b2) > 255):
                            print("Note  :the value cannot be grater than 11111111 or the value cannot be smaller then 00000000")
                            continue
                        else:
                            correctvalue2 = True
                    elif(b2 == ""):
                        print("The empty value is not accepted")
                    elif(b2.lower() in alphabet):
                        print("The alphabets or any special characters are not accepted are not accepted")
                    else:
                        print("The entered number is not binary numbers")
                        print("Note : Binary number contains only 0 and 1 without decimal")
                        continue
                correctvalue = isValueCorrect(b1,b2,value)
                if(correctvalue == False):
                    print("please input the values in such a way that their sum is not greater than 11111111")
                    print()
                    continue
                else:
                    correctvalue = True
            binarylist.append(convert_eightbit(b1))
            binarylist.append(convert_eightbit(b2))
            flag = True
            return binarylist
        elif(value == ""):
            print("The empty value cannot be accepted")
        elif(value.lower() in alphabet):
            print("The value except alphabet b and d or any special characters are not accepted")
        else:
            print("You cannot enter any positive or negative integer and decimal numbers")


def validBinaryValue(inputvalue):
        validation = False
        for i in inputvalue:
            if(i in ["0","1"]):
                validation = True
            else:
                validation =  False
                break
        return validation

def isValueCorrect(x,y,value):
        if(value.lower() == "d"):
            if(x+y > 255):
                return False
            else:
                return True
        elif(value.lower() == "b"):
            if((convert_decimal(x) + convert_decimal(y)) > 255):
                return False
            else:
                return True
            
                    
                
                    
            
            
                
                
            
