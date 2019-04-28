#Assisting functions
def formatNum(a):
    a = str(a)
    temp = ""
    a = a[::-1]
    i = 0
    while (i < len(a)):
        if (len(a) == 6):
            temp = a[:3] + "." + a[3:]
            break
        if (i != 0 and i % 3 == 0):
            b = a[:i] + "."
            a = a[i:]
            temp += b
            i -= 3
        if (len(a) <= 3):
            temp += a
            break
        i += 1
    return temp[::-1]

def format_currency(a):
    b = str(a)
    return b + " kr."
