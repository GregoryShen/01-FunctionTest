from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import uuid

# handle = driver.current_window_handle

base_url = 'http://172.16.9.254:8888/ibotpro/authmgr/login.jsp'
username = str(uuid.uuid1())[:8]


class Login:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.name = 'admin'
        self.password = 'admin'
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//input[@id="username"]').send_keys(
            self.name)
        self.driver.find_element_by_xpath('//input[@id="password"]').send_keys(
            self.password)
        self.driver.find_element_by_link_text('立即登录').click()
        # self.driver.find_element_by_xpath('//*[@id="loginButton"]').click()
        # driver.implicitly_wait(5)

        # WebDriverWait(self.driver, 10).until(lambda x:
        #                                      x.find_element_by_xpath(
        #                                          '//title'))
        time.sleep(3)
        # print(self.driver.title)
        if self.driver.title == '小i智能机器人统一管理平台':
            print('登录成功')
        else:
            print('登录失败')

    # driver.quit()

    def switch_to_user_management(self):
        # 切换到用户管理
        self.driver.find_element_by_xpath(
            '//div[@class="x-treelist-item-tool x-fa fa-cogs '
            'menutree-cursor-pointer"]').click()
        ac = ActionChains(self.driver)
        ac.move_to_element(
            self.driver.find_element_by_xpath(
                '//*[@id="nav_authmgr"]/li[2]/a')).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="user_mgr"]').click()
        self.driver.switch_to.frame("fr_authmgr")

    def create_user(self):
        ele = self.driver.find_element_by_xpath(
            '//div[@id="user_mgr-bodyWrap"]/div/div/div/a')
        ele.click()
        self.driver.find_element_by_xpath(
            '//*[@name="username"]').send_keys(username)
        self.driver.find_element_by_xpath(
            '//*[@name="password"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@name="roles"]').click()
        # self.driver.find_element_by_xpath('//div[@role="dialog"]//a').click()
        # eles = self.driver.find_elements_by_xpath(
        #     '//*[@class="x-tree-node-text "]')
        # for ele in eles:
        #     if ele.text == '管理员':
        #         print('%s/preceding-sibling::div[@role="button]' % ele)
        # pre_ele = self.driver.find_element_by_xpath()
        #         self.driver.find_element_by_xpath(
        #             '%s/preceding-sibling::div[@role="button]' % ele).click()
        #         break
        self.driver.find_element_by_xpath(
            '//*[@class=" x-tree-checkbox"]').click()
        self.driver.find_element_by_link_text('确定').click()
        self.driver.find_element_by_link_text('保存').click()
        element = self.driver.find_element_by_xpath(
            '//div[text()="保存成功"]')
        if element:
            print("新建成功")
        else:
            print("新建失败")
        #     if e.text == '保存成功':
        #         print('新建成功')
        #         return True

    def edit_user(self):
        self.driver.find_element_by_xpath(
            '//div[text()="test1"]/../../td/div/span').click()
        self.driver.find_element_by_link_text('编辑').click()
        ele = self.driver.find_element_by_xpath('//input[@name="password"]')
        ele.send_keys('test1')
        self.driver.find_element_by_link_text('保存').click()
        element = self.driver.find_element_by_xpath(
            '//div[text()="保存成功"]')
        if element:
            print("修改成功")
        else:
            print("修改失败")

    def del_user(self, username):
        self.driver.find_element_by_link_text('删除').click()
        ele = self.driver.find_element_by_xpath('//div[text()="请先选中需要删除的行！"]')
        if ele:
            print("未选中账户时删除提示语正确")
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[text()="确定"]').click()
        else:
            print("未对删除先选择做限定")
        self.driver.find_element_by_xpath(
            '//div[text()="{0}"]/../../td/div/span'.format(username)).click()
        self.driver.find_element_by_link_text('删除').click()
        self.driver.find_element_by_xpath('//span[text()="是"]').click()

    def unlock_user(self):
        pass

    def refresh_user_list(self):
        time.sleep(2)
        self.driver.find_element_by_link_text('刷新').click()
        print("刷新成功")

    def search_user(self):
        # self.driver.find_elements_by_xpath(
        #     '//div[@class="x-form-item-body x-form-item-body-default x-form-text-field-body x-form-text-field-body-default "]'
        # ).click()
        # self.driver.find_element_by_xpath('//li[text()="全部"]').click()
        self.driver.find_element_by_xpath(
            '//input[@placeholder="输入用户名搜索..."]').send_keys('hyttest')
        self.driver.find_element_by_xpath('//span[text()="搜索"]').click()
        eles = self.driver.find_elements_by_xpath('//tbody/tr/td[3]')
        for ele in eles:
            print(ele.text)


if __name__ == '__main__':
    login = Login()
    login.switch_to_user_management()
    # login.edit_user()
    # login.del_user('0b4bfbfa')
    # login.refresh_user_list()
    login.search_user()
