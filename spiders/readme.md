# 无界面
options.add_argument('--headless')

##### driver属性和方法
# 页面加载
driver.get("http://www.baidu.com")
# 关闭浏览器
driver.close()
# 获取当前URL
driver.current_url
# 刷新
driver.refresh()
# 页面标题
driver.title
# 页面渲染后的源码
driver.page_source
# 获取窗口信息
driver.get_window_rect()

#### --- cookie操作 ---
# 给当前url域设置cookie
# name的值对应cookie key，value的值对应cookie value
driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})
# 可选的属性
# 'domain' -> String,
# 'secure' -> Boolean,
# 'expiry' -> Milliseconds since the Epoch it should expire.

# 输出当前url所有的Cookie
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

# 通过name删除Cookie
driver.delete_cookie("CookieName")
# 删除所有的Cookie
driver.delete_all_cookies()