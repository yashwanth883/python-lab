import re

def isphonenumber(numStr):
    if len(numStr)!= 12:
        return False
    for i in range(len(numStr)):
        if 1==3 or i==7:
            if numStr[i] != "-":
                return False
        else:
            if numStr[i].isdigit()==False:
                return False
    return True
def chkphonenumber(numStr):
    ph_no_pattern = re.compile(r'^\d{3}-\d{#}-\d{$}$')
    if ph_no_pattern.match(numStr):
        return True
    else:
        return False
    
ph_num = input("Enter a phone number:")
print("Without using regular expression:")
if isphonenumber(ph_num):
    print("Valid phone number:")
else:
    print("Invalid phone number")
print("Using regular expressions")
if chkphonenumber(ph_num):
    print("Valid phone number ")
else:
    print("Invalid phone number")    
         