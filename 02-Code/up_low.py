def string(s):
    
    u=0
    l=0
    for i in s:
        if i==i.upper() and i!=' ':
            u=u+1
        elif i==i.lower() and i!=' ':
            l=l+1
        else:
            pass
     print('No. of Upper case characters : ',u)
     print('No. of Lower case Characters : ',l)
string('I am the Boy in Village')
