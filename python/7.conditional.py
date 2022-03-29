print(1)
if True:
    print(2) #들여쓰기로 구문을 구분하도록 설정됨. 따라서 같은 구문에 속해 있다면 동일한 위치에 띄어쓰기 혹은 들여쓰기 간격이 되어있어야됨.
    print(3)
print(4)

if False:
    print(2)
    print(3)
print(4)

print(1)
if True:
    print(2.1)
    print(3.1)
else:
    print(2.2)
    print(3.3)
print(4)

print(1)
if False:
    print(2.1)
    print(3.1)
else:
    print(2.2)
    print(3.3)
print(4)