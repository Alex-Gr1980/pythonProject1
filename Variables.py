def second_f(a: int, b:int):
    return a+b

def first_f (func):
    print("Starting")
    print(f"Result: {func}")

def prov(a,b,c):
    k1=a/c
    k2=b/c
    if int(k1) ==k1 and int(k2) ==k2:
        return c
    else:
        return 0

def delit(a:int, b:int) -> int:
    k=1
    result=0
    if a>b or a==b:
        while k<(b/2):
            if prov(a,b,k)>0:
                result=k
            k+=1
    else:
        while k<(a/2):
            if prov(a,b,k)>0:
                result=k
            k+=1
    return result

print(delit(72,48))






