from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.remote.webdriver import By
from utils.waits import Waits
import pages.dashboard_page


class LoginPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = Waits(self.driver)
        self.username_fld = self.driver.find_element(By.ID, "txtUsername")
        self.password_fld = self.driver.find_element(By.ID, "txtPassword")
        self.submit_btn = self.driver.find_element(By.ID, "btnLogin")

    def enter_user_name(self, username: str):
        self.username_fld.send_keys(username)
        return self

    def enter_password(self, password: str):
        self.password_fld.send_keys(password)
        return self

    def click_login_button(self):
        self.submit_btn.click()
        return pages.dashboard_page.DashboardPage(self.driver)

    def correct_login(self, username: str, password: str):
        return self.enter_user_name(username).enter_password(password).click_login_button()
