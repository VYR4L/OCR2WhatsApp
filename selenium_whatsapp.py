from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import keyboard

def send_whatsapp_message(list_no, text, link):

    with open("exclude.txt", "r") as file:
        excluded_numbers = file.read().splitlines()

    user_data_dir = "C:\\Users\\fkzza\\AppData\\Local\\Google\\Chrome\\User Data"
    profile_name = "Default"

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory={profile_name}")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get('https://web.whatsapp.com/')
    time.sleep(4)

    for phone_no in list_no:
        # Abrir uma nova guia
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        
        # Navegar para a URL do WhatsApp com o número de telefone
        driver.get('https://wa.me/' + phone_no)
        time.sleep(4)

        # Verifica e fecha a caixa de diálogo
        try:
            go_to_app_button = driver.find_element(By.XPATH, '//*[@id="action-button"]')  # primeira parte do processo de abrir o wpp web
            go_to_app_button.click()  # clica no botão do iniciar conversa
            time.sleep(4)
            keyboard.press_and_release('esc')
            time.sleep(4)
            go_to_app_button.click()
        except:
            pass
        
        time.sleep(4)
        open_app_button = driver.find_element(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a/span') 
        open_app_button.click()
        # Abre o QR code do WhatsApp Web

        time.sleep(4)  # Aguarde o carregamento da página do WhatsApp

        # Envie a mensagem de texto
        message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        message_box.send_keys(text)
        send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        send_button.click()
        time.sleep(4)

        # Envie o link
        message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        message_box.send_keys(link)
        send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        send_button.click()
        time.sleep(4)

        excluded_numbers.append(phone_no)

        # Fechar a guia atual
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    driver.quit()
