import scrapy
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# class Demo(scrapy.Spider):
#     name = 'demo'
#     allowed_domains = ['https://www.zhihu.com/signin?next=%2F']
#     start_urls=['https://www.zhihu.com/signin?next=%2F']

# def parse(self,resoponse):
#     pass
## C:\Program Files\Google\Chrome\Application
## --remote-debugging-port=9222

class Demo:
    def __init__(self):
        self.url ='https://www.zhihu.com/signin?next=%2F' 
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  #
        self.driver = webdriver.Chrome(executable_path=r'd:\program\chrome_driver\chromedriver.exe',options=self.chrome_options) 

        self.driver.set_window_position(20,40)
        self.driver.set_window_size(800,700)
        self.driver.get(self.url)

    def get_start(self):
        try:
            self.driver.find_elements_by_class_name("SignFlow-tab")[1].click()
            self.driver.find_element_by_css_selector("#root input[name='username']").send_keys('')
            self.driver.find_element_by_css_selector("input[name='password']").send_keys('')
            self.driver.find_element_by_css_selector("#root button[type='submit']").click()
        except:
            print('已登陆过')

        info=self.driver.get_cookies()
        print(info)
        with open(r"./info.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(info))

if __name__=='__main__':
    Demo()
    # print('打印下事件空间')