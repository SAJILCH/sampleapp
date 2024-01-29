from appium.webdriver.common.touch_action import TouchAction

from utilities.Utils import PageUtils


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.page_utils = PageUtils(self.driver)

    def get_element(self, locator):
        self.page_utils.get_element(locator)

    def get_elements(self, locator):
        self.page_utils.get_elements(locator)

    def get_element_by_type(self, method, value):
        self.page_utils.get_element_by_type(method, value)

    def is_visible(self, locator):
        self.page_utils.is_visible(locator)

    def android_scroll(self, locator):
        self.page_utils.android_scroll(locator)

    def ios_scroll(self, locator):
        self.page_utils.ios_scroll(locator)

    def scrolling(self, locator):
        self.page_utils.scrolling(locator)

    def swipeing(self, locator):
        self.page_utils.swipe(locator)

    def wait_visible(self, locator, timeout=10):
        self.page_utils.wait_visible(locator, timeout)

    def click(self, locator):
        self.page_utils.click(locator)

    def tap(self, locator):
        self.page_utils.tap(locator)

    def send_keys(self, locator, text):
        self.page_utils.send_keys(locator, text)

    def clear(self, locator):
        self.page_utils.clear(locator)

    def hide_keyboard(self):
        self.page_utils.hide_keyboard()

    def back(self):
        self.page_utils.close()

    def wait(self, locator):
        self.page_utils.wait(locator)

    def get_text(self, locator):
        return self.page_utils.get_text(locator)

    def action_perform(self, locator):
        self.page_utils.action_tap(locator)

    def tap_by_cordinates(self, x, y):
        self.page_utils.action_tap_bycordinates(x, y)

    def set_value(self, locator, text):
        self.page_utils.set_value(locator, text)

    def is_element_present(self, locator):
        return self.page_utils.is_element_present(locator)

    def system_bar(self):
        return self.page_utils.get_system_bar()

    def seekbarrow_scroll(self, locator):
        return self.page_utils.seekbarrow_scrolling(locator)

    def seekbarseat_scroll(self, locator):
        return self.page_utils.seekbarseat_scrolling(locator)

    def change_accebility(self):
        return self.change_accebility()


