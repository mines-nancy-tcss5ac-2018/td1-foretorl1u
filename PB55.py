def solve():
    lych=[]
    for i in range(1,10000):
        a=str(i)
        compt=1
        while palindrome(a)==False and compt<=50:
            a=str(reverse(a))
            compt+=1
        if palindrome(a)==False:
            lych.append(i)
    print(lych)
    return len(lych)
            
            

def palindrome(str):
    for i in range(len(str)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
     


def reverse(str):
    a=''
    for i in range(len(str)):
        a+=str[len(str)-i-1]
    rev=int(str)+int(a)
    return rev