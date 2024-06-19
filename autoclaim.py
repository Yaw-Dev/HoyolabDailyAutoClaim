from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

hoyolab_dailies_url = 'https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481'

# cookies (not sure which are needed so just put all of them lol)
hoyo_cookies = [
    {
        'name': 'cookie_token_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    },
    {
        'name': 'ltoken_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    },
    {
        'name': 'account_id_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    },
    {
        'name': 'account_mid_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    },
    {
        'name': 'ltmid_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    },
    {
        'name': 'ltuid_v2',
        'value': '',
        'domain': '.hoyolab.com',
        'path': '/',
    }
]

driver_options = Options()
driver_options.add_argument("--headless") # giving a bunch of warnings (hoyo might be blocking headless?) | nevermind, using a useragent bypasses that
driver_options.add_argument("--window-size=1920x1080")
driver_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options=driver_options)

driver.get('https://hoyolab.com/')
time.sleep(5) #? idk if needed but give time for page load

for cookie in hoyo_cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(2)

driver.get(hoyolab_dailies_url)
time.sleep(5)

try: # click the x button on the popup
    x_btn = driver.find_element(By.CLASS_NAME, 'components-home-assets-__sign-guide_---guide-close---2VvmzE')
    x_btn.click()
    time.sleep(1)
except: pass

divs = driver.find_elements(By.CLASS_NAME, 'components-home-assets-__sign-content-test_---sign-item---3gtMqV') # get all daily claim elements

for div in divs:
    try:
        active_day = div.find_element(By.CLASS_NAME, 'components-home-assets-__sign-content-test_---actived-day---34r3rb') # "--actived-day" is the flag we are looking for
        if active_day:
            div.click()
            time.sleep(3) #? value might need to change(?)
            break
    except: continue

driver.quit()