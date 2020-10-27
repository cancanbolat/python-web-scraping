from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# 1 allow, 2 block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(chrome_options=option, executable_path='drivers/chromedriver')
browser.get("https://www.facebook.com/")
time.sleep(1)

username = browser.find_element_by_xpath('//*[@id="email"]')
username.send_keys("")

password = browser.find_element_by_xpath('//*[@id="pass"]') 
password.send_keys("")
time.sleep(1)

signBtn = browser.find_element_by_name("login")
signBtn.click()

market = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[3]") 
market.click()
time.sleep(2)

for i in range(1,2):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)

markets = browser.find_elements_by_class_name("a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7") 
marketlist = []

for market in markets:
    marketlist.append(market.text)

with open("market.txt", "w", encoding="UTF-8") as file:
    for product in marketlist:
        file.write(product.strip() + "\n")

time.sleep(2)

browser.quit()



