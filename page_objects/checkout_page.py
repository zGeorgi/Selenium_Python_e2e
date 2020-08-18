from selenium.webdriver.common.by import By

from page_objects.confirm_page import Confirm


class CheckOut:

    def __init__(self, driver):
        self.local_driver = driver

    item_name = (By.LINK_TEXT, "Blackberry")

    def add_blackbery_in_basket(self):
        item = self.local_driver.find_element(*CheckOut.item_name)
        item.find_element_by_xpath("parent::h4/parent::div/parent::div"
                                   "/div[@class='card-footer']/button").click()

    checkout_btn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def click_checkout(self):
        self.local_driver.find_element(*CheckOut.checkout_btn).click()

    quantity = (By.CSS_SELECTOR, "#exampleInputEmail1")

    def get_item_quantity(self):
        return self.local_driver.find_element(*CheckOut.quantity).get_attribute("value")

    second_check = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def check_after_verify(self):
        self.local_driver.find_element(*CheckOut.second_check).click()
        return Confirm(self.local_driver)