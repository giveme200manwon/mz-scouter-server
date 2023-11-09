import _jpype
from konlpy.tag import Okt
from konlpy.tag import Kkma
kkma = Kkma()
okt = Okt()

bad_sum = 6084
no_bad_sum = 5021

mz_sum = 764
no_mz_sum = 526

mz_end_words_cnt = 0
not_mz_end_words_cnt = 0

short_ans_cnt = 0
mz_end_words = ["네", "을걸", "을래", "ㄹ래", "ㄹ걸", "을게", "ㄹ게", "을래", "ㄹ래", "어", "아", "대", "은걸요"]
not_mz_end_words = ["죠","ㄴ가","는가", "읍니다", "군", "군요", "는군", "으마", "마", "구나", "는구나", "으냐", "냐", "느냐", "으랴", "려무나", "소서", "지", "단다", "느냔다", "란다", "잔다", "나", "ㅂ시다", "ㄴ걸", "는걸", "은걸","네"]
end_words = []

#[단어, yock, not_yock 순]
bad_words = [['새끼', 307, 6],
            ['존나', 183, 13],
            ['병신', 153, 1],
            ['개', 120, 40],
            ['좆', 110, 2],
            ['느금', 111, 1],
            ['느금마', 108, 1],
            ['씨발', 93, 1],
            ['년', 92, 13],
            ['애미', 84, 49],
            ['지랄', 92, 1],
            ['니애미', 88, 1],
            ["씨발롬",100,1],
            #['임', 95, 110],
            ['놈', 78, 31],
            #['돈', 68, 89],
            ['사람', 68, 126],
            ['그냥', 71, 84],
            #['더', 74, 88],
            ['뭐', 76, 92],
            ['시발', 77, 1],
            #['니', 74, 50],
            ['왜', 73, 71],
            ['생각', 61, 93],
            #['소리', 65, 23],
            ['때', 63, 112],
            #['내', 63, 70],
            #['용접', 45, 46],
            #['이', 61, 68],
            #['너', 58, 40],
            ['것', 48, 74],
            ['한국', 48, 44],
            #['여자', 54, 36],
            ['게이', 51, 11],
            ['일베', 50, 32],
            #['함', 47, 66],
            #['나', 54, 77],
            ['저', 55, 61],
            ['좀', 50, 68],
            ['홍어', 31, 3],
            #['일', 40, 45],
            #['보고', 41, 33],
            ['나라', 37, 41],
            ['틀', 42, 3],
            #['또', 38, 24],
            ['그', 45, 77],
            ['정도', 35, 59],
            ['공부', 28, 36],
            ['대가리', 38, 3],
            ['쓰레기', 37, 7],
            ['일본', 27, 49],
            #['남자', 31, 26],
            #['알', 37, 27],
            ['처', 33, 6],
            ['글', 35, 30],
            ['하나', 33, 32],
            ['안', 31, 57],
            ['인간', 29, 15],
            ['지금', 32, 58],
            ['게', 32, 24],
            ['남', 31, 21],
            ['짱깨', 28, 1],
            ['욕', 30, 18],
            ['미국', 25, 21],
            ['자기', 27, 23],
            ['수준', 30, 10],
            ['결혼', 22, 17],
            ['보지', 26, 5],
            ['노가다', 22, 6],
            #['못', 27, 27],
            ['걸', 29, 38],
            #['해', 27, 20],
            ['머리', 24, 16],
            ['집', 25, 39],
            ['인생', 25, 14],
            ['개새끼', 27, 2],
            #['건', 26, 23],
            #['수', 25, 42],
            #['이해', 25, 17],
            ['난', 28, 44],
            ['때문', 23, 27],
            ['중국', 19, 29],
            ['살', 21, 32],
            ['거리', 22, 11],
            ['데', 24, 26],
            ['그게', 23, 24],
            ['기술', 19, 20],
            #['저런', 23, 15],
            ['다음', 24, 23],
            ['재앙', 21, 2],
            ['빨', 20, 6],
            ['거지', 21, 20],
            ['응', 10, 100],
            #['그거', 23, 20],
            ['똥', 20, 3],
            ['충', 19, 9],
            ['직업', 18, 16],
            ['위장', 5, 1],
            #['문제', 23, 24],
            ['무슨', 22, 20],
            ['일게이', 21, 3],
            ['위', 13, 24],
            #['비', 18, 20],
            ['전', 22, 21],
            ['팩트', 19, 14],
            ['빨갱이', 20, 0],
            ['명', 17, 20],
            ['조선', 12, 11],
            ['댓글', 20, 17],
            ['노', 19, 20],
            ['자체', 18, 20],
            ['이기', 20, 22],
            ['요즘', 20, 22],
            ['곳', 19, 28],
            ['몸', 18, 5],
            #['사회', 17, 11],
            ['문재인', 16, 6],
            #['정신', 19, 9],
            ['질', 20, 10],
            ['한번', 17, 25],
            #['응', 18, 10],
            ['나이', 19, 6],
            ['좌파', 17, 5],
            ['이제', 19, 31],
            ['머', 17, 10],
            #['짓', 17, 11],
            ['보수', 13, 9],
            ['키', 16, 15],
            #['해도', 17, 14],
            ['친구', 15, 21],
            #['기', 18, 14],
            ['주작', 12, 5],
            ['앞', 14, 16],
            #['전라도', 17, 17],
            #['이노', 17, 12],
            #['자', 16, 13],
            ['이상', 17, 23],
            ['뭘', 15, 17],
            #['강사', 14, 11],
            ['사진', 12, 23],
            ['자살', 14, 6],
            ['녀', 13, 4],
            #['끼리', 14, 13],
            ['벌레', 16, 2],
            ['사실', 15, 28],
            ['김치', 14, 5],
            #['북한', 14, 3],
            ['누가', 14, 21],
            ['쟤', 14, 16],
            #['도', 16, 16],
            ['바로', 15, 20]]

mz_words = [["ㄹㅇㅋㅋ", 10, 1],
         ["ㄴㅇㄱ", 10, 1],
         ["돔황챠", 10, 1],
         ["가즈아", 10, 1],
         ["시치", 10, 1],
         ["아오", 10, 1],
         ["게이", 10, 1],
         ["틀딱", 10, 1],
         ["대가리", 10, 3],
         ["능지", 10, 2],
         ["섹스", 10, 1],
         ["야스", 10, 1],
         ["개", 8, 4],
         ["미친", 8, 3],
         ["야", 8, 2],
         ["인정", 8, 2],
         ["우와", 8, 2],
         ["헐", 9, 1],
         ["이야", 8, 3],
         ["존나", 8, 2],
         ["병신", 8, 4],
         ["이불킥", 10, 1],
         ["급식", 8, 3],
         ["상남자", 8, 4],
         ["하남자", 10, 1],
         ["ㅍㅌㅊ", 10, 1],
         ["국룰", 10, 1],
         ["여친", 8, 1],
         ["남친", 8, 1],
         ["연애", 7, 2],
         ["야", 8, 3],
         ["아니", 7, 3],
         ["쿨거래", 9, 1],
         ["알빠노", 10, 2],
         ["악플", 9, 3],
         ["먹방", 8, 2],
         ["코노", 10, 1],
         ["인싸", 10, 1],
         ["아잇", 8, 1],
         ["롤", 8 ,1],
         ["게임", 7, 2],
         ["응아니야", 10, 1],
         ["공익", 8, 3],
         ["정공", 9, 2],
         ["ㅈㅈ", 10, 1],
         ["수능", 8, 4],
         ["마라", 9, 1],
         ["레전드", 9, 2],
         ["샌즈", 10, 1],
         ["카톡", 8, 3],
         ["노잼", 9, 1],
         ["꿀잼", 9, 1],
         ["아가리", 8, 3],
         ["갑분싸", 9, 1],
         ["아재개그", 8, 2],
         ["엄", 9, 1],
         ["엄준식",9, 1],
         ["지렸다", 10, 1],
         ["쌌다", 8, 3],
         ["미쳤다", 8, 2],
         ["어쩔티비", 10, 1],
         ["구라", 8, 1],
         ["스트레스", 8, 2],
         ["헐", 8, 1],
         ["대박", 8, 2],
         ["신박한", 8, 2],
         ["기모띠", 10, 1],
         ["MZ", 9, 1],
         ["여러분", 5, 7],
         ["가족", 4, 8],
         ["최고", 3, 8],
         ["홧팅", 1, 9],
         ["늘", 3, 9],
         ["건강", 2 ,9],
         ["평안", 1, 10],
         ["사랑합니다", 1, 10],
         ["건강하세요", 2, 9],
         ["담소", 3, 9],
         ["처리", 4, 6],
         ["해석", 4, 7],
         ["분석", 4, 6],
         ["재롱", 3, 8],
         ["힘내세요", 3, 8],
         ["고맙습니다", 3, 8],
         ["학생", 3, 6],
         ["과제", 5, 5],
         ["제출", 3, 9],
         ["부탁", 4, 7],
         ["제안", 3, 7],
         ["바랍니다", 2, 8],
         ["요소", 3, 7],
         ["세미나", 4, 6],
         ["학회", 3, 8],
         ["경로당", 4, 8],
         ["교수", 4, 8],
         ["도전", 4, 7],
         ["입력", 2, 8],
         ["출력", 3, 7],
         ["교육", 4, 7],
         ["정말", 3, 8],
         ["너무", 4, 7],
         ["예약", 4, 6],
         ["착오", 2, 8],
         ["영화관", 4, 7],
         ["상사", 4, 6],
         ["직장", 3, 7],
         ["회사", 4, 5],
         ["수고", 4, 6],
         ["죄송합니다", 5, 7],
         ["잘", 4, 6],
         ["구속", 2, 9],
         ["시켜", 3, 8],
         ["에휴", 4, 8],
         ["루삥뽕", 10, 1],
         ["어쩔",8 ,2],
         ["GOAT", 8 ,1],
         ["손주", 2, 8],
         ["대표", 3, 7],
         ["회장", 3, 7],
         ["소장", 2, 8],
         ["손녀", 2, 8],
         ["진지", 5, 7],
         ["뽕짝", 3, 9],
         ["읍니다", 1, 10],
         ["OTL", 3, 8],
         ["오락", 2, 8],
         ["되겠는가",2,8],
         ["하겠는가",2,8],

         ]


sent = input("문장을 입력하시오 : ")
noun = okt.morphs(sent)

bad_poss = bad_sum / (no_bad_sum + bad_sum)
not_bad_poss = bad_sum / (no_bad_sum + bad_sum)

mz_poss = mz_sum / (no_mz_sum + mz_sum)
not_mz_poss = no_mz_sum / (no_mz_sum + mz_sum)

poss_sum = 0

for i in noun:
    for j in bad_words:
        if j[0] == i:
            bad_poss *= j[1]/bad_sum
            not_bad_poss *= j[2]/no_bad_sum
        else:
            bad_poss *= (1 - j[1]/bad_sum)
            not_bad_poss *= (1 - j[2]/no_bad_sum)

    for j in mz_words:
        if j[0] == i:
                mz_poss *= j[1]/mz_sum
                not_mz_poss *= j[2]/no_mz_sum
        else:
            mz_poss *= (1 - j[1]/mz_sum)
            not_mz_poss *= (1 - j[2]/no_mz_sum)

print(noun)
bad_poss = bad_poss/(bad_poss+not_bad_poss)
poss_sum += bad_poss*100
print("욕설을 통한 MZ력 분석 : ",bad_poss*100,"%")

# if bad_poss > 0.5:
#     print("욕설 입니다")
# else:
#     print("욕설이 아닙니다")

mz_poss = mz_poss/(mz_poss+not_mz_poss)
poss_sum += mz_poss*100
print("사용한 단어들을 통한 MZ력 분석 : ", mz_poss*100, "%")

# if mz_poss > 0.5:
#     print("MZ 입니다")
# else:
#     print("MZ가 아닙니다")

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
mz_end_poss=0
if short_ans_cnt:
    mz_end_poss = 100
elif mz_end_words_cnt > not_mz_end_words_cnt:
    mz_end_poss = 90
elif mz_end_words_cnt < not_mz_end_words_cnt:
    mz_end_poss = 10
else:
    mz_end_poss = 50.23584975
# print("mz한 종결어미, 틀 같은 종결어미, 음슴체")
# print(mz_end_words_cnt, not_mz_end_words_cnt, short_ans_cnt)
poss_sum += mz_end_poss
print("종결어미를 통한 MZ력 분석 : ", mz_end_poss, "%")

single_word_cnt = 0
mz_symbol_cnt = 0
not_mz_symbol_cnt = 0
single_word_mz_power = [50,60,30,70,80,90]

for word in sent:
    if word >= 'ㄱ' and word <= 'ㅎ':
        single_word_cnt += 1
    if word >= 'ㅏ' and word <= 'ㅡ':
        single_word_cnt += 1

    if word == '.' or word == ',' or word == '~' or word == '^' or word == '*':
        not_mz_symbol_cnt += 1
    if word == '?' or word == '!' or word == ';' or word == '(' or word == ')':
        mz_symbol_cnt += 1

if single_word_cnt > 5:
    mz_single_poss = 100
else:
    mz_single_poss = single_word_mz_power[single_word_cnt]
poss_sum += mz_single_poss
print("자음이나 모음만 쓰이는 경우를 통한 MZ력 분석 : ", mz_single_poss, "%")

mz_symbol_poss=0
if mz_symbol_cnt > not_mz_symbol_cnt:
    mz_symbol_poss = min(100,50+(mz_symbol_cnt-not_mz_symbol_cnt)*10)
elif mz_symbol_cnt < not_mz_symbol_cnt:
    mz_symbol_poss = max(0,50-(not_mz_symbol_cnt-mz_symbol_cnt)*10)
else:
    mz_single_poss = 50

poss_sum += mz_symbol_poss
print("특수기호를 통한 MZ력 분석 : ", mz_symbol_poss, "%")

print("모든 분석을 통한 당신의 MZ력 : ", poss_sum/5,"%")
