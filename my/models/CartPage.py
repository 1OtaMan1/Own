from models.driver import MyDriver
from models.LoginPage import LoginPage


class CartPage:
    # driver = MyDriver()
    login_page = LoginPage()

    def add_mac_to_cart(self):
        self.login_page.driver.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/a').click()
        self.login_page.driver.driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a').click()
        self.login_page.driver.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a/img').click()
        self.login_page.driver.driver.find_element_by_id("button-cart").click()

    def go_to_cart(self):
        self.login_page.driver.driver.find_element_by_class_name("fa-shopping-cart").click()
        self.login_page.driver.driver.refresh()

    def edit_good_qty(self):
        self.login_page.driver.driver.find_element_by_class_name("fa-shopping-cart").click()
        self.login_page.driver.driver.find_element_by_name("quantity").send_keys('2')


page = CartPage()
page.add_mac_to_cart()
page.go_to_cart()
page.edit_good_qty()
