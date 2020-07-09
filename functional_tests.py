from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
# check homepage for TD app
        self.browser.get('http://localhost:8000')

#check page title and header mention to do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


# invited to insert To do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

# add to do item to text box
        inputbox.send_keys('Buy peacock feathers')

# then page updates and now to do item is in a list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find.elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

# text box is still there inviting to add another item
        self.fail('Finish the test!')


#page now updates and shows new item if second item is added

#site generates unique URL for each user

# if you return to that URL the user's stuff will still be here

# end of User Story

if __name__ == '__main__':
    unittest.main(warnings='ignore')

