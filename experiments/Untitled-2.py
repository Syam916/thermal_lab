def beauty(n,m,s,x,y):
  edges={}
  for i in range(m):
    if edges.get(x[i]):
      edges[x[i]]+=[y[i]]
    else: edges[x[i]]=[y[i]]

  
  def maxi(lis):
    if lis==[]: return 0
    k={}
    ma=0
    for i in lis:
      kk=s[i-1]
      if k.get(kk) is None:
        k[kk]=1
      else: k[kk]+=1
      if k[kk]>ma: ma=k[kk]
    return ma
  
  
  def path(node,done):
    if node in done: raise Exception
    if edges.get(node) is None: return [done+[node]]
    temp=[]
    for i in edges[node]:
      temp+=path(i,done+[node])
    return temp
  
  ma=0
  try:
    for i in range(1,n+1):
      for j in path(i,[]):
        mm=maxi(j)
        if mm>ma: ma=mm
    return ma
  except Exception:
    return -1

n=int(input('enter n'))
m=int(input())
s=input()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
print(beauty(n,m,s,x,y))