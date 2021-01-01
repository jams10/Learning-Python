game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   a  b  c ")
# enumerate : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용.
# 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환.  
for count, row in enumerate(game):
    print(count, row)