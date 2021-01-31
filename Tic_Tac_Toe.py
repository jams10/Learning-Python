game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(game_map, player = 0, row = 0, column = 0, just_display = False):
        try:    
                print("   0  1  2 ")
                if not just_display:
                        game_map[row][column] = player
                # enumerate : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용.
                # 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환.  
                for count, row in enumerate(game_map):
                        print(count, row)
        
                return game_map
        except IndexError as e:
                print("Error : make sure you input row/column as 0 1 or 2?", e)
        except Exception as e: # General Exception
                print("Something went very wrong!", e)

b = game_board # x가 game_board() 함수가 됨.

game = game_board(game, just_display = True)
game = game_board(game_board, player = 1, row = 3, column = 0)
