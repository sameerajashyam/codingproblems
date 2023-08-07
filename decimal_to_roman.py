def print_roman(num):
    if num>=1000:
        print("M",end="")
        print_roman(num-1000)
    elif num>=900:
        print("CM",end="")
        print_roman(num-900)
    elif num>=500:
        print("D",end="")
        print_roman(num-500)
    elif num>=400:
        print("CD",end="")
        print_roman(num-400)
    elif num>100:
        print("C",end="")
        print_roman(num-100)
    elif num>=90:
        print("XC",end="")
        print_roman(num-90)
    elif num>=50:
        print("L",end="")
        print_roman(num-50)
    elif num>=40:
        print("XL",end="")
        print_roman(num-40)
    elif num >= 10:
        print("X", end="")
        print_roman(num - 10)
    elif num >= 9:
        print("IX", end="")
        print_roman(num - 9)
    elif num >= 5:
        print("V", end="")
        print_roman(num - 5)
    elif num >= 4:
        print("IV", end="")
        print_roman(num - 4)
    elif num >= 1:
        print("I", end="")
        print_roman(num - 1)

number = 850
print_roman(number)
