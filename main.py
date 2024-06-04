import json
import sys
import warnings

import nofity
import requests
from banner import banner
from toCSV import resultsToCSV

# Global variable
datas = dict()
cnt = 0
results = dict()
output = False
Fast = False
warnings.filterwarnings(action='ignore')

# 요청을 숨기기 위함
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
}


def check_user():
    if len(sys.argv[1::]) == 0:
        nofity.user_not_found()
        exit(1)


def read_json():
    global datas
    with open('data.json', 'r', encoding='utf-8') as data_file:
        datas = json.load(data_file)
    data_file.close()


def find_user():
    global cnt, output, Fast
    for user in sys.argv[1::]:
        if user == '-version' or user == '-v':
            print('Version 1.0')
            exit(0)
        elif user == '-help' or user == '-h':
            print('Usage: python main.py [-verion], [-v], [-help], [-h], [-output], [-o], [-fast], [-f] [username1], [username2], ...')
            print('-v, -version : 버전을 확인합니다.')
            print('-h, -help : 도움말을 확인합니다.')
            print('-o, -output : 결과를 파일로 출력합니다.')
            print('-f, -fast : 오탐방지 기능을 끕니다.')
            print('username1, username2, ... : 검색할 유저명을 입력합니다.')
            exit(0)
        elif user == '-output' or user == '-o':
            output = True
        elif user == '-fast' or user == '-f':
            Fast = True
        else:
            results[user] = dict()
            nofity.start(user)
            for data in datas:
                site = data['name']
                url = data['url'].replace('{}', user)
                try:
                    response = requests.get(url, headers=headers, verify=False)
                    if response.status_code == 200:
                        if data['user_not_found'] in response.text and data['user_not_found'] != '' and Fast == False:
                            continue
                        nofity.search(site, url, response.status_code)
                        cnt += 1
                    results[user][data['name']] = url
                except requests.exceptions.RequestException:
                    continue
            print('\r' + '=' * 20 + '\r')
            nofity.result(cnt, user)
            cnt = 0


def main():
    banner("PodoChung")

    check_user()

    read_json()

    find_user()

    if output:
        resultsToCSV(results)


if __name__ == '__main__':
    main()
