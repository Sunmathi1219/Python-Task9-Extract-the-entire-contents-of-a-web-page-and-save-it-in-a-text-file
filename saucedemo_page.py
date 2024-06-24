"""
Visit the url https://www.saucedemo.com/ and login with the following credentials
Username:standard_user
password:secret_sauce
Try to fetch the following using python selenium:
1.)Tittle of the web page
2.)Current URL of the webpage
3.)Extract the entire content of the webpage and save it in a text file whose name will be webpage_task_11.txt
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Sauce_demo:
    #username&password data
    user_name = "standard_user"
    password = "secret_sauce"

    #locators
    username_locator = "user-name"
    password_locator = "password"
    button_locator = "/html/body/div/div/div[2]/div[1]/div/div/form/input"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #login with username&password and print the current url and title of the web page
    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.user_name)
            sleep(2)
            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
            sleep(2)

            if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
                print("Login success")
                #1.)Current_url
                print(self.driver.current_url)
                #2.)Tittle
                print(self.driver.title)
                sleep(3)
            return True

        except Exception as e:
                print("Error: Invalid URL", e)
                return False

    #Extract the web page contents and save it in a text file
    def extract_content(self):
            if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
             #3.)Extract the entire contents of the web page
             page_content = self.driver.find_element(By.TAG_NAME, 'body').text
             sleep(2)

                # save the content to a text file format
             with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
                 file.write(page_content)
                 print("Content saved")

             return True

            else:
                print("Error:unable to login")
                return False


    # shutdown the entire python selenium automation
    def shut_down(self):
        self.driver.quit()
        return None

