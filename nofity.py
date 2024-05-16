from colorama import Fore, Style


def user_not_found():
    title = "사용법: python main.py [유저명1] [유저명2] ..."

    print(Style.BRIGHT + Fore.RED + f"{title}")
    print('\r')
    return


def start(message):
    title = "유저 검색중"

    print(Style.BRIGHT + Fore.GREEN + "[" +
          Fore.YELLOW + "*" +
          Fore.GREEN + f"] {title}" +
          Fore.WHITE + f" {message}")
    print('\r')

    return


def search(site, url, status):
    if status == 200:
        print(Style.BRIGHT + Fore.WHITE + "[" + Fore.GREEN + "+" +
              Fore.GREEN + f"] {site} \t" +
              Fore.WHITE + f": {url}")
    return


def result(cnt, user):
    print(Style.BRIGHT + Fore.WHITE + f"총 {cnt}개의 사이트에서 {user}를 찾았습니다.")
    return
