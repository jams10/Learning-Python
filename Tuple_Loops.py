# Tuple 
# 불변한 순서가 있는 객체의 집합. 한 번 생성되면 값을 변경할 수 없음.
# 다양한 타입이 함께 포함될 수 있음.
programming_languages = ("Python", "Java", "C#", "C++")

various_elements = (1, 0.5, "hi", 'a')

one_element = ('a')
# 쉼표(,)를 추가해 줌으로써 원소가 하나만 있어도 튜플로 유지 가능.
one_element_2 = ('a',)

# 변수 타입 출력
print(type(programming_languages))
print(type(various_elements))
print(type(one_element))
print(type(one_element_2))

print(programming_languages)

# for문 통한 출력
for language in programming_languages:
    print(language)

# 튜플 연산

# 1. 추가
t = ("하나", "둘")
t += (3, 1.5)

print(t)

# 2. 반복
print(t * 2)

# 3. 튜플 안에 튜플
tt = ((1,2), ('a',3.5), ("헤헤", "히히"))
print(tt[1])

# 4. 원소 존재 유무 체크
print(("헤헤", "히히") in tt)

# 5. 함수 리턴 값
# 튜플을 이용해 여러 개의 값 한번에 리턴 가능

def minmax(items):
    return min(items), max(items)

ttt = ((1,2,4,10,6,8))

print(minmax(ttt))
