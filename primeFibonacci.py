def primes(n):
    l = [True for _ in range(n+1)]
    p = []
    i = 2
    while i < n:
        if l[i] is True:
            for j in range(2*i,n+1,i):
                l[j] = False
        i += 1
    for i in range(n+1):
        if i > 1 and l[i] is True:
            p.append(i)
    return p


n1,n2 = list(map(int, input().split()))

m = primes(n2)
p = []
for i in m:
    if i >= n1:
        p.append(i)

q = []
for i in range(len(p)):
    for j in range(len(p)):
        if i != j:
            q.append(int(str(p[i]) + str(p[j])))
d = {}
q = list(set(q))

r = []
k = primes(max(q))
for i in q:
    if i in k:
        r.append(i)


a = min(r)
b = max(r)
for i in range(len(r)-2):
    c = a + b
    a = b
    b = c
print(c)
