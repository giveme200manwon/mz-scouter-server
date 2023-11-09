import csv

# .txt 파일 읽기
with open('data/641253.txt', 'r') as in_file:
    lines = in_file.readlines()

# 첫 두 글자가 공백인 행 제외
filtered_lines = [line.strip() for line in lines if not line.startswith('  ')]

# 리스트를 한 열로 하여 CSV 파일 생성
with open('output.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['내용'])
    writer.writerows([[line] for line in filtered_lines])