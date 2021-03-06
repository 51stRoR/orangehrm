from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pages.base_page import BasePage
import pages.myinfo_page
import pages.time_page
import pages.admin_page
import pages.dashboard_page


class RecruitmentPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def to_dashboard_module(self):
        self.wait.wait_for_visibility(self.dashboard_module)
        self.dashboard_module.click()
        return pages.dashboard_page.DashboardPage(self.driver)

    def to_admin_module(self):
        self.wait.wait_for_visibility(self.admin_module)
        self.admin_module.click()
        return pages.admin_page.AdminPage(self.driver)

    def to_time_module(self):
        self.wait.wait_for_visibility(self.time_module)
        self.time_module.click()
        return pages.time_page.TimePage(self.driver)

    def to_myinfo_module(self):
        self.wait.wait_for_visibility(self.myinfo_module)
        self.myinfo_module.click()
        return pages.myinfo_page.MyInfoPage(self.driver)