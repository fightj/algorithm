def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    current_time = pos.split(':')
    op_start = op_start.split(':')
    op_end = op_end.split(':')
    video_len = video_len.split(':')
    
    op_start_time =int(op_start[0])*60 + int(op_start[1])
    op_end_time = int(op_end[0])*60 + int(op_end[1])
    video_len_time = int(video_len[0])*60 + int(video_len[1])
    current_int_time = int(current_time[0])*60 + int(current_time[1])
    
    if op_start_time <= current_int_time <= op_end_time:
                current_int_time = op_end_time
            
    for com in commands:
        if com == 'next':
            current_int_time += 10
            if current_int_time >= video_len_time:
                current_int_time = video_len_time
            if op_start_time <= current_int_time <= op_end_time:
                current_int_time = op_end_time
        elif com == 'prev':
            current_int_time -= 10
            if current_int_time < 0:
                current_int_time = 0
            if op_start_time <= current_int_time <= op_end_time:
                current_int_time = op_end_time
                
    result_time = ''
    mi = str(current_int_time // 60)
    if len(mi) < 2:
        mi = '0' + mi
    sec = str(current_int_time % 60)
    if len(sec) < 2:
        sec = '0' + sec
        
    answer = mi + ':' + sec
    
    
    return answer

# ------------------------------------------
# 단순한 문자열 파싱문제. 발생할 수 있는 모든 예외를 처리해줘야함.
# .split() 활용.