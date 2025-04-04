def merge(a,b):
    for i in b.keys():
       if i in a:
           a[i]=[a[i],b[i]]
       else:
            a[i]=b[i]
    return a

a={"name":"surya","roll":25,"tech":"python"}
b={"name":"vamsi","id":50,"tech":"java"}
print(merge(a,b))