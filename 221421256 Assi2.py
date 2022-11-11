# Problem 1
def list_check(num):
    """
    Find pattern in num list
    """
    print(2 in num)
list_check([0,2,3])

# Problem 2
def string_bit(str):
    """
    Extract bits from string
    """
    x=0
    y=""
    i = len(str)
    while x <i:
        y =y + str[x]
        x = x+ 2
    print(y)
string_bit("bestie")

# Problem 3
"""
Extract last char of string with less len
"""
def last_char(a,b):
    a= a.lower()
    b= b.lower()
    cd = len(a)
    de = len(b)
    end=""
    count = -1
    if(la>lb):
        e = de
        e = e*-1
        c = b
    else:
        e = cd
        e = e*-1
        c = a
    while e<=count:
        if(la>lb):
            end = end + a[e]
        else:
            end = end + b[e]
        e +=1
    print(c==end)
last_char("Blue","Rediblue")

# Problem 4
def double_value(str):
    """
    Duplicate every char in a string
    """
    dup_char=""
    n = len(str)
    i=0
    while i < n:
        dup_char = dup_char + str[i] + str[i]
        i +=1
    print(dup_char)
double_value("awesoMe")

# Problem 5


# Problem 6
def count_even(even):
    """
    Counting even numbers in array
    """
    even_number =0
    n = len(even)
    i=0
    while i < n:
        if(even[i]%2==0):
            even_number+=1
        i+=1
    print(even_number)
count_even([2,1,2,6,4])
