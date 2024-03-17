from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    productList = (By.XPATH,"//div[@class='card h-100']")
    def products(self):
        return self.driver.find_elements(*CheckOutPage.productList)