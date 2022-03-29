members = ['utaha', 'duru']
for member in members:   #for ~ in ~ 문
    print('member',member)

members2 = [
    ['utaha', 'tokyo', 'writer'],
    ['eriri', 'chiba', 'illustrater']
]
print(members2[0][0])
for member in members2:
    print(member[0], member[1])

utaha1 = ['utaha', 'tokyo', 'writer']# 각각 성격이 다른 element. 이럴 경우엔 List를 사용하지 않음.
utaha2 = {'name': 'utaha', 'city': 'tokyo', 'job': 'writer'} #dictionary, 사전형(javascript의 객체와 동일한 기능)
print(utaha2['city'])
for name in utaha2:
    print(utaha2[name])

member3 = [
    {'name': 'utaha', 'city': 'tokyo', 'job': 'writer'},
    {'name': 'eriri', 'city': 'chiba', 'job': 'illustrater'}
]
for member in member3:
    print(member)
    print(member['name'])