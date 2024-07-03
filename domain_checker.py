import re
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import requests


def is_shortened_url(url):
    shortened_domains = [
        "bit.ly", "t.co", "goo.gl", "tinyurl.com",
        "is.gd", "ow.ly", "buff.ly", "shorte.st",
        "clk.im", "trib.al", "tiny.cc", "t.ly",
        "url.kr", "kvo.kr", "u2.to", "bit.do",
        "mcaf.ee", "soo.gd", "yourls.org", "v.gd",
        "qr.ae", "x.co", "adf.ly", "lnkd.in",
        "ift.tt", "po.st", "rb.gy", "1url.com",
        "cutt.ly", "rebrandly.com", "bl.ink", "t2mio.com",
        "vzturl.com", "shorturl.at", "short.cm"
    ]
    
    domain_pattern = re.compile(r"https?://([^/]+)")
    match = domain_pattern.match(url)
    
    if match:
        domain = match.group(1)
        if domain in shortened_domains:
            return True
    
    return False

def get_original_url(short_url):
    if is_shortened_url(short_url):
        try:
            response = requests.head(short_url, allow_redirects=True)
            return response.url
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
    else:
        return short_url

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def is_related_to_user(domain_info, user, thr = 0.3):
    def is_similar(value, user):
        threshold = thr  # 유사도로 판단할 임계값 설정 (0.0 ~ 1.0)
        if not value:
            return False
        distance = levenshtein_distance(value.lower(), user.lower())
        similarity = 1 - distance / max(len(value), len(user))
        return similarity >= threshold

    if isinstance(domain_info, dict):
        if 'Registrant' in domain_info and is_similar(domain_info['Registrant'], user):
            return True
        if 'Administrative' in domain_info and is_similar(domain_info['Administrative'], user):
            return True
        if 'AC E-Mail' in domain_info and domain_info['AC E-Mail'] is not None:
            if any(is_similar(email, user) for email in domain_info['AC E-Mail']):
                return True
    return False

## KISA WHOIS
## => OpenAPI로 수정 필요: https://xn--c79as89aj0e29b77z.xn--3e0b707e/kor/openkey/keyCre.do
def query_krnic_whois(domain):
    server = "whois.kr"
    port = 43
    query = f"{domain}\r\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        s.send(query.encode())
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    
    return response.decode()


def parse_whois_response(response):
    result = {}
    lines = response.splitlines()
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def e_checker(user, url, thr=0.3):
    domain = get_original_url(url)
    response = query_krnic_whois(domain)
    parsed_result = parse_whois_response(response)
    # for key, value in parsed_result.items():
    #     print(f"{key}: {value}")
    return is_related_to_user(parsed_result, user, thr=thr)


if __name__ == '__main__':
    result = e_checker("magicclub", "magicclub.co.kr", thr=0.3)
    print(result)
