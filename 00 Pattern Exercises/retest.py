s="abcdef"
l=len(s)
dic = {}
sset = set()
llist= []
ttup = ()
print(type(ttup))
for i in range(l):
    print(i,end=" ")
    dic[i]=s[i]
    sset.add(s[i])
    llist.append(s[i])
    ttup += (s[i],)
print()
print("dict:  ",dic)
print("set:   ",sset)
print("list:  ",llist)
print("tuple: ",ttup)
for i in range(5,0,-1):
    print(i,end=" ")
print()
