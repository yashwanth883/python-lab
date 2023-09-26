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





def roman_to_integer(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_dict[char]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result

roman_numeral = input("Enter a Roman numeral: ").upper()
integer_value = roman_to_integer(roman_numeral)

print(f"The integer value of {roman_numeral} is {integer_value}")
