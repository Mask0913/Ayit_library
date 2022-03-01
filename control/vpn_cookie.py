#coding=utf-8
from selenium import  webdriver
import time

class vpn_cookie:

    def get_cookie(self):
        with open('user_pwd.txt', 'r') as f:
            user_pwd = eval(f.read())
        driver = webdriver.Chrome()
        driver.get('https://webvpn.ayit.edu.cn/')
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="loginNew"]/div[2]/div[2]/div[2]/div[2]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="credentials"]/ul/li[2]/input').send_keys(user_pwd['username'])
        driver.find_element_by_xpath('//*[@id="credentials"]/ul/li[3]/input').send_keys(user_pwd['password'])
        driver.find_element_by_xpath('//*[@id="credentials"]/ul/li[5]/input[3]').click()
        diccookie = driver.get_cookie("client_vpn_ticket")
        cookie = str(diccookie["value"])
        driver.quit()
        print(cookie)
        with open('cookie.txt', 'w') as f:
            f.write(cookie)
        time.sleep(1)

if __name__ == '__main__':
    vpn_cookie().get_cookie()



