"""
后台管理系统-->审核文章
"""
# 对象库层
import time

from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisAtcalPage(BasePage):

    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title = (By.CSS_SELECTOR, "[placeholder*='文章名称']")
        # 选择频道

        # 点击查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过/驳回确认按钮
        self.pass_con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

        self.time = (By.CSS_SELECTOR, "[placeholder='选择结束时间']")

    # 找到文章标题搜索输入框
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找到选择频道

    # 找到点击查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 找到通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 找到驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 找到确认按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.pass_con_rej_btn)

    def find_time(self):
        return self.find_elt(self.time)


# 操作层
class MisAtcalHandle(BaseHandle):
    def __init__(self):
        self.mis_atcal_page = MisAtcalPage()

    # 文章标题搜索框输入
    def input_ari_title(self, title):
        # 调用父类的模拟输入的方法
        self.input_text(self.mis_atcal_page.find_ari_title(), title)

    # 选择文章状态
    def check_ari_status(self, status):
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", status)

    # 查询按钮点击
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 审核通过按钮点击
    def click_aduit_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 驳回按钮点击
    def click_regic_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 确认审核通过/驳回的按钮点击
    def click_confim_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()

    def clear_time(self):
        self.mis_atcal_page.find_time().clear()


# 业务层
class MisAtcalProxy:
    def __init__(self):
        self.mis_atcal_handle = MisAtcalHandle()

    # 审核通过的测试用例
    def test_aduit_pass(self, title):
        # 1.输入搜索的文章名称
        self.mis_atcal_handle.input_ari_title(title)
        self.mis_atcal_handle.clear_time()
        # 2.选择文章状态
        self.mis_atcal_handle.check_ari_status("待审核")
        # 3.点击查询按钮
        self.mis_atcal_handle.click_query_btn()
        time.sleep(2)
        # 4.点击通过按钮
        self.mis_atcal_handle.click_aduit_pass_btn()
        # 5.点击提示框的确认对象
        self.mis_atcal_handle.click_confim_btn()
        # 6.选择文章状态为:审核通过
        self.mis_atcal_handle.check_ari_status("审核通过")
        # 7.点击查询按钮
        self.mis_atcal_handle.click_query_btn()

    # 驳回的测试用例
    def test_reject(self):
        # 2.选择文章状态
        self.mis_atcal_handle.check_ari_status("待审核")
        # 3.点击查询按钮
        self.mis_atcal_handle.click_query_btn()
        time.sleep(2)
        # 4.点击驳回按钮
        self.mis_atcal_handle.click_regic_btn()
        # 5.点击提示框的确认对象
        self.mis_atcal_handle.click_confim_btn()
        time.sleep(2)
        # 6.切换审核失败页面
        self.mis_atcal_handle.check_ari_status("审核失败")
        # 7.点击查询按钮
        self.mis_atcal_handle.click_query_btn()
        time.sleep(2)
