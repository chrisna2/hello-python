'''
★함수와 모듈
함수 -> 코드 재사용
'''
# 대신 들여쓰기가 중요함 TAB
def add(a, b):
    return a + b
"""
C계열 언어 : 중괄호 
function add(a, b){
    return a + b;
}
"""
print(add(10,20))

"""
[파이썬의 차별화된 함수기능]
- 파라미터를 받는데 기본 값을 설정이 가능하다.
    -장점 1] 파라미터 타입을 간접적으로 선언한다.
    -장점 2] 파라미터 키워드에 맞춰서 선택적으로 인자 값을 넘겨 줄수 있다.
            -> "키워드 파라미터"라고 한다.
            
※ 파이썬의 문화            
    파라미터 기본 값을 설정하는게 국룰임
"""
def bmi(height=170, weight=60, age=20):
    return height + weight * age

print(bmi(180,75,40))
print(bmi(age=40))

'''
- 파이썬 리턴값이 다중 값을 리턴할 수도 있다!
'''

def bmi_info(height=170, weight=60, age=20):
    return height, weight, age

#[사실은] 위에 것 처럼 리턴 값을 설정 할 경우 3개의 데이터를 리턴하는게 아니라 튜플의 형태의 데이터가 리턴한 것임
# 문법 : 튜플의 괄호는 "()"는 생략이 가능한다. height, weight, age =사실은=> (height, weight, age) 이거였음
print(bmi_info(180,75,40))


'''
파이썬은 순수 객체 지향 언어
-> 모든 함수는 객체다.

내장 함수(builtin function) : 15개 

'''
# print 여러개의 데이터를 나열할 경우 기본값으로 sep = " "이 들어 간다.
'''
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
print("Good","day","commader")
print("Good","day","commader", end="★")
print("Good","day","commader", sep="^_^")