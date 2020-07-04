from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import By


class Waits(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.5)

    def wait_for_visibility(self, element: WebElement):
        self.wait.until(EC.visibility_of(element))

    def wait_for_visibility_by(self, by: By, locator: str):
        self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_invisibility_by(self, by: By, locator: str):
        self.wait.until(EC.invisibility_of_element_located((by, locator)))
