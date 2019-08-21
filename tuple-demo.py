'''
★ 튜플 (tuple)
-튜플은 더 적은 공간을 사용한다
-실수로 튜플의 항목이 손상될 염려가 없다
-튜플은 딕셔너리키로 사용할수 있다.
-네임드 튜플은 객체의 단순한 대안이 될수 있다.
-함수의 파라미터들은 튜플로 전달된더.
'''

empty_tuple = ()

# 정의할 때에는 괄호 안붙임
color = 'red','green','yellow','blue'

# 여러 변수에 값을 할당가능
a, b, c, d = color
print(a)
print(b)
print(c)
print(d)


# 리스트를 튜플로 전환가능
favorite_color = ['red', 'blue', 'yellow', 'white', 'black']
print(tuple(favorite_color))