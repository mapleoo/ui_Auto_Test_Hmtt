import pytest
from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_element_exist


# 1. 定义测试类
@pytest.mark.run(order=2)
class TestMpLogin:
    # 2. 定义初始化方法
    def setup_class(self):
        # 2.1 获取浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 2.2 创建好所需要调用的业务方法所在的类的对象
        self.login_proxy = LoginProxy()

    # 3. 定义测试方法
    def test_mp_login(self):
        # 3.1 定义测试数据
        username = "13911111111"
        code = "246810"
        # 3.2 调用业务方法形成完整的业务操作
        self.login_proxy.test_mp_login(username, code)
        # 3.3 断言
        assert is_element_exist(self.driver, "江苏传智播客教育科技股份有限公司")

    # 4. 定义销毁的方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
