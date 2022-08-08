from .pages.product_page import ProductPage

def test_guest_should_add_product_to_backet(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_backet()