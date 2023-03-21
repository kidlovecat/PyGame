def sum(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = sorted(a,key=sum)
    print(*b,sep=" ")