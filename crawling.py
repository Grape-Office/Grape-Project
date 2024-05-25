from selenium import webdriver

def check_alert(url, options) :
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    try :
        result = driver.switch_to.alert
        return True #사용자 X
    except :
        return False #사용자 O
    
def crawlingFunc(url, description) :
    options = webdriver.ChromeOptions()
    user_agent = "User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if description == "alert" :
        flag = check_alert(url, options)
        return not flag #사용자 O => True