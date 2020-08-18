from selenium.webdriver.common.by import By
from page_objects.checkout_page import CheckOut


class HomePage:

    def __init__(self, driver):
        self.local_driver = driver

    shop_btn = (By.LINK_TEXT, "Shop")

    def click_shop_btn(self):
        self.local_driver.find_element(*HomePage.shop_btn).click()
        return CheckOut(self.local_driver)

    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")

    def get_name_input(self):
        return self.local_driver.find_element(*HomePage.name)

    email = (By.XPATH, "//input[@name='email']")

    def get_email(self):
        return self.local_driver.find_element(*HomePage.email)

    tick = (By.ID, "exampleCheck1")

    def check_box(self):
        return self.local_driver.find_element(*HomePage.tick)

    drop_down = (By.ID, "exampleFormControlSelect1")

    def drop_down_locator(self):
        return self.local_driver.find_element(*HomePage.drop_down)

    submit = (By.XPATH, "//input[@class='btn btn-success']")

    def submit_data(self):
        return self.local_driver.find_element(*HomePage.submit)

    msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def get_message(self):
        return self.local_driver.find_element(*HomePage.msg).text
