def solve(n):
    somme=0
    a=2**n
    while a!=0:
        somme+=a%10
        a=a//10
    return somme

assert solve(15) == 26

print(solve(15))
            
        
    
    