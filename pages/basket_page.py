from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BacketPageLocators
import time

class BasketPage(BasePage):
    #Нет товаров в корзине и есть сообщение об этом
    def hasnt_product_in_backet(self):
        assert self.is_not_element_present(*BacketPageLocators.PRODUCTS_IN_BACKET), "There is product in basket"
        assert self.is_element_present(*BacketPageLocators.MESSAGE_IN_BACKET), "No message about empty basket"