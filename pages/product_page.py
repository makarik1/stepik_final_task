from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_add_product_to_backet(self):
        name_product_main = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        price_product_main = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text

        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BACKET).click()
        self.solve_quiz_and_get_code()

        name_in_message = self.browser.find_element(*ProductPageLocators.ALERT_NAME_OF_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_OF_PRODUCT).text

        assert name_product_main == name_in_message, "Product name doesn't match"
        assert price_product_main == price_in_message, "Product price doesn't match"