from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.waits import Waits


class BasePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = Waits(self.driver)
        self.action_chains = ActionChains(self.driver)
        self.dashboard_module = self.driver.find_element(By.ID, "menu_dashboard_index")
        self.admin_module = self.driver.find_element(By.ID, "menu_admin_viewAdminModule")
        self.time_module = self.driver.find_element(By.ID, "menu_time_viewTimeModule")
        self.recruitment_module = self.driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule")
        self.myinfo_module = self.driver.find_element(By.ID, "menu_pim_viewMyDetails")
        self.success_message_status = False
        self.success_message_txt = ""

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_success_save_msg_txt(self):
        return self.success_message_txt

    def is_success_save_msg_displayed(self):
        return self.success_message_status
