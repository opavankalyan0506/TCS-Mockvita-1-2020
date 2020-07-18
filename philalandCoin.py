T = int(input())
for i in range(T):
  N = int(input())
  C = 0
  while N != 0:
    C += 1
    N >>= 1
  if i == T-1:
    print(C,end="")
  else:
    print(C)