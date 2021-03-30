from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dataPro import *

driver = webdriver.Chrome()
driver.get("https://image.baidu.com/")

search = driver.find_element_by_name("word")
#输入搜索词
search.send_keys('python')
#点击确认
s_search = driver.find_element_by_class_name('s_search')
s_search.click()

#向下翻页，加载更多图片
count =0
while(count < 300): #向下翻页一定时间
    time.sleep(0.1)
    count= count+1
    # 指定像素
    jsCode = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(jsCode)



if True:
    pics = driver.find_elements_by_class_name('main_img.img-hover')
    print(len(pics))
    #获取相关属性
    for index,i in enumerate(pics):
        img = i.get_attribute('data-imgurl')
        request_download(img, "images/" + str(index) + ".jpg")


driver.close()