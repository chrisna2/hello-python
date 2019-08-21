'''
★ 연산자
==
<
<=
>
>=
!=

★ and , or
java에서     파이썬에서
&&       ==> and
||       ==> or
'''
post = {
    "title":"good day commado",
    "content":"considerate done.",
    "tag":["yamato","battle","crusier","operation"],
    "price":[
        {
            "singer":"iu",
            "wage":200000
        },
        {
            "singer":"suzi",
            "wage":10000
        }
    ]
}

'''
파이썬 if문
in : java의 contian() 메서드임 
not in : 위에 거에 반대
'''
if 10000 >= post.get("price")[1]["wage"] or 10000 >= post.get("price")[0]["wage"]:
    print("섭외 가능")
else:
    print("예산 초과")


'''
파이썬 for문 
☆ for문은 원래 어렵다. 이거 못해서 프로그램 그만둔 사람 졸라게 많음
점점 for문을 없에려는게 방향성임 : 함수형 프로그래밍, 선언적 프로그램밍 등등..

근데 상식적으로 이게 어려우면 프로그램 하는 사람이 아니지...
'''
favorite_colors = ['red', 'blue', 'yellow', 'white', 'black']

result_list1 = []

# 영어적 관점 : favorite_colors 아이템이 color에 각각 담김
for color in favorite_colors:
    if len(color) >= 5:
        result_list1.append(color)

print(result_list1)
'''
이거 어렵다고 못한데 프로그래밍 아이고...
일반적인 숫자형 for 문이란다. 아무튼 되게 잘 넘긴다.
'''
result_list2 = []
for i in range(10):
    result_list2.append(i)
    
print(result_list2)

'''
강사 왈
2중 for문, 3중 for문은 살아가는데 아주 도움이 되지 않는다.
필요없다.

2차원 데이터를 표현하는 자료구조가 없다.

pandas 라이브러리
-> 2차원 배열의 데이터를 직관적으로 표현하는 파이썬 라이브러리

파이썬에서 클래스 필요없데요.
'''















