_s = ""
print(_s)
print("="*20)
print("Autoplication")
print("="*20)
print(_s)
print("<>"*20)
print("Life made simpler for primary grade students")
print("'multi-autoplication'")
print("<>"*20)
print(_s)
_beautification_1 = "|"
_beautification_2 = "-"
try:
    num=int(input("Enter the number:"))
    for a in range(1,11):
        mult=num*a
        print(_beautification_2*20)
        print(_beautification_1+(str(num)),"x",a,"=",(str(mult))+_beautification_1)
    print(_beautification_2*20)
    print(_s) 
    print("#Welcome back in advance#")
    print(_s)
except:
    if ValueError:
        print("Your input should be an integer")    
