import json
import sys
import threading
import warnings

import requests

import nofity
from banner import banner
from domain_checker import e_checker
from toCSV import resultsToCSV

# Global variable
datas = dict()
cnt = 0
results = dict()

categories = dict()
findcategories = dict()

output = False
Fast = False
Domain = False
target_domain = str()
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
    global cnt, output, Fast, Domain
    global target_domain
    args = iter(sys.argv[1::])
    for user in args:
        if user == '-version' or user == '-v':
            print('Version 1.0')
            exit(0)
        elif user == '-help' or user == '-h':
            print('Usage: python main.py [-verion], [-v], [-help], [-h], [-output], [-o], [-fast], [-f], [-domain domain_path], [-d domain_path] [username1], [username2], ...')
            print('-v, -version : 버전을 확인합니다.')
            print('-h, -help : 도움말을 확인합니다.')
            print('-o, -output : 결과를 파일로 출력합니다.')
            print('-f, -fast : 오탐방지 기능을 끕니다.')
            print('username1, username2, ... : 검색할 유저명을 입력합니다.')
            print('-d, -domain : 입력된 도메인의 정보와 검색할 유저명을 비교합니다.')
            exit(0)
        elif user == '-output' or user == '-o':
            output = True
        elif user == '-fast' or user == '-f':
            Fast = True
        elif user == '-domain' or user == '-d':
            Domain = True
            target_domain = next(args)
        else:
            for data in datas[0]:
                data = data.strip()
                categories[data] = 0
                findcategories[data] = 0
            results[user] = dict()
            nofity.start(user)
            if Domain:
                d_result, d_re_dict = e_checker(user, target_domain, thr=0.3)
                nofity.domain(target_domain, user, d_result, d_re_dict)
            for data in datas[1::]:
                site = data['name']
                url = data['url'].replace('{}', user)
                for word in str(data['category']).split(','):
                    categories[word.strip()] += 1
                try:
                    response = requests.get(url, headers=headers, verify=False)
                    if response.status_code == 200:
                        if data['user_not_found'] in response.text and data['user_not_found'] != '' and Fast == False:
                            continue
                        nofity.search(site, url, response.status_code)
                        cnt += 1
                    results[user][data['name']] = url
                    for word in str(data['category']).split(','):
                        findcategories[word.strip()] += 1
                except requests.exceptions.RequestException:
                    continue
            print('\r' + '=' * 20 + '\r')
            nofity.result(cnt, user)
            cnt = 0


def draw_histogram():
    labels = [nofity.pad_string(label, 15) for label in categories.keys()]
    values = [findcategories[label] for label in categories.keys()]
    sorted_pairs = sorted(zip(labels, values), key=lambda x: x[0])
    sorted_labels, sorted_values = zip(*sorted_pairs)
    nofity.plot_histogram(sorted_labels, sorted_values)
    

def main():
    banner("PodoChung")

    check_user()

    read_json()

    find_user()

    if output:
        resultsToCSV(results)
        
    draw_histogram()

if __name__ == '__main__':
    main()
