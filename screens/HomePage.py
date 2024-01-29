from utilities.Utils import PageUtils
import time
from dataProvider.base import Base


class homepage(Base):
    click_btn = ('xpath', '//android.widget.Button[@content-desc="Here"]')


    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def click_here(self):
        self.click(self.click_btn)

    def click_element(self):
        self.click_here()
        return self.check_element("This is screen 2")


