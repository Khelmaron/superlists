from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidiationTest(FunctionalTest):

    def test_cannot_add_empty_item_to_list(self):

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text, "You can't have an empty list item!"))

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk!')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk!')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text, "You can't have an empty list item!"))

        inputbox.send_keys('Make tea!')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Make tea!')



