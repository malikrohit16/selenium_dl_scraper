from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/home/singhrohit41/selenium/chromedriver')
driver.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
time.sleep(3)

def get_captcha():
    return input('Enter Captcha: ')

driver.find_element_by_id("form_rcdl:tf_dlNO").send_keys(input('Enter DL number: '))
driver.find_element_by_id('form_rcdl:tf_dob_input').send_keys(input('Enter DOB in dd-mm-yyyy format: '))
driver.find_element_by_id('form_rcdl:j_idt33:CaptchaID').send_keys(get_captcha())
driver.find_element_by_id('form_rcdl:j_idt43').click()

time.sleep(3)

dl_details = {
        'Name':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[1]/tbody/tr[2]/td[2]').text ,
        'Current Status':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[1]/tbody/tr[1]/td[2]/span').text ,
        'Date Of Issue': driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[1]/tbody/tr[3]/td[2]').text,
        'Non-Transport Valid':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[2]/tbody/tr[1]/td[2]').text ,
        'Non-Transport Valid':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[2]/tbody/tr[1]/td[3]').text ,
        'Transport Valid':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[2]/tbody/tr[2]/td[2]').text ,
        'Transport Valid':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt122"]/table[2]/tbody/tr[2]/td[3]').text ,
        'COV Category':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt170_data"]/tr/td[1]').text ,
        'Class Of Vehicle':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt170_data"]/tr/td[2]').text ,
        'COV Issue Date':driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt170_data"]/tr/td[3]').text ,
}

print(dl_details)

driver.quit()
