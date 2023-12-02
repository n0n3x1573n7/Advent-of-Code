from string import digits

stringrepr = 'zero, one, two, three, four, five, six, seven, eight, nine'.split(', ')
digitrepr = digits

anyrepr = {}
for i, s, d in zip(range(10), stringrepr, digitrepr):
    anyrepr[s] = i
    anyrepr[d] = i

print(anyrepr)

ans=[]
with open('./day1/input.txt') as f:
    for line in f.read().strip().split('\n'):
        location_front = {}
        location_back = {}
        for i in anyrepr:
            location_front[i] = line.find(i)
            location_back[i] = line[::-1].find(i[::-1])
        
        frontidx, frontval = len(line)+1, ''
        for key, val in location_front.items():
            if val==-1 or val>frontidx:
                continue
            frontidx, frontval = val, key
        
        backidx, backval = len(line)+1, ''
        for key, val in location_back.items():
            if val==-1 or val>backidx:
                continue
            backidx, backval = val, key

        ans.append(10*anyrepr[frontval]+anyrepr[backval])
print(sum(ans))
        
