add = 3+1
# 파이썬은 세미콜론을 안붙임
print(add)
my_name = '나현기'
print(my_name+" 파이썬 교육중...")


'''
★ 기본 파이썬 데이터 구조 (변수 데이터 타입) ★ 

1. number 숫자
    - 정수(cpu 연산) :1
    - 실수(gpu 연산) :2
2. string 문자
    - 무조건 유니코드(UTF-8) :3
3. boolean 논리 :4
4. collection 타입 :5

=> 이 5개가 전부이다.

★ 덕후들이 만든 언어 ★
변수를 만들때 두 단어 이상이면 언더바 '_' 사용해 변수를 만든다.
이게 파이썬 스타일임, 카멜 케이스는 사용 안해줘야 파이썬 국룰
변수명 설정이 프로그램의 반이상임
이스케이프 문자 확인 

★ 변수 선언시 타입을 따로 적지는 않는다. ★
데이터의 형태로 추론을 함. 처음에는 이게 좋아보였으나... 
소스 코드 자체가 문서로 여겨 지면서 가독성이 매우 떨어지게 됨
규모가 커지면 유지보수가 어려워짐. 파이썬의 단점이 되어 버림

'''

my_int = 29
my_float = 3.141592
my_str = "hello world!"
my_bool = True

print(my_int)
print(type(my_int))
print(my_float)
print(type(my_float))
print(my_str)
print(type(my_str))
print(my_bool)
print(type(my_bool))

'''
파이썬의 연산
'''
#덧셈
print(3+9)
#뺄셈
print(10-2)
#곱셈
print(3*8)
#나눗셈
print(9/3)
#제곱
print(2**10)

'''
변수
메모리 공간 주소 확인 id()
'''
x = 1000
print(id(x))

x = "hello world!"
print(id(x))
# 여기서 x는 위에 x와는 다르다. 자바에서는 안되는 행위, 새롭게 변수를 만든것임...


'''
파이썬 문자열 조작법

*자르고(slicing) 
*붙이고(join)

파이썬의 문자열은 모든 것을 인덱싱 처리 한다.

+인덱스 일 경우 : 앞에서 0 부터 시작
-인덱스 일 경우 : 끝에서 -1 부터 시작

'''
test_word = "hello world!"

print(test_word[0])
print(test_word[-1])
print(test_word[11])
# print(test_word[12])
# IndexError: string index out of range

print(test_word[0:5])
print(test_word[6:11])
print(test_word[6:-1])

# 문자열 길이 : len()
print(len(test_word))

'''
파이썬은 모든 것이 객체 이다.
모든 것이 객체 이기 때문에 함수란 존재 하지 않고 메소드만 있다.

다만 문법적 허용이 존재한다.
★ 파이썬의 내장 함수 : 대략 50개 정도 + 10개가 주력 
-> 원래는 .method() 임
'''

# 문자열 나누기 : .split()
print(test_word.split(" "))
print(test_word.split(" ")[0])

# 대소문자 변환 , upper, lower
print(test_word.upper())

# 문자열로 결합 : join()
test_list = ["he","is","iron","man"]


'''
파이썬 if문
in : java의 contian() 메서드임 
not in : 위에 거에 반대
'''
if 'hello' in test_word:
    print("hello 있음")
else:
    print("hello 없음")

'''
파이썬이 쉽다는 말
-> 영어를 사용하는 사람들에게 쉽게 다가온다는 말
-> 한국인에게는 어렵다.
'''


