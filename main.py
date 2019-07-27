from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import os
from time import sleep
f1=open("marks.txt","a")
url=input()
roll=int(input("Enter the starting roll no:"))
end=int(input("Enter the ending roll no:"))
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)
dropDown=Select(driver.find_element_by_id('msg-exam'))
dropDown.select_by_index(1)
while(roll<=end):
        inputField=driver.find_element_by_id('msg-regno')
        inputField.send_keys(roll)
        window_before=driver.window_handles[0]
        driver.execute_script('return ValidateResultAndNavigate()')
        inputField.clear()
        window_after=driver.window_handles[1]
        driver.switch_to_window(window_after)
        sleep(2)
        soup=BeautifulSoup(driver.page_source, 'html.parser')
        tds=soup.find_all('td')[-3]
        f1.write(str(roll)+' ')
        for t in tds.find_all('span'):
                f1.write(t.text+' ')
        driver.execute_script('window.close()')
        roll=roll+1
        f1.write('\n')
        driver.switch_to_window(window_before)
f1.close()
driver.close()

