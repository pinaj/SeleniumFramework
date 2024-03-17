import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.FormSubmissionData import FormSubmissionData
from Utilities.BaseClass import BaseClass


class Testfillingforms(BaseClass):

    def test_fillingforms(self, get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Entering the first name")
        homepage.get_name().send_keys(get_data['firstname'])
        homepage.get_email().send_keys(get_data['email'])
        homepage.get_password().send_keys(get_data['pwd'])
        self.select_option_text(homepage.get_gender_dropdown(),get_data['gender'])
        homepage.get_gender_submit_button().click()
        success_msg = homepage.get_success_msg().text
        print(success_msg)

        assert success_msg == '×\nSuccess! The Form has been submitted successfully!.'
        self.driver.refresh()

    @pytest.fixture(params=FormSubmissionData.test_form_submission_data)
    def get_data(self,request):
        return request.param
