import pytest
from selenium import webdriver

#https://docs.pytest.org/en/7.1.x/example/simple.html
#this is to write mutilpe options using command line option

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")

@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        #firefox invocation
        print("hi  firefox")
    elif browser_name == "IE":
        #IE invocation
        print("IE")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
