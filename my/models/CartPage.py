from models.driver import MyDriver
from models.LoginPage import LoginPage


class CartPage:
    driver = MyDriver()

    def go_to_cart(self):
        login_page = LoginPage()
        # self.driver.go_to_home()
        # self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        # self.driver.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
        # self.driver.driver.find_element_by_id("input-email").send_keys(email)
        # self.driver.driver.find_element_by_id("input-password").send_keys(password)
        # self.driver.driver.find_element_by_class_name("btn-primary").click()
        self.driver.driver.find_element_by_class_name("fa-shopping-cart").click()
