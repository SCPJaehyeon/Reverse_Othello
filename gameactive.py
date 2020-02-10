import sys, os, copy
#Needed lpva, npvp
depth = 3
mini = 0 - 1
maxi = 100 + 1
#Needed lpvp, lpva
p_x = 3
p_y = 3
pass_check = 0
board = [['0' for x in range(8)] for y in range(8)]
#Needed npvp
updated_board = [['0' for x in range(8)] for y in range(8)]
lastest = (-1, -1)
turn_check = '1'
game_status = "ing"
#Needed ALL
check_x = [-1, 0, 1, -1, 1, -1, 0, 1]
check_y = [-1, -1, -1, 0, 0, 1, 1, 1]
player = '0'

def Score(board, player): #스코어 계산
    score = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == player:
                score += 1
    return score

def ChangeBoard(board_str): #네트워크 프로토콜 > 호스트 프로토콜
    l = 0
    board = [['0' for x in range(8)] for y in range(8)]
    for i in range(8):
        for j in range(8):
            if(board_str[l] == 'b'):
                board[i][j] = '1'
            elif(board_str[l] == 'w'):
                board[i][j] = '2'
            l += 1
    return board

def PassCheck(board, player): #둘수있는곳있는지 체크
    for y in range(8):
        for x in range(8):
            if Available(board, x, y, player):
                return False
    return True

def Available(board, x, y, player): #가능한 자리인지 계산
    if x < 0 or x > 7 or y < 0 or y > 7: #0부터 7까지
        return False
    if board[y][x] != '0': #땅이아니면
        return False
    (Temp, total) = Move(copy.deepcopy(board), x, y, player) #뒤집을수있는곳
    if total == 0: #뒤집을수있는 총 돌갯수
        return False
    return True

def Move(board, x, y, player): #이동 및 뒤집기
    total = 0
    board[y][x] = player
    for d in range(8): 
        taken = 0
        for i in range(8): #뒤집을 곳 체크
            changed_x = x + check_x[d] * (i + 1) #8방향
            changed_y = y + check_y[d] * (i + 1) #8방향
            if changed_x < 0 or changed_x > 7 or changed_y < 0 or changed_y > 7: #범위아니면 제외
                taken = 0
                break
            elif board[changed_y][changed_x] == player: #자기 돌이면 제외
                break
            elif board[changed_y][changed_x] == '0': #땅이면 제외
                taken = 0
                break
            else:
                taken += 1
        for i in range(taken): #뒤집기
            changed_x = x + check_x[d] * (i + 1)
            changed_y = y + check_y[d] * (i + 1)
            board[changed_y][changed_x] = player
        total += taken
    return (board, total)

def Best(board, player): #MINIMAX알고리즘위한
    maxPoint = 0
    max_x = -1
    max_y = -1
    for y in range(8):
        for x in range(8):
            if Available(board, x, y, player):
                (Temp, total) = Move(copy.deepcopy(board), x, y, player)
                point = Minimax(Temp, player, depth, True)
                if point > maxPoint:
                    maxPoint = point
                    max_x = x
                    max_y = y
    return (max_x, max_y)


def Weighted(board, player): #가중치 조정
    weight = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == player:
                if (x == 0 or x == 7) and (y == 0 or y == 7):
                    weight += 1 #끝코너
                elif (x == 0 or x == 7) or (y == 0 or y == 7):
                    weight += 3 #끝사이드
                elif (x == 1 and y == 1) or (x == 6 and y == 1) or (x == 1 and y == 6) or (x==6 and y == 6):
                    weight += 10 #끝에서 두번째 코너
                elif ((x == 1 or x == 6) and (x != 0 or x != 7)) or ((y == 1 or y == 6) and (y != 0 or y != 7)):
                    weight += 7 #끝에서 두번째 사이드
                else:
                    weight += 5 #나머지
    return weight

def Minimax(board, player, depth, maximizingPlayer): #MINIMAX알고리즘
    if depth == 0 or PassCheck(board, player):
        return Weighted(board, player)
    if maximizingPlayer:
        bestValue = mini
        for y in range(8):
            for x in range(8):
                if Available(board, x, y, player):
                    (Temp, total) = Move(copy.deepcopy(board), x, y, player)
                    v = Minimax(Temp, player, depth - 1, False)
                    bestValue = max(bestValue, v)
    else:
        bestValue = maxi
        for y in range(8):
            for x in range(8):
                if Available(board, x, y, player):
                    (Temp, total) = Move(copy.deepcopy(board), x, y, player)
                    v = Minimax(Temp, player, depth - 1, True)
                    bestValue = min(bestValue, v)
    return bestValue