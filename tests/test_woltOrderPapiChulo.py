from pageObjects.MenuPage import MenuPage
from utilities.baseClass import BaseClass


class TestWolt(BaseClass):

    def test_wolt_order(self):
        log = self.get_logger()
        menu_page = MenuPage(self.driver)

        # !!! GDPR Agreement !!!
        gdpr_button = "button[data-localization-key='gdpr-consents.banner.accept-button']"
        self.driver.find_element_by_css_selector(gdpr_button).click()

        # menu-page

        # access the search bar and add search term
        log.info("Clicking searchbar on homepage")
        menu_page.get_search_bar().click()

        log.info("Adding search query and accessing restaurant page")
        menu_page.get_search_bar().send_keys('Papi Ch')

        log.info("Selecting restaurant - Papi Chulo by clicking from dropdown")
        restaurant_page = menu_page.choose_search_result()

        # restaurant-page

        # select 'adama mishpachtit'
        restaurant_page.add_order('adama_mishpachtit')
        log.info("Selecting item 'adama_mishpachtit' and adding to order")

        # select malabi
        restaurant_page.add_order('malabi')
        log.info("Selecting item 'malabi' and adding to order")

        # select 'arancini'
        # restaurant_page.add_order('arancini')
        # log.info("Selecting item 'arancini' and adding to order")

        print(restaurant_page.price_running_totals)

        # convert strings to numbers and add together
        price_list = restaurant_page.price_running_totals

        new_price_total = []

        for price in price_list:
            new_price = float(price[1::])
            new_price_total.append(new_price)

        print(sum(new_price_total))

        checkout_price = restaurant_page.get_checkout_button_total()

        assert sum(new_price_total) == checkout_price
