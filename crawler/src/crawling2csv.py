import csv

# .txt 파일 읽기

file_names = [
    '817081',
    '783052',
    '769209',
    '747269',
    '641253',
    '792651',
    '812354',
    '783053',
    '717481',
    '796152'
]

for file_name in file_names:
    with open(f'../data/webtoon/{file_name}.txt', 'r') as in_file:
        lines = in_file.readlines()

    # 첫 두 글자가 공백인 행 제외
    filtered_lines = [line.strip()
                      for line in lines if not line.startswith('  ')]

    # 리스트를 한 열로 하여 CSV 파일 생성
    with open(f'{file_name}.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['내용'])
        writer.writerows([[line] for line in filtered_lines])
