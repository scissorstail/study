n, m = map(int, input().split(' '))

# print(n, m)

check_row = (n - 8) + 1
check_col = (m - 8) + 1

# print('check', check_row, check_col)

board = []
for row in range(n):
    board.append(list(input()))

result_list = []
for row_check_start in range(check_row):
    for col_check_start in range(check_col):
        # 체스판 체크
        # print('board check start', row_check_start, col_check_start)
        
        # 맨 왼쪽 위 칸이 W로 시작할 경우 체크
        changes_when_start_with_w = 0 
        for board_row in range(8):
            for board_col in range(8):
                check_value = None
                if(board_row % 2 == 0):
                    check_value = 'W' if board_col % 2 == 0 else 'B'
                else:
                    check_value = 'B' if board_col % 2 == 0 else 'W'

                if(check_value != board[row_check_start + board_row][col_check_start + board_col]):
                    changes_when_start_with_w += 1

                # print(board_row, board_col, check_value, board[board_row][board_col])
        # print(changes_when_start_with_w)
        
        # 맨 왼쪽 위 칸이 B로 시작할 경우 체크
        changes_when_start_with_b = 0 
        for board_row in range(8):
            for board_col in range(8):
                check_value = None
                if(board_row % 2 == 0):
                    check_value = 'B' if board_col % 2 == 0 else 'W'
                else:
                    check_value = 'W' if board_col % 2 == 0 else 'B'

                if(check_value != board[row_check_start + board_row][col_check_start + board_col]):
                    changes_when_start_with_b += 1

                # print(board_row, board_col, check_value, board[board_row][board_col])
        # print(changes_when_start_with_b)

        result_list.append(min(changes_when_start_with_w, changes_when_start_with_b))

print(min(result_list))
