import pytest
from base.login_action import LoginActions
#from screens.HomePage import LoginApp


@pytest.mark.usefixtures('setup')
class BaseTests:

    @pytest.fixture
    def init(self):
        driver = self.driver

