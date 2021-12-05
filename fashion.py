from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
import requests
from pathlib import Path

# save images to this folder
images_folder_path = "/Users/Kejkaew/Downloads/test/"


driver = webdriver.Chrome('/Users/Kejkaew/Downloads/test/chromedriver')
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys('korean fashion casual',Keys.ENTER)

# you can use Images instead of ค้นรูป
elem = driver.find_element_by_link_text('ค้นรูป')
elem.get_attribute('href')
elem.click()
value = 0

# scroll down for more images 
for i in range(3):
	driver.execute_script('scrollBy("+ str(value) +",+500);')
	value += 100
	time.sleep(4)
elements = driver.find_elements_by_xpath('//img[contains(@class,"rg_i")]')

# show number of images 
print(len(elements))

count = 0
for i in elements:
    
    try:
        i.click()
        time.sleep(5)
        preview_image = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
        src = preview_image.get_attribute('src')
        print(src)

        # save images to this folder
        data_folder_name = Path(r'fashion-v2')
        if not os.path.exists(images_folder_path / data_folder_name):
            os.mkdir(images_folder_path / data_folder_name)

        # create image file name
        file_name = os.path.join('korean_'+str(count)+'.jpg')
        r = requests.get(src)
        with open(images_folder_path / data_folder_name / file_name,'wb') as outfile:
            outfile.write(r.content)

        print("success for file: ", file_name)
    except:
            # print(exception)
        print("failure for file: ", i)
    
    count += 1


driver.quit()