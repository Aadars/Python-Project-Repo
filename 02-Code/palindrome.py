def palin(s):
    s=s.replace(' ','')
    if s==s[::-1]:
        return True
    else:
        return False
print(palin('12 1'))
