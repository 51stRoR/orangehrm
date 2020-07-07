from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pages.base_page import BasePage
import time
import pages.myinfo_page
import pages.recruitment_page
import pages.time_page
import pages.admin_page


class DashboardPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def to_admin_module(self):
        self.wait.wait_for_visibility(self.admin_module)
        self.action_chains.move_to_element(self.admin_module).click().perform()
        time.sleep(2)
        return pages.admin_page.AdminPage(self.driver)

    def to_time_module(self):
        self.wait.wait_for_visibility(self.time_module)
        self.action_chains.move_to_element(self.time_module).click().perform()
        time.sleep(2)
        return pages.time_page.TimePage(self.driver)

    def to_recruitment_page(self):
        self.wait.wait_for_visibility(self.recruitment_module)
        self.recruitment_module.click()
        time.sleep(2)
        return pages.recruitment_page.RecruitmentPage(self.driver)

    def to_myinfo_module(self):
        self.wait.wait_for_visibility(self.myinfo_module)
        self.myinfo_module.click()
        time.sleep(2)
        return pages.myinfo_page.MyInfoPage(self.driver)
