from selenium import webdriver
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Start desire browser from cmd"
    )
    parser.addoption(
        "--second_param", action="store", default="SecondArg_fromCmd",
        help="Start desire browser from cmd"
    )


@pytest.fixture(scope="class")
def invoke_browser(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
         chr_options = wbdriver.ChromeOptions()
         driver = webdriver.Remote("http://ec2-18-134-74-167.eu-west-2.compute.amazonaws.com/:4444", options=chr_options)
       
    elif browser_name == "firefox":
         chr_options = wbdriver.FirefoxOptions()
         driver = webdriver.Remote("http://ec2-18-134-74-167.eu-west-2.compute.amazonaws.com/:4444", options=chr_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    print(request.config.getoption("--second_param"))
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("/home/georgi/PycharmProjects/E_Shop/reports/" + name)
