import allure
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


# 对象库层(自媒体)
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # 账号输入框
        self.username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder='验证码']")
        # 登陆按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 找到账号输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找到验证码输入框
    def find_code(self):
        return self.find_elt(self.code)

    # 找到登陆按钮
    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 用户名输入的方法
    @allure.step(title="输入用户名")
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 验证码输入的方法
    @allure.step(title="输入密码")
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 登陆按钮的点击
    @allure.step(title="点击登陆")
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登陆业务方法
    def test_mp_login(self, username, code):
        # 1.输入用户名
        self.login_handle.input_username(username)
        # 2.输入验证码
        self.login_handle.input_code(code)
        # 3.点击登陆按钮
        self.login_handle.click_login_btn()
