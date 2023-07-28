# CONVERT ROMAN NUMBER TO INTEGER NUMBER
def roman2dec(romStr):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romanBack = list(romStr)[::-1]
    value= 0
    rightVal = roman_dict[romanBack[0]]
    for numerical in romanBack:
        leftVal = roman_dict[numerical]
        if leftVal < rightVal:
            value -= leftVal
        else:
            value +=leftVal
        rightVal = leftVal
    return value

romanStr=input("Enter a Roman number:")
print(roman2dec(romanStr))    