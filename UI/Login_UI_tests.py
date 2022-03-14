from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Correct_login_test():
    driver = open_web_page()
    driver.get("https://testpages.herokuapp.com/styled/cookies/adminlogin.html")
    driver.find_element_by_name('username').send_keys('Admin')
    driver.find_element_by_name('password').send_keys('AdminPass')
    driver.find_element_by_id('login').click()
    porovnani = driver.find_element_by_id('gologin').text
    assert "Go To Login" == porovnani


def open_web_page():
    return webdriver.Firefox(executable_path=r"C:\Users\sabin\PythonTesting\UI\geckodriver.exe")

Correct_login_test()