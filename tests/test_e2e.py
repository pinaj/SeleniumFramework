from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckOutPage import CheckOutPage
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Testone(BaseClass):
    def test_one(self):
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        #checkoutpage = CheckOutPage(self.driver)

        products = checkoutpage.products()

        for product in products :
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("ind")
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        assert "Success! Thank you!" in successText
        self.driver.close()




















