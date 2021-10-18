from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.RestaurantPage import RestaurantPage


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    search_bar = (By.XPATH, "//input[@id='SearchInputAnimated-input-id']")
    search_result = (By.PARTIAL_LINK_TEXT, "Papi Ch")
    # search_result = (By.XPATH, "//a[@href='/en/isr/tel-aviv/restaurant/papi-chulo']")
    # search_result = (By.XPATH, '//a[@href="/en/isr/tel-aviv/restaurant/papi-chulo" and @data-test-id="SearchResultItem"]')
    #                           //a[@href="/en/isr/tel-aviv/restaurant/papi-chulo" and @data-test-id="SearchResultItem"]
    def get_search_bar(self):
        return self.driver.find_element(*MenuPage.search_bar)

    def get_search_result(self):
        return self.driver.find_element(*MenuPage.search_result)

    def choose_search_result(self):
        WebDriverWait(self.driver, 7).until(ec.presence_of_element_located(MenuPage.search_result))
        el = self.get_search_result()
        el.click()
        restaurant_page = RestaurantPage(self.driver)

        return restaurant_page
