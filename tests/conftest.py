import pytest
import time
import csv
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage


@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    request.cls.webdriver_path = GeckoDriverManager().install()
    request.cls.webdriver = webdriver.Firefox


@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path)
    request.cls.initialized_webdriver.get("http://localhost/orangehrm/orangehrm-4.4/orangehrm")
    time.sleep(2)
    request.cls.login_page = LoginPage(request.cls.initialized_webdriver)

    def driver_close():
        time.sleep(2)
        request.cls.initialized_webdriver.close()

    request.addfinalizer(driver_close)


def pytest_generate_tests(metafunc):
    with open('/home/nk/PycharmProjects/orangehrm/credentials.csv', 'r') as data:
        params_list = list(csv.reader(data))
    metafunc.parametrize("email, password", (tuple(params_list)))
