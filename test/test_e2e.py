from utilities.baseClass import BaseClass
from page_objects.home_page import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLog_obj()
        home_page = HomePage(self.driver)
        checkout_page = home_page.click_shop_btn()
        log.info("click shop Btn")

        checkout_page.add_blackbery_in_basket()
        log.info("Select item")
        checkout_page.click_checkout()
        log.info("click checkout")
        item = "Blackberry"
        self.wait_link_presence(item, 9)
        quantity = checkout_page.get_item_quantity()
        assert 1 == int(quantity)
        log.info("pass verification")

        confirm_page = checkout_page.check_after_verify()
        link = "Italy"
        confirm_page.find_country("ita")
        self.wait_link_presence(link, 9)
        confirm_page.select_country()
        log.info("select country for delivery")

        confirm_page.terms_and_conditions()
        confirm_page.press_purchase()
        log.info("accept term&conditions And finalize")
        assert "Success" in confirm_page.get_the_msg()
