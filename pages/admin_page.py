import time
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import data.data_classes
import pages.myinfo_page
import pages.recruitment_page
import pages.time_page
import pages.dashboard_page


class AdminPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.country = ""
        self.result_list = []
        self.organization_menu = None
        self.locations_menu = None
        self.add_btn = None
        self.delete_btn = None
        self.save_btn = None
        self.location_name = None
        self.location_country_code = None
        self.location_province = None
        self.location_city = None
        self.location_address = None
        self.location_zip_code = None
        self.location_phone = None
        self.location_fax = None
        self.location_notes = None
        self.locations_list = []
        self.location_rec_found = False
        self.location_rec_displayed = False

    def is_location_found(self):
        return self.location_rec_found

    def is_location_displayed(self):
        return self.location_rec_displayed

    def to_organization_menu(self):
        action_chains = ActionChains(self.driver)
        self.organization_menu = self.driver.find_element(By.ID, "menu_admin_Organization")
        action_chains.move_to_element_with_offset(self.organization_menu, 233, 135).click(self.organization_menu) \
            .perform()
        self.locations_menu = self.driver.find_element(By.ID, "menu_admin_viewLocations")
        return self

    def open_locations_menu(self):
        self.locations_menu.click()
        self.wait.wait_for_visibility_by(By.ID, "frmList_ohrmListComponent")
        self.wait.wait_for_visibility_by(By.ID, "resultTable")
        self.add_btn = self.driver.find_element(By.ID, "btnAdd")
        self.delete_btn = self.driver.find_element(By.ID, "btnDelete")
        self.locations_list = self.driver.find_elements(
            By.XPATH, "//table[@id='resultTable']//tr[@class='odd' or @class='even']")
        return self

    def click_add_button(self):
        self.add_btn.click()
        self.wait.wait_for_visibility_by(By.ID, "frmLocation")
        self.location_name = self.driver.find_element(By.ID, "location_name")
        self.location_country_code = self.driver.find_element(By.ID, "location_country")
        self.location_province = self.driver.find_element(By.ID, "location_province")
        self.location_city = self.driver.find_element(By.ID, "location_city")
        self.location_address = self.driver.find_element(By.ID, "location_address")
        self.location_zip_code = self.driver.find_element(By.ID, "location_zipCode")
        self.location_phone = self.driver.find_element(By.ID, "location_phone")
        self.location_fax = self.driver.find_element(By.ID, "location_fax")
        self.location_notes = self.driver.find_element(By.ID, "location_notes")
        self.save_btn = self.driver.find_element(By.ID, "btnSave")
        return self

    def set_location_name(self, name: str):
        self.location_name.send_keys(name)
        return self

    def select_country(self, code: str):
        countries_list = Select(self.location_country_code)
        countries_list.select_by_value(code)
        self.country = countries_list.first_selected_option.text
        return self

    def set_location_province(self, province: str):
        self.location_province.send_keys(province)
        return self

    def set_location_city(self, city: str):
        self.location_city.send_keys(city)
        return self

    def set_location_address(self, address: str):
        self.location_address.send_keys(address)
        return self

    def set_location_zip_code(self, zipcode: str):
        self.location_zip_code.send_keys(zipcode)
        return self

    def set_location_phone(self, phone: str):
        self.location_phone.send_keys(phone)
        return self

    def set_location_fax(self, fax: str):
        self.location_fax.send_keys(fax)
        return self

    def add_location_notes(self, notes: str):
        self.location_notes.send_keys(notes)
        return self

    def save_location(self):
        self.save_btn.click()
        add_success_message = self.driver.find_element(By.XPATH, "//div[@class='message success fadable']")
        self.success_message_txt = add_success_message.text
        self.success_message_status = add_success_message.is_displayed()
        return self

    def click_delete_button(self):
        self.delete_btn.click()
        self.wait.wait_for_visibility_by(By.ID, "deleteConfModal")
        return self

    def confirm_delete(self):
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()
        add_success_message = self.driver.find_element(By.XPATH, "//div[@class='message success fadable']")
        self.success_message_txt = add_success_message.text
        self.success_message_status = add_success_message.is_displayed()
        return self

    def add_location(self, location: data.data_classes.LocationData):
        return self.click_add_button() \
            .set_location_name(location.name) \
            .select_country(location.country_code) \
            .set_location_province(location.state) \
            .set_location_city(location.city) \
            .set_location_address(location.address) \
            .set_location_zip_code(location.zipcode) \
            .set_location_phone(location.phone) \
            .set_location_fax(location.fax) \
            .add_location_notes(location.notes) \
            .save_location()

    def find_location_record_in_list(self, location: data.data_classes.LocationData):
        for location_record in self.locations_list:
            if location_record.find_element(By.XPATH, "//td[2]") == location.name and \
                    location_record.find_element(By.XPATH, "//td[3]") == location.city and \
                    location_record.find_element(By.XPATH, "//td[4]") == self.country and \
                    location_record.find_element(By.XPATH, "//td[5]") == location.phone:
                self.location_rec_found = True
                self.location_rec_displayed = location_record.is_displayed()
                break
        return self

    def mark_location_for_delete(self, location: data.data_classes.LocationData):
        for location_record in self.locations_list:
            # if location_record.find_element(By.XPATH, "//td[2]") == location.name and \
            #         location_record.find_element(By.XPATH, "//td[3]") == location.city and \
            #         location_record.find_element(By.XPATH, "//td[4]") == self.country and \
            #         location_record.find_element(By.XPATH, "//td[5]") == location.phone:
            if True:
                location_record.find_element(By.XPATH, "//td[1]").click()
                break
        return self

    def create_location_record(self, location: data.data_classes.LocationData):
        return self.to_organization_menu().open_locations_menu().add_location(location)

    def find_location_record(self, location: data.data_classes.LocationData):
        return self.to_organization_menu().open_locations_menu().find_location_record_in_list(location)

    def delete_location_record(self, location: data.data_classes.LocationData):
        return self.to_organization_menu().open_locations_menu().mark_location_for_delete(location)\
            .click_delete_button().confirm_delete()

    # navigation part
    def to_dashboard_module(self):
        self.wait.wait_for_visibility(self.dashboard_module)
        self.dashboard_module.click()
        time.sleep(2)
        return pages.dashboard_page.DashboardPage(self.driver)

    def to_time_module(self):
        self.wait.wait_for_visibility(self.time_module)
        self.time_module.click()
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
