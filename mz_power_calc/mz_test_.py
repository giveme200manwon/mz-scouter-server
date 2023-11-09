# -*- coding: cp949 -*-
#자음이나 모음만 있는 경우
def count_single_word(s):
    single_word_cnt = 0
    for word in s:
        if word >= 'ㄱ' and word <= 'ㅎ':
            single_word_cnt += 1
        if word >= 'ㅏ' and word <= 'ㅡ':
            single_word_cnt += 1
    return single_word_cnt

#ㅋ,ㅎ,ㅠ개수 세기
def count_z_b (s):
    z_cnt, b_cnt = 0,0
    for word in s:
        if word == "ㅋ":
            z_cnt += 1
        elif word == "ㅠ":
            b_cnt += 1
            
    return [z_cnt, b_cnt]

#ㅋ,ㅎ,ㅠ 개수에 따른 mz력 반환
def mz_point_count (cnt_list):
    z_cnt,b_cnt = cnt_list
    mz_power_z = [50,70,10,50,60,70,80,100]
    if b_cnt:
        return 100
    elif z_cnt:
        return mz_power_z[z_cnt]
    else:
        return 0

sentence = "안녕 ㅋㅋㅋ ㅎㅎ ㅠ"
print(count_z_b(sentence))
print(mz_point_count(count_z_b(sentence)),"%")
print("자음, 모음 개수 :",count_single_word(sentence))



