#program to test zero division error
try:
    a=int(input("Enter a numerator"))
    b=int(input("Enter a denominator"))
    c=a/b
    print("result is ",c)
except:
    print("cant be divided by zero")
