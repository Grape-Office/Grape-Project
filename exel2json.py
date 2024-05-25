import csv
import json

csv_file_path = 'data.csv' # our csv file

# csv 파일 읽어오기
with open(csv_file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for line in reader:
        d = {
            'chk_regi': line[0],
            'name': line[1],
            'url': line[2],
            'user_not_found': line[3],
            'description': line[4]
        }
        data.append(d)

data.sort(key=lambda x: x['name'])

json_string = json.dumps(data, ensure_ascii=False, indent=2)

txt_file_path = 'data.json'

with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(json_string)
