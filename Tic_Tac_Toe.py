game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board():
        print("   0  1  2 ")
        # enumerate : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용.
        # 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환.  
        for count, row in enumerate(game):
                print(count, row)

x = game_board # x가 game_board() 함수가 됨.

game[0][1] = 1

x()