import os

import pandas as pd


def resultsToCSV(data):
    for username, data in data.items():
        csv_data = {'site':[], 'url':[]}
        for name, url in data.items():
            csv_data['site'].append(name)
            csv_data['url'].append(url)
        toCSV(username, csv_data)

def toCSV(username, result):
    df = pd.DataFrame(result)
    folder_name = 'result'
    file_name = 'results_{}.csv'.format(username)
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    csv_file_path = os.path.join(folder_name, file_name)
    df.to_csv(csv_file_path, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    toCSV_data = {'Column1': [1, 2, 3, 4],
            'Column2': ['A', 'B', 'C', 'D']}
    
    resultsToCSV_data = {
        'seungjin': {'네이버': 'https://blog.naver.com/seungjin', '티스토리': 'https://seungjin.tistory.com', '디벤치 - 개발자 포럼': 'https://devbench.kr/users/seungjin', '깃허브': 'http://github.com/seungjin', 'Chzzk': 'http://api.chzzk.naver.com/service/v1/search/channels?keyword=seungjin', '일간베스트': 'http://www.ilbe.com/list/jjal?searchType=nick_name&search=seungjin', 'velog': 'https://velog.io/@seungjin/posts', '에펨코리아': 'https://www.fmkorea.com/search.php?search_keyword=seungjin&search_target=nick_name', '루리웹': 'https://bbs.ruliweb.com/hobby/board/300228//?search_type=name&search_key=seungjin', '아카라이브': 'https://arca.live/b/breaking?target=nickname&keyword=seungjin', '나무위키': 'https://namu.wiki/w/사용자:seungjin', '브런치스토리': 'https://brunch.co.kr/@seungjin', '인스타그램': 'https://www.instagram.com/seungjin', '유튜브': 'https://www.youtube.com/@seungjin', '쿨앤조이': 'https://coolenjoy.net/bbs/profile.php?mb_id=seungjin', '힙합플레이야': 'https://hiphopplaya.com/g2/bbs/profile.php?mb_id=seungjin', '풋셀': 'https://footsell.com/g2//bbs/profile.php?mb_id=seungjin', '스팀잇': 'https://steemit.com/@seungjin', '미디엄': 'https://medium.com/@seungjin', '인벤': 'https://www.inven.co.kr/member/inventory/view_inventory.php?nick=seungjin'},
        'kimkimkim': {'네이버': 'https://blog.naver.com/승진', '티스토리': 'https://승진.tistory.com', '디벤치 - 개발자 포럼': 'https://devbench.kr/users/승진', '깃허브': 'http://github.com/승진', 'Chzzk': 'http://api.chzzk.naver.com/service/v1/search/channels?keyword=승진', '일간베스트': 'http://www.ilbe.com/list/jjal?searchType=nick_name&search=승진', 'velog': 'https://velog.io/@승진/posts', '에펨코리아': 'https://www.fmkorea.com/search.php?search_keyword=승진&search_target=nick_name', '루리웹': 'https://bbs.ruliweb.com/hobby/board/300228//?search_type=name&search_key=승진', '아카라이브': 'https://arca.live/b/breaking?target=nickname&keyword=승진', '나무위키': 'https://namu.wiki/w/사용자:승진', '브런치스토리': 'https://brunch.co.kr/@승진', '인스타그램': 'https://www.instagram.com/승진', '유튜브': 'https://www.youtube.com/@승진', '쿨앤조이': 'https://coolenjoy.net/bbs/profile.php?mb_id=승진', '힙합플레이야': 'https://hiphopplaya.com/g2/bbs/profile.php?mb_id=승진', '풋셀': 'https://footsell.com/g2//bbs/profile.php?mb_id=승진', '스팀잇': 'https://steemit.com/@승진', '미디엄': 'https://medium.com/@승진', '인벤': 'https://www.inven.co.kr/member/inventory/view_inventory.php?nick=승진'},
    }

    toCSV("temp", toCSV_data)
    resultsToCSV(resultsToCSV_data)
