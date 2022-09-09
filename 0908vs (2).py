a = "Life is too short, You need Python"
b= a[0] + a[1] + a[2] + a[3]
b
a[0:5]
a[5:7]
a[12:17]
a[19:]
a[:]
a[19:-7]
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather
a = "20010331Rainy"
print(a)
year = a[:4]
day = a[4:8]
weather = a[8:13]
year
day
weather
len(a)
a[:3]
a[:-5]

a = "Pithon"
len(a)
a[:1] + "y" + a[2:]

a = "Life is too short, You need Python"

a[1 : 10 : 2]
a[-1 : -5 : -1] # 문자열의 순서 뒤집기
a[ : : -1] #끝에서 처음까지 거꾸로 출력
# 숫자가 증가하는 방향으로 구성 , 정렬 시 숫자가 감소하는 방향 원할 때 사용하기 
# 
a[ : : 1] #처음부터 끝까지 하나씩 증가
a[ : : -1] # 끝에서 처음으로 하나씩 출력

"I eat {0} apples". format(3)
"I eat {0} apples".format('five')
number = 3
"I eat {0} apples" . format(number)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days." . format(number , day)

"I ate {0} apples" . format(3)

# 1을 001로 표현하기 d
# 3.000 3.140       f

y = 3.42134234
"{0:0.4f}".format(y) # 문자열을 표현할 때 소수점 네자리까지 표현 
# 중괄호에서 문자열을 받아오는 인덱스 : 받아온 값을 어떻게 표현할지 

"{0: 03d}". format (7) # 앞에 0을 붙이고 세자리로 표현하기
"{0: 03d}". format (10)

# count 문자 개수 세기
a = "hobby"
a.count('b')

# find 위치 알려주기
a = "Python is the best choice"
a.find('b')
a.find('k')

# index 위치 알려주기
 a = "Life is too short"
 a.index('t')
 a.index('k')

# join 문자열 삽입
",".join('abcd')

# upper 소문자를 대문자로 바꾸기 <-> lower
a = "hi"
a. upper ()

# strip 공백 지우기 lstrip 왼쪽 공백 rstrip 오른쪽 공백

# replace 문자열 바꾸기 replace (바귀게 될 문자열, 바꿀 문자열)\
a = "Life is too short"
a.replace("Life", "Your leg")

# split 문자열 나누기
a = "Life is too short"
a.split()

b = "a\tb\tc\td"
print(b)
b.split('\t')
b.split(' ')






