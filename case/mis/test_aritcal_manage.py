import pytest

import config
from page.mis.mis_aaritcal_page import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestAritcalMana:
    # 类级别的初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        self.login_page = MisLoginProxy()
        self.home_page = MisHomePage()
        self.ad_page = MisAtcalProxy()

    # def setup(self):
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # 测试审核文章的测试用例
    def test_aduit_ari_pass(self):
        # 定义测试数据
        ari_title = config.PUB_ARITCAL_TITLE
        # 调用进入审核文章页面的业务方法
        self.home_page.to_aaritcal_page()
        # 调用审核文章的业务方法
        self.ad_page.test_aduit_pass(ari_title)
        # 断言
        assert is_element_exist(self.driver, "驳回")

    # # 测试驳回文章的测试用例
    # @pytest.mark.run(order=3)
    # def test_reject_aritcal(self):
    #     # 调用进入审核文章页面的业务方法
    #     self.home_page.to_aaritcal_page()
    #     # 调用驳回的业务方法
    #     self.ad_page.test_reject()
    #     # 断言
    #     assert is_element_exist(self.driver, "查看")

    def teardown_class(self):
        DriverUtils.quit_mis_driver()
