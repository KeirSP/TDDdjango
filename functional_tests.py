from selenium import webdriver
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
        self.fail('Finish the test!')

# invited to insert To do item

# add to do item to text box

# then page updates and now to do item is in a list

# text box is still there inviting to add another item

#page now updates and shows new item if second item is added

#site generates unique URL for each user

# if you return to that URL the user's stuff will still be here

# end of User Story

if __name__ == '__main__':
    unittest.main(warnings='ignore')

