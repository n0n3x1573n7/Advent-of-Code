from string import digits

with open('./day1/input.txt') as f:
    ans=[]
    for line in f.read().strip().split('\n'):
        s=''
        for i in line:
            if i in digits:
                s+=i
        ans.append(int(s[0]+s[-1]))

print(sum(ans))
