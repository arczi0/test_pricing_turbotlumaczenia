from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EXECUTABLE_PATH = 'chromedriver.exe'
URL = 'https://turbotlumaczenia.pl'


@given('Start browser')
def first_step(context):
    context.driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    context.driver.maximize_window()
    context.driver.get(url=URL)


@when('The user clicks button')
def second_step(context):
    estimate_button = context.driver.find_element(By.XPATH,
                                                  "//body/div[@id='page']/div[@id='pages_show']/div[@id='site_index']/section[@id='clouds']/div[1]/div[1]/a[1]")
    estimate_button.click()


@when('The user enters the text and selects the target language')
def third_step(context):
    to_lang = context.driver.find_element(By.CLASS_NAME, "dropdown_expand--left")
    to_lang.click()

    en_lang = context.driver.find_element(By.ID, "Row_1en").click()

    de_lang = context.driver.find_element(By.ID, "Row_16de").click()

    extra_translator = context.driver.find_element(By.XPATH, "//input[@id='verification']")
    extra_translator.click()

    text_file = open("text.txt", "r", encoding='utf-8')
    text = text_file.read()

    text_to_translate = context.driver.find_element(By.XPATH, "//textarea[@id='content']").send_keys(text)


@when('The user selects additional options')
def fourth_step(context):
    extra_translator = context.driver.find_element(By.XPATH, "//input[@id='verification']")
    extra_translator.click()
    time.sleep(5)


@then('The application will respond with the time and cost of the service')
def fifth_step(context):
    estimated_value = context.driver.find_element(By.CSS_SELECTOR,
                                                  "section.content.content--order:nth-child(4) div.container div.row:nth-child(2) div.col-lg-4.col-sm-12.col-md-12 div.content__slider div.row div.col-sm-12.col-md-12.col-lg-10.offset-lg-2 div.content__bluebox div:nth-child(1) div.content__row:nth-child(2) div.row div.col-sm-6:nth-child(1) > span.content__strong")
    estimated_time = context.driver.find_element(By.CSS_SELECTOR,
                                                 "section.content.content--order:nth-child(4) div.container div.row:nth-child(2) div.col-lg-4.col-sm-12.col-md-12 div.content__slider div.row div.col-sm-12.col-md-12.col-lg-10.offset-lg-2 div.content__bluebox div:nth-child(1) div.content__row:nth-child(1) div.row div.col-sm-6:nth-child(1) > span.content__strong")
    default_value = 'od 10 zł'
    default_time = 'godzina'

    assert default_time != estimated_time and default_value != estimated_value
