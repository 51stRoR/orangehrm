from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import pages.myinfo_page
import pages.recruitment_page
import pages.admin_page
import pages.dashboard_page


class TimePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.attendance_menu = None
        self.punch_inout_menu = None
        self.attendance_records_menu = None
        self.punch_date = None
        self.punch_time = None
        self.in_text_area = None
        self.confirm_punch_btn = None
        self.success_message_status = False
        self.success_message_txt = ""
        self.attendance_date = None
        self.employee_records_list = []
        self.punch_in_date_time = None
        self.punch_out_date_time = None
        self.last_record = None
        self.last_record_punch_in = None
        self.last_record_punch_in_note = None
        self.last_record_punch_out = None
        self.last_record_punch_out_note = None
        self.empty_record = None

    def get_punch_in_date_time(self):
        return self.punch_in_date_time

    def get_punch_out_date_time(self):
        return self.punch_out_date_time

    def get_last_record_punch_in(self):
        return self.last_record_punch_in

    def get_last_record_punch_in_note(self):
        return self.last_record_punch_in_note

    def get_last_record_punch_out(self):
        return self.last_record_punch_out

    def get_last_record_punch_out_note(self):
        return self.last_record_punch_out_note

    def get_empty_record_msg(self):
        return self.empty_record.text

    def is_empty_record_displayed(self):
        return self.empty_record.is_displayed()

    def get_success_punch_msg(self):
        return self.success_message_txt

    def is_success_punch_msg_displayed(self):
        return self.success_message_status

    def to_attendance_menu(self):
        action_chains = ActionChains(self.driver)
        self.attendance_menu = self.driver.find_element(By.ID, "menu_attendance_Attendance")
        action_chains.move_to_element(self.attendance_menu).perform()
        self.attendance_records_menu = self.driver.find_element(By.ID, "menu_attendance_viewMyAttendanceRecord")
        self.punch_inout_menu = self.driver.find_element(By.ID, "menu_attendance_punchIn")
        return self

    def open_punch_menu(self):
        self.punch_inout_menu.click()
        self.wait.wait_for_visibility_by(By.ID, "punchTimeForm")
        return self

    def get_punch_in_data(self):
        self.punch_date = self.driver.find_element(By.ID, "currentDate")
        self.punch_time = self.driver.find_element(By.ID, "currentTime")
        self.in_text_area = self.driver.find_element(By.XPATH, "//textarea[@id='note']")
        self.confirm_punch_btn = self.driver.find_element(By.ID, "btnPunch")
        self.punch_in_date_time = f"{self.punch_date.text} {self.punch_time.text}:00 GMT 2"
        return self

    def get_punch_out_data(self):
        self.punch_date = self.driver.find_element(By.ID, "currentDate")
        self.punch_time = self.driver.find_element(By.ID, "currentTime")
        self.in_text_area = self.driver.find_element(By.XPATH, "//textarea[@id='note']")
        self.confirm_punch_btn = self.driver.find_element(By.ID, "btnPunch")
        self.punch_out_date_time = f"{self.punch_date.text} {self.punch_time.text}:00 GMT 2"
        return self

    def enter_punch_text(self, message: str):
        self.in_text_area.send_keys(message)
        return self

    def save_punch_in(self):
        self.confirm_punch_btn.click()
        return self

    def save_punch_out(self):
        self.confirm_punch_btn.click()
        punch_success_message = self.driver.find_element(By.XPATH, "//div[@class='message success fadable']")
        self.success_message_txt = punch_success_message.text
        self.success_message_status = punch_success_message.is_displayed()
        return self

    def create_punch_record(self, in_message: str, out_message: str):
        return self.to_attendance_menu().open_punch_menu().get_punch_in_data().enter_punch_text(in_message)\
            .save_punch_in().get_punch_out_data().enter_punch_text(out_message).save_punch_out()

    def to_records(self):
        self.attendance_records_menu.click()
        return self

    def set_records_date(self, date: str):
        self.attendance_date = self.driver.find_element(By.ID, "attendance_date")
        self.attendance_date.clear()
        self.attendance_date.send_keys(date + Keys.ENTER)
        return self

    def get_no_records_table(self):
        self.wait.wait_for_visibility_by(By.ID, "recordsTable")
        self.empty_record = self.driver.find_element(
            By.XPATH, "//form[@id='employeeRecordsForm']//tr/td[@id='noRecordsColumn']")
        return self

    def get_records_table(self):
        self.wait.wait_for_visibility_by(By.ID, "recordsTable")
        self.employee_records_list = self.driver.find_elements(
            By.XPATH, "//form[@id='employeeRecordsForm']//tr[@class='odd' or @class='even']")
        return self

    def get_last_record_data(self):
        self.last_record = self.employee_records_list[-1].find_elements(By.XPATH, "./td")
        self.last_record_punch_in = self.last_record[1].text
        self.last_record_punch_in_note = self.last_record[2].text
        self.last_record_punch_out = self.last_record[3].text
        self.last_record_punch_out_note = self.last_record[4].text
        return self

    def check_punch_in_records_table(self, date: str):
        return self.to_attendance_menu().to_records().set_records_date(date).get_records_table().get_last_record_data()

    def check_empty_records_table(self, date: str):
        return self.to_attendance_menu().to_records().set_records_date(date).get_no_records_table()

    # navigation methods
    def to_dashboard_module(self):
        self.wait.wait_for_visibility(self.dashboard_module)
        self.dashboard_module.click()
        return pages.dashboard_page.DashboardPage(self.driver)

    def to_admin_module(self):
        self.wait.wait_for_visibility(self.admin_module)
        self.admin_module.click()
        return pages.admin_page.AdminPage(self.driver)

    def to_recruitment_page(self):
        self.wait.wait_for_visibility(self.recruitment_module)
        self.recruitment_module.click()
        return pages.recruitment_page.RecruitmentPage(self.driver)

    def to_myinfo_module(self):
        self.wait.wait_for_visibility(self.myinfo_module)
        self.myinfo_module.click()
        return pages.myinfo_page.MyInfoPage(self.driver)
