import scrapy
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time
from demo.items import Taobao 

class Taobao:
    def __init__(self):
        self.url ='https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.6a7311d9botob8&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F%3Fspm%3Da2107.1.0.0.5f2311d9wFCQgC' 
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") #
        self.driver = webdriver.Chrome(executable_path=r'd:\program\chrome_driver\chromedriver.exe',options=self.chrome_options) 

        self.driver.set_window_position(20,40)
        self.driver.set_window_size(800,700)
        self.driver.get(self.url)

    def get_start(self):
        try:
            # self.driver.find_elements_by_class_name("SignFlow-tab")[1].click()
            self.driver.find_element_by_css_selector("#fm-login-id").send_keys('')
            self.driver.find_element_by_css_selector("#fm-login-password").send_keys('')
            self.driver.find_element_by_css_selector("#login-form button[type='submit']").click()
        except:
            print('已登陆过')
        handles = self.driver.window_handles  # 获取当前浏览器所有窗口句柄
        self.driver.switch_to.window(handles[-1])  # 切换最新窗口句柄

        info=self.driver.get_cookies()
        self.get_books()
        with open(r"./taobao.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(info))

    def get_books(self):
        time.sleep(3)
        self.driver.find_element_by_css_selector('input#q').send_keys('书')
        time.sleep(1)
        self.driver.find_element_by_css_selector('input#q').send_keys(Keys.ENTER)
        self.get_list()
        pass

    def get_list(self):
        time.sleep(1)
        book_name = self.driver.find_elements_by_css_selector('div.shop>a>span:nth-child(2)')
        item = Taobao()
        for i in book_name:
            item['name'] = i.text
            print('打印下当前页面',i.text)
        
        try:
            self.driver.find_element_by_css_selector('li.item.next').click()
            time.sleep(1)
            self.get_list()
        except:
            print('出错了没有条到下一页')
            pass 


    def jump_next(self):
        time.sleep(1)

if __name__=='__main__':
    Taobao().get_start()
    # print('打印下事件空间')