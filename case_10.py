from selenium import webdriver
import time

link = "https://my.selectel.ru/login/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id("login")
    input1.send_keys("120884")
    input2 = browser.find_element_by_id("password")
    input2.send_keys("Password1")
    button1 = browser.find_element_by_css_selector("button.m-solid")
    button1.click()
    time.sleep(5)

    button2 = browser.find_element_by_css_selector("a.m-solid")
    button2.click()
    time.sleep(5)

    option1 = browser.find_element_by_css_selector("[value='1']")
    option1.click()
    option2 = browser.find_element_by_xpath("//md-checkbox/div[1]")
    option2.click()
    button3 = browser.find_element_by_css_selector("button.m-brand")
    button3.click()
    time.sleep(5)

    button4 = browser.find_element_by_css_selector("button.m-brand")
    button4.click()
    message1 = browser.find_element_by_css_selector("""[ng-bind="'common-form-error' | translate"]""")

finally:
    time.sleep(5)
    browser.quit()
    print("Test Completed")
