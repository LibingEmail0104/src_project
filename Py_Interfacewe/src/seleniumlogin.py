#coding=utf-8
from selenium import webdriver
import time

#调用chrome浏览器
driver=webdriver.Chrome()
#设置浏览器为手机模式
driver.get('https://m.228.cn')
#driver.find_element_by_id("search-text").send_keys("ces")
time.sleep(5)
#driver.find_element_by_xpath("//*[@id=\"app\"]/div[5]/ul/li[2]/a").click()
#获取a标签进行点击用户中心
url=driver.find_element_by_link_text("用户中心")
driver.get(url.get_attribute("href"))
#登录操作
time.sleep(5)
driver.find_element_by_xpath("//*[@id=\"loginfrm\"]/div/div[1]/input").send_keys("15810318261")
driver.find_element_by_xpath("//*[@id=\"loginfrm\"]/div/div[2]/input").send_keys("123456")
driver.find_element_by_id("loginbtn").click()
print(driver.title)
time.sleep(10)
#极验验证

driver.quit()
