from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EXECUTABLE_PATH = 'chromedriver.exe'
URL = 'https://turbotlumaczenia.pl'

driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
driver.maximize_window()

driver.get(url=URL)

estimate_button = driver.find_element(By.XPATH,
                                      "//body/div[@id='page']/div[@id='pages_show']/div[@id='site_index']/section[@id='clouds']/div[1]/div[1]/a[1]")
estimate_button.click()

to_lang = driver.find_element(By.CLASS_NAME, "dropdown_expand--left")
to_lang.click()

en_lang = driver.find_element(By.ID, "Row_1en").click()

de_lang = driver.find_element(By.ID, "Row_16de").click()

extra_translator = driver.find_element(By.XPATH, "//input[@id='verification']")
extra_translator.click()

text_file = open("text.txt", "r", encoding='utf-8')
text = text_file.read()

text_to_translate = driver.find_element(By.XPATH, "//textarea[@id='content']").send_keys(text)

time.sleep(5)

estimated_value = driver.find_element(By.CSS_SELECTOR,
                                      "section.content.content--order:nth-child(4) div.container div.row:nth-child(2) div.col-lg-4.col-sm-12.col-md-12 div.content__slider div.row div.col-sm-12.col-md-12.col-lg-10.offset-lg-2 div.content__bluebox div:nth-child(1) div.content__row:nth-child(2) div.row div.col-sm-6:nth-child(1) > span.content__strong")
estimated_time = driver.find_element(By.CSS_SELECTOR,
                                     "section.content.content--order:nth-child(4) div.container div.row:nth-child(2) div.col-lg-4.col-sm-12.col-md-12 div.content__slider div.row div.col-sm-12.col-md-12.col-lg-10.offset-lg-2 div.content__bluebox div:nth-child(1) div.content__row:nth-child(1) div.row div.col-sm-6:nth-child(1) > span.content__strong")

print("Koszt podanego tlumaczenia to: ", estimated_value.text)
print("Czas potrzebny na tlumaczenie to: ", estimated_time.text)
