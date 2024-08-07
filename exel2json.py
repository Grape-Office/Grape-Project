import csv
import json

csv_file_path = '한국 커뮤니티 조사 - 시트1 (1).csv'  # our csv file

arr = []

# csv 파일 읽어오기
with open(csv_file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for line in reader:
        d = {
            'name': line[1],
            'url': line[3],
            'user_not_found': line[4],
            'category': line[2]
        }
        data.append(d)
        semiarr = line[2].split(',')
        for i in semiarr:
            arr.append(i)

data.sort(key=lambda x: x['name'])

arr.sort()
arr = list(set(arr))

data.insert(0, arr)

json_string = json.dumps(data, ensure_ascii=False, indent=2)

txt_file_path = 'data.json'

with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(json_string)
