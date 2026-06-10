s="abcdef"
l=len(s)
dic = {}
sset = set()
llist= []
ttup = ()
print(type(ttup))
for i in range(l):
    dic[i]=s[i]
    sset.add(s[i])
    llist.append(s[i])
    ttup += (s[i],)
for i in range(l):
    dic[i]=s[i]
    sset.add(s[i])
    llist.append(s[i])
    ttup += (s[i],)
print(dic)
print(sset)
print(llist)
print(ttup)