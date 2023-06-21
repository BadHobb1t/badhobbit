'''
chet = [] 
nechet = []
for i in range(10): 
    x = int(input()) 
    if x % 2 == 0: 
        chet.append(x) 
    else: 
        nechet.append(x) 
print(f"{chet} \n{nechet}") 
'''
a = (5, 3, 2, 1, 4) 
print(tuple(sorted(a)))