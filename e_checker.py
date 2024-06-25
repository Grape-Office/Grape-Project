import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import whois


def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            'domain_name': w.domain_name,
            'registrar': w.registrar,
            'whois_server': w.whois_server,
            'referral_url': w.referral_url,
            'updated_date': [date.isoformat() if isinstance(date, datetime) else date for date in w.updated_date] if isinstance(w.updated_date, list) else (w.updated_date.isoformat() if isinstance(w.updated_date, datetime) else w.updated_date),
            'creation_date': [date.isoformat() if isinstance(date, datetime) else date for date in w.creation_date] if isinstance(w.creation_date, list) else (w.creation_date.isoformat() if isinstance(w.creation_date, datetime) else w.creation_date),
            'expiration_date': [date.isoformat() if isinstance(date, datetime) else date for date in w.expiration_date] if isinstance(w.expiration_date, list) else (w.expiration_date.isoformat() if isinstance(w.expiration_date, datetime) else w.expiration_date),
            'name_servers': w.name_servers,
            'status': w.status,
            'emails': w.emails,
            'dnssec': w.dnssec,
            'name': w.name,
            'org': w.org,
            'address': w.address,
            'city': w.city,
            'state': w.state,
            'zipcode': w.zipcode,
            'country': w.country
        }
    except Exception as e:
        return {'error': str(e)}

def find_e_owner():
    # read JSON
    with open('e_data.json', 'r') as file:
        data = json.load(file)

    domain_info = {}

    # get domain info with multiThreading
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(get_whois_info, domain): domain for domain in data['domains']}
        for future in as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                info = future.result()
                domain_info[domain] = info
            except Exception as e:
                domain_info[domain] = {'error': str(e)}

    return domain_info

def is_related_to_user(domain_info, user):
    if isinstance(domain_info, dict):
        if 'name' in domain_info and user in str(domain_info['name']):
            return True
        if 'emails' in domain_info and any(user in str(email) for email in domain_info['emails']):
            return True
        if 'org' in domain_info and user in str(domain_info['org']):
            return True
    return False

def e_checker(user):
    # get all of domain infomation
    all_domain_info = find_e_owner()

    # filtering with multiThreading
    related_domains = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(is_related_to_user, info, user): domain for domain, info in all_domain_info.items()}
        for future in as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                if future.result():
                    related_domains[domain] = all_domain_info[domain]
            except Exception as e:
                related_domains[domain] = {'error': str(e)}

    # store related infomation
    with open(f'related_domains_{user}.json', 'w') as file:
        json.dump(related_domains, file, indent=4)

if __name__ == '__main__':
    e_checker("username")
