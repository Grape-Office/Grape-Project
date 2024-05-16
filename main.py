import json
import sys
import requests
import nofity
import warnings
from banner import banner

# Global variable
datas = dict()
cnt = 0

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
    global cnt
    for user in sys.argv[1::]:
        nofity.start(user)
        for data in datas:
            site = data['name']
            url = data['url'].replace('{user}', user)
            try:
                response = requests.get(url, headers=headers, verify=False)
                nofity.search(site, url, response.status_code)
                if response.status_code == 200:
                    cnt += 1
            except requests.exceptions.RequestException:
                continue
        print('\r')
        nofity.result(cnt, user)
        cnt = 0


def main():
    banner("PodoChung")

    check_user()

    read_json()

    find_user()


if __name__ == '__main__':
    main()
