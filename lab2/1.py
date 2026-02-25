from itertools import*
p=product('еиймотф',repeat=5)
k=0
for x in p:
    s=''.join(x)
    if s.count('й')<=1 and 'ий'not in s and 'йи'not in s and s[0]!='й' and s[4]!='й':
        k+=1
print(k)    
