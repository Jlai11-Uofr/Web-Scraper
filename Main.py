from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Test  import initialize_VPN,rotate_VPN,terminate_VPN
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
crimefile = open("Usernames.txt", 'r')

temp = [line[:-1] for line in crimefile]


initialize_VPN(stored_settings=1)





for item in temp:
        try:
                rotate_VPN()
                time.sleep(5)
                DRIVER_PATH = 'chromedriver'
                driver = webdriver.Chrome(executable_path=DRIVER_PATH)




                driver.get('https://azeriteps.io/vote')
                time.sleep(3)

                username = driver.find_element_by_id('username').send_keys(item)

                submit = driver.find_element_by_class_name('buy-btn').click()


                time.sleep(1)

                #sites = driver.find_element_by_xpath(('//div[@id="step"]//a'))

                #print(sites)

                elements = driver.find_elements_by_css_selector("div.row a")

                sites_tovote = elements[2:4]
                ##Cant solve captcha ye

                for item in sites_tovote:
                        ActionChains(driver) \
                        .key_down(Keys.CONTROL) \
                        .click(item) \
                        .key_up(Keys.CONTROL) \
                        .perform()

                driver.switch_to.window(driver.window_handles[1])
                time.sleep((2))


                submit = driver.find_element_by_class_name('btn.btn-outline-white.btn-block.rounded-pill').click()
                javaScript = "window.scrollBy(0,1000);"
                driver.execute_script(javaScript)

                time.sleep((4))
                submit = driver.find_element_by_class_name('btn.btn-default.vote').click()
                time.sleep((2))
                driver.switch_to.window(driver.window_handles[2])
                time.sleep(4)
                submit = driver.find_element_by_class_name('btn.btn-success').click()

                time.sleep(5)
                driver.quit()
        except Exception as  e:
                print(e)
                continue

