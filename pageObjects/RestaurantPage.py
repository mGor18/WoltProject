from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class RestaurantPage:
    def __init__(self, driver):
        self.driver = driver

    adama_mishpachtit = (By.XPATH, "//div[@data-id='5f5e2894f531a1b7983c79c9']")
    arancini = (By.XPATH, "//div[@data-id='5f02ea1859e97eee123b570b']")
    malabi = (By.XPATH, "//div[@data-id='5f02ea7b2b13bbacd8e0955a']")
    price_element = (By.XPATH, "//span[@class='ProductViewScreen__OriginalPrice-sc-1aalkz5-9 kVJXxw']")
    # add_button = (By.XPATH, "//div[@class='Button__SpinnerContainer-sc-a3fg5q-4 hrUzBx']")
    add_button = (By.XPATH, "//button[@data-test-id='product-modal.submit']")
    checkout_button_total = (By.XPATH, "//span[@data-test-id='Common.Total']")
    price_running_totals = []

    def get_adama(self):
        return self.driver.find_element(*RestaurantPage.adama_mishpachtit)

    def get_arancini(self):
        return self.driver.find_element(*RestaurantPage.arancini)

    def get_malabi(self):
        return self.driver.find_element(*RestaurantPage.malabi)

    def get_price_element(self):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(RestaurantPage.price_element))
        return self.driver.find_element(*RestaurantPage.price_element)

    def get_add_button(self):
        return self.driver.find_element(*RestaurantPage.add_button)

    def get_checkout_button_total(self):
        button_text = self.driver.find_element(*RestaurantPage.checkout_button_total).text
        return float(button_text[1::])

    def add_price(self, price):
        prices_list = self.price_running_totals

        prices_list.append(price)

    def choose_item(self, item):
        return getattr(RestaurantPage, item)

    def add_order(self, item):
        item_choice = self.choose_item(item)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(item_choice))
        item = self.driver.find_element(*item_choice)
        item.click()
        self.add_price(self.get_price_element().text)
        self.get_add_button().click()

# //div[@data-id='5f5e2894f531a1b7983c79c9']//span[contains(@class, 'price')]
# class="ProductViewScreen__OriginalPrice-sc-1aalkz5-9 kVJXxw"
