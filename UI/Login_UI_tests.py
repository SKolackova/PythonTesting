import unittest  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):
    
    def Correct_login_test(self):
        driver = open_web_page()
        driver.get("https://testpages.herokuapp.com/styled/cookies/adminlogin.html")
        driver.find_element_by_name('username').send_keys('Admin')
        driver.find_element_by_name('password').send_keys('AdminPass')
        driver.find_element_by_id('login').click()
        porovnani = driver.find_element_by_id('gologin').text
        self.assertEqual("Go To Login", porovnani) 
        driver.quit()

    def Incorrect_password_login_test():
        driver = open_web_page()
        driver.get("https://testpages.herokuapp.com/styled/cookies/adminlogin.html")
        driver.find_element_by_name('username').send_keys('Admin')
        driver.find_element_by_name('password').send_keys('Spatneheslo')
        driver.find_element_by_id('login').click()
        porovnani = driver.find_element_by_id('gologin').text    # musím si ještě najít, jak udělat záporné porovnání,test jestli funguje git
        self.assertEqual("Go To Login", porovnani) 
        driver.quit()



def open_web_page():
        return webdriver.Firefox(executable_path=r"C:\Users\Jaroslav Kafka\uceni\PythonTesting\UI\geckodriver.exe")
    
if __name__ == '__main__':
    unittest.main()