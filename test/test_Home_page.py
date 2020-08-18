import pytest

from data_tests.homePageData import HomePageData
from page_objects.home_page import HomePage
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homepage(self, load_data):
        log = self.getLog_obj()

        home_page = HomePage(self.driver)
        home_page.get_name_input().send_keys(load_data["first_name"])
        log.info(load_data["first_name"])

        home_page.get_email().send_keys(load_data["email"])
        log.info(load_data["email"])

        home_page.check_box().click()
        log.info("tick the checkbox")

        self.select_option_by_text(home_page.drop_down_locator(), load_data["gender"])
        log.info(load_data["gender"])

        home_page.submit_data().click()
        print(home_page.get_message())
        log.info("submit the Data and print the message! ")
        self.driver.refresh()


@pytest.fixture(params=HomePageData.data)
def load_data(request):
    return request.param
