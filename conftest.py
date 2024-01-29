import pytest
from appium.webdriver.common.appiumby import AppiumBy

from dataProvider import configuration
from settings import *
from appium import webdriver


@pytest.fixture()
def setup(request):
    global driver
    capabilities = {
        'platformName': configuration.initial_setup.get("appium:platformName"),
        # 'platformName': (CONFIG[platform][configuration.desired_cap.get("appium:deviceName")]),
        # 'platformVersion': (CONFIG[platform]['platformVersion']),
        'deviceName': configuration.initial_setup.get("appium:deviceName"),
        # 'automationName': (CONFIG[platform]['automationName']),
        # 'appPackage': (CONFIG[platform]['appPackage']),
        # 'appActivity': (CONFIG[platform]['appActivity']),
        # 'noReset': (CONFIG[platform]['noReset']),
        'app': configuration.initial_setup.get("appium:app"),

    }

    url = configuration.initial_setup.get("url")
    request.instance.driver = webdriver.Remote(url, capabilities)

    def teardown():
        request.instance.driver.quit()

    request.addfinalizer(teardown)
