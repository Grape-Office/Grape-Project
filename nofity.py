from colorama import Fore, Style
from wcwidth import wcswidth

CATEGORIE_WIDTH = 20
BRIGHT_GREEN_PLUS = f"{Style.BRIGHT}{Fore.WHITE}[{Fore.GREEN}+] "


def pad_string(s, width):
    pad_length = width - wcswidth(s)
    return s + ' ' * pad_length


def plot_histogram(labels, values):
    for label, value in zip(labels, values):
        print(
            f"{Style.BRIGHT}{label}: {Fore.GREEN}{'▇▇' * int(value)} {Fore.BLUE}{value}")


def user_not_found():
    title = "사용법: python main.py [옵션] [유저명1] [유저명2] ..."

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
        padded_site = pad_string(site, CATEGORIE_WIDTH)
        print(f"{BRIGHT_GREEN_PLUS}{Fore.GREEN}{padded_site}{Fore.WHITE}: {url}")
    return


def result(cnt, user):
    print(Style.BRIGHT + Fore.WHITE + f"총 {cnt}개의 사이트에서 {user}를 찾았습니다.")
    return


def domain(domain, user, result, re_dic):
    if result:
        print(
            Style.BRIGHT +
            Fore.WHITE +
            f"사이트 \"{domain}\"과 \"{user}\"는 연관되어 보입니다.")
        for key, value in re_dic.items():
            if 'Registrant' == key:
                print(f"\t{key}: {value}")
            if 'Administrative' == key:
                print(f"\t{key}: {value}")
            if 'AC E-Mail' == key:
                print(f"\t{key}: {value}")
        print()
    else:
        print(
            Style.BRIGHT +
            Fore.WHITE +
            f"사이트 \"{domain}\"과 \"{user}\"는 연관이 없어 보입니다.\n")
    return
