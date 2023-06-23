def palindrom():
    x = str(input())
    a = x[::-1]
    if x == a:
        print('True')
    else:
        print('False')
palindrom()