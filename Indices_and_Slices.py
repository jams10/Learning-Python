l = [1,2,3,4,5]

# 둘은 같은 인덱스를 가리킴.
print(l[4])
print(l[-1])

print(l[0:3]) # [a:b] 인덱스 a부터 b-1 까지 slice 출력
print(l[2:]) # [a:] 인덱스 a부터 끝까지 출력

l[0] = 123

print(l)