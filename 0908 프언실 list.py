a = []
type(a)
a[0]
a = [4, 3, 2, 1]
a[0]
a = list(range(101))
a[2:7] 
a[[1,6,9]]

a = [1, 2, 3]
del a[1]
a
a = list(range(101))
a
del a[0:10]
a

#리스트 요소 제거 del remove pop

b = list(range(5))
b
a+b

# append a에 적용할 수 있는 함수
a.append() 
a.append("a")
a.append([0,3,5])
a 
# 리스트 그대로 더하기
len(a)
a[-1]
type (a[-1])
# a[-1]이 리스트이기 때문에 
a[-1][1]

#extend 리스트만을 받을 수 있음
a.extend([0,3,5])
a 