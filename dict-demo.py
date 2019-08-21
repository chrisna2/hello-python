'''
★ Dictionary : java 에서 map 같은 녀석
    -> key, value 타입으로 설정
    -> 순서가 필요 없다.
    -> 반드시 key 는 유니크 속성으로 설정
    (자료구조 관점에서 dictionary 형이 더 빠르다.)
'''

# 생성법
slang = {'a':'assassin',
         'b':'badass',
         'c':'cockpick',
         'd':'deadly_gone'}

print(slang)

# 조회
print(slang.get('a'))
print(slang['d'])

# 수정 update
slang['a'] = 'akira'

#print(slang['e']) #에러 발생함

# 삽입 insert
slang['e'] = 'electro_shock' # upsert : 있으면 update , 없으면 insert
print(slang)

'''
데이터 타입을 정의 할 때 많이 사용한다고 함.

공교롭게도
파이썬의 dictonary 타입과
JSON의 구조 똑같다.
'''
post = {
    "title":"good day commado",
    "content":"considerate done.",
    "tag":["yamato","battle","crusier","operation"],
    "replies":[
        {
            "author":"iu",
            "content":"good"
        },
        {
            "author":"suzi",
            "content":"bad"
        }
    ]
}

# 조회 v1
print(post)
print(post['replies'][0]['author'])
print(post['tag'][3])
# 단점 : 철자가 틀리면 에러가 발생한다.

# 조회 v2
#print(post['repli'])    # 에러 발생! 하위 스크립트 실행 실패
#print(post['tag'][3])
print(post.get('repl'))  # NONE : java 에서 null 과 같음 -> 에러가 발생하지 않음, 권장 되는 조회 방식
print(post['tag'][3])