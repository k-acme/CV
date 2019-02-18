import random

li = []
for i in range(10):
    li.append(random.randint(1, 600))
    

def stretch(li):
    min_n = li[0]
    max_n = li[0]
    for i in range(len(li)):
        if li[i] < min_n:
            min_n = li[i]
        if li[i] > max_n:
            max_n = li[i]
            
    print("max: {}, min: {}".format(max_n, min_n))
    for i in range(len(li)):
        v = (li[i]-min_n)/(max_n-min_n)
        v = int(v*255)
        li[i] = v

print(li)
stretch(li)
print(li)
