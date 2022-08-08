from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BACKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")

    ALERT_NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    ALERT_PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")