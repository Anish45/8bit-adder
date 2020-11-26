from input import *

def main():
    flag = False
    while(flag == False):
        binarylist = user_input()
        binaryNum1 = binarylist[0]
        binaryNum2 = binarylist[1]
        print("The eight bit binary digit of the input is: "+binaryNum1 +" and"+binaryNum2)
        print()
        sum = ""
        carry_in = "0"
        print("Adding in binary \t Adding in decimal")
        print(binaryNum1+"\t\t\t",convert_decimal(binaryNum1),"\n")
        print(binaryNum2+"\t\t\t",convert_decimal(binaryNum2),"\n")
        for i in range(len(binaryNum1)-1,-1,-1):
            if(carry_in == "1"):
                if(binaryNum1[i] == "1" and binaryNum2[i] == "1" and carry_in == "1"):
                   sum = "1" + sum
                   carry_out = "1"
                elif(binaryNum1[i] == "0" and binaryNum2[i] == "0"  and carry_in == "1"):
                    sum = "1" + sum
                    carry_out = "0"
                elif(binaryNum1[i] == "1" and binaryNum2[i] == "0" and carry_in == "1"):
                    sum = "0" + sum
                    carry_out = "1"
                elif(binaryNum1[i] == "0" and binaryNum2[i] == "1" and carry_in == "1"):
                    sum = "0" + sum
                    carry_out = "1"
            else:
                if(binaryNum1[i] == "1" and binaryNum2[i] == "1"):
                    sum  = "0" + sum
                    carry_out = "1"
                elif(binaryNum1[i] == "0" and binaryNum2[i] == "0"):
                    sum = "0" + sum
                    carry_out = "0"
                elif(binaryNum1[i] == "1" and binaryNum2[i] == "0" ):
                    sum = "1" + sum
                    carry_out = "0"
                elif(binaryNum1[i] == "0" and binaryNum2[i] == "1"):
                    sum = "1" + sum
                    carry_out = "0"
            carry_in = carry_out
        sumindecimal = convert_decimal(binaryNum1) + convert_decimal(binaryNum2)
        print("The sum is : " +sum + "\t" + " The sum is : " ,sumindecimal)
        print()
        print("Do you want to continue?")
        input_value = False
        while(input_value == False):            
            type = input("press C or c to continue and E or e to exit! : ")
            if(type.lower() == "c"):
                flag = False
                input_value = True
            elif(type.lower() == "e"):
                flag = True
                input_value = True
                print("Thank you for using this program!!")
            elif(type == ""):
                print("The empty value is not accepted")
            else:
                print("please input the correct value")


main()
        
        
                
                    
