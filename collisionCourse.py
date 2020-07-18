def fun(n):
  return n*(n+1)//2

n = int(input())
l = []
d = {}

for _ in range(n):
    x,y,s = list(map(int, input().split()))
    r = int(((x*x + y*y)**0.5)*100000/s)
    l.append(r)

for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

s = 0
for i in d.keys():
  g = d[i]
  s += fun(g-1)
print(s)
