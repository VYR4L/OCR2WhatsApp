from selenium import webdriver
import time


def send_whatsapp_message(list_no, text, link):
    with open ("exclude.txt", "r") as file:
        excluded_numbers = file.read().splitlines()

    driver = webdriver.Chrome()
    for phone_no in list_no:
        driver.get('https://wa.me' + phone_no)
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(text)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(link)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(3)

        excluded_numbers.append(phone_no)
    
    driver.quit()
