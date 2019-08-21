'''
★ Collection
여러 개의 데이터를 다루기
CRUD (Create, Read, Update, Delete)
위한 자료 구조

- List : 배엻,자바에서 list, array
    -> 순서 , 인덱스를 부여 해서 순서대로 나열
'''

# [1] list
# 5개의 아이템으로 이루어진 리스트 작성
favorite_color = ['red', 'blue', 'yellow', 'white', 'black']
print(favorite_color)

# 아이템 추가 .append() : 원본 자체가 변경됨
favorite_color.append('gold')
print(favorite_color)

# 수정... 자체는 없다.... 아이템을 제거하고 다시 입력해야 됨
# insert 지정된 위치에 특정 아이템 추가 가능.
favorite_color.insert(2, 'silver')
print(favorite_color)

# 제거 remove
favorite_color.remove("black")
print(favorite_color)

# 인덱스 번호를 기준으로 해당 데이터 삭제
del(favorite_color[3])
print(favorite_color)

# 조회 : string 과 동일한 문법 사용
print(favorite_color[1])
print(favorite_color[2:4])

# 삽입 확장 : append 의 확장판..
favorite_color.extend(["purple","green"])
print(favorite_color)

word_list = ["hello","world","who","are","U?"]
number_list = [1,2,3,4]
mixed_list = [1,"world",30.1245,"are","U?"]



