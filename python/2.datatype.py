print(1)
print(1.1)
print(1+1)
print(2-1)
print(2*2)
print(6/2)
print(pow(4,3))
import random
print(random.random())

# String
print('Hello')
print("Hello")
print('''
    Hello
    World
''')
print("""
    Hello
    World
""")
print(len('Hello'))
print('Hello, World!'.replace('World', 'Python'))
s = 'Hello, World!'
s = s.replace('World!', 'Python')

# List -> 서로 연관된 데이터를 모아 그룹핑하여 이름을 붙인 것. 정리정돈가능, 리스트와 관련된 수많은 연산들을 이용해 계산을 할 수가 있게 함.
member = ['egoing', 'duru', 'taeho'] 
print(member[0])
print(len(member)) #list 의 값이 몇개인지 확인할 수 있는 코드

import random #제비뽑기 하고 싶을 때(예)
print(random.choice(member)) # choice 함수 -> 실행할 때마다 랜덤하게 데이터를 뽑아옴.

score = [100,200,300]
print(sum(score)) #데이터를 합치고 싶을 때