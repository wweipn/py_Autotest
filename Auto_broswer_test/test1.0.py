from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.fullscreen_window()
# 访问百度
driver.get('https://www.baidu.com')
# 输入同学
driver.find_element_by_name('wd').send_keys('同学')
# 点击搜索
driver.find_element_by_id('su').click()
# 点击第一个搜索结果
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# 定义链接名称
handles = driver.window_handles
# 关闭第一个选项卡
driver.close()
# 选择第二个选项卡
driver.switch_to.window(handles[1])
# 点击第二个选项卡的内容
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(3)
driver.quit()
