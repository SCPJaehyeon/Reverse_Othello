

def gen_accept_msg(turn, token, board):
    return 'accept\n' \
        'color:{color}\n' \
        'token:{token}\n' \
        'board:{board}'.format(color=turn, token=token, board=board)
    
def gen_turn_msg(available_list):
    return 'turn\n' \
        'available:{available}'.format(available=' '.join(available_list))

def gen_move_msg(move, token):
    return 'move\n' \
        'move:{move}\n' \
        'token:{token}'.format(move=move, token=token)

def gen_update_msg(board, move):
    return 'update\n' \
        'board:{board}\n' \
        'move:{move}'.format(board=board, move=move)

def gen_end_msg(status, score, board):
    return 'end\n' \
        'status:{status}\n' \
        'score:{score}\n' \
        'board:{board}'.format(status=status, score=score, board=board)

def parse_msg(msg:str):
    lines = msg.split('\n')
    code = lines[0]
    data = dict()

    for i in range(1, len(lines)):
        key, value = lines[i].split(':')
        data[key] = value

    return code, data