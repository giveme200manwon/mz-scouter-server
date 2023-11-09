import _jpype
from konlpy.tag import Okt
from konlpy.tag import Kkma

kkma = Kkma()
okt = Okt()
mz_end_words = ["네", "을걸", "을래", "ㄹ래", "ㄹ걸", "을게", "ㄹ게", "을래", "ㄹ래", "어", "아", "대"]
not_mz_end_words = ["읍니다", "군", "는군", "으마", "마", "구나", "는구나", "으냐", "냐", "느냐", "으랴", "려무나", "소서", "지", "단다", "느냔다", "란다", "잔다", '나']
end_words = []
mz_end_words_cnt = 0
not_mz_end_words_cnt = 0
short_ans_cnt = 0

sent = input("문장을 입력하시오(종결어미 분석): ")
print(kkma.pos(sent,flatten=False))

for i in kkma.pos(sent,flatten=False):
    for j in i:
        if j[0] == 'ㅁ' or j[0] == '음':
            short_ans_cnt += 1
        if j[1][0:2] == 'EF':
            for k in mz_end_words:
                if j[0] == k:
                    mz_end_words_cnt += 1
            for k in not_mz_end_words:
                if j[0] == k:
                    not_mz_end_words_cnt += 1


print(mz_end_words_cnt, not_mz_end_words_cnt, short_ans_cnt)