from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    #the below variable is created inside a tuple, (*HomePage.shop)-->* is for indicating that it is a tuple

    name_field = (By.XPATH,"//div[@class = 'form-group']/descendant::input[@name = 'name']")
    email_field = (By.XPATH,"//div[@class = 'form-group']/descendant::input[@name = 'email']")
    password_field = (By.XPATH,"//div[@class = 'form-group']/descendant::input[@id = 'exampleInputPassword1']")
    gender_dropdown = (By.XPATH,"//div[@class = 'form-group']/descendant::select[@id = 'exampleFormControlSelect1']")
    submit_button = (By.XPATH,"//input[@class= 'btn btn-success']")
    success_message = (By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_name(self):
        return self.driver.find_element(*HomePage.name_field)

    def get_email(self):
        return self.driver.find_element(*HomePage.email_field)

    def get_password(self):
        return self.driver.find_element(*HomePage.password_field)

    def get_gender_dropdown(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    def get_gender_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_success_msg(self):
        return self.driver.find_element(*HomePage.success_message)
    def shopItems(self):
         self.driver.find_element(*HomePage.shop).click()
         checkoutpage = CheckOutPage(self.driver)
         return checkoutpage
