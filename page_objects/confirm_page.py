from selenium.webdriver.common.by import By


class Confirm:

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")

    def find_country(self, country_code):
        self.driver.find_element(*Confirm.country).send_keys(country_code)

    link = (By.LINK_TEXT, "Italy")

    def select_country(self):
        self.driver.find_element(*Confirm.link).click()

    tick = (By.XPATH, "//label[@for='checkbox2']")

    def terms_and_conditions(self):
        self.driver.find_element(*Confirm.tick).click()

    purchase = (By.CSS_SELECTOR, ".btn-success")

    def press_purchase(self):
        self.driver.find_element(*Confirm.purchase).click()

    msg = (By.CLASS_NAME, "alert")

    def get_the_msg(self):
        return self.driver.find_element(*Confirm.msg).text
