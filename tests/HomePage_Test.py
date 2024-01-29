import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.HomePage import *
from utilities.ReadExcel import *


class homepage_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - TC_BT_P4_001")
    def test_verify_visiblity_of_how_to_play(self):
        home = homepage(self.driver)
        self.assertTrue(home.click_element())


