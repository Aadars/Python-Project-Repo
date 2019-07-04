def is_pang(s):
    a=s.split()
    c=set(a)
    d=list(c)
    m=(' '.join(d))
    if m==a:
        return True
print(is_pang('the quick brown fox in this list again again'))
