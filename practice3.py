a = int(input())
n = 1

while(1):
    x = (n*(n+1))//2

    if x < a:
        n += 1
    elif x == a:
        break
    else:
        n -= 1
        break


print(n)