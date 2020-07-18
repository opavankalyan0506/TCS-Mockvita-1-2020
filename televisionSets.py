n = int(input())
p,q = list(map(int, input().split()))
t = int(input())

d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
s = 0
l = [0]*(n+1)
for i in range(1,13):
    for j in range(1, d[i]+1):
        x = ((6-i)**2) + abs(j-15)
        if x > n:
            x = n
        for k in range(n+1):
            if x <= (n-k):
                l[k] += (x*q)
            else:
                l[k] += ((n-k)*q)
                l[k] += ((x-n+k)*p)
res = n
for i in range(n+1):
  if l[i] >= t:
    res = i
    break
print(res,end="")
