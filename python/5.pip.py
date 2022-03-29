import pandas # 이 프로그램(라이브러리)을 사용하려고 가져오는 것.(표시)
house = pandas.read_csv('boston.csv')
print(house)
print(house.head(1)) #1건만 보여줌.
print(house.describe()) # column 별로 데이터를 보여주는 것.