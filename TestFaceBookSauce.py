import unittest
import time

from selenium import webdriver

class FacebookTestsOnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = dict(platform="WINDOWS",
                                    browserName="firefox",
                                    version="3.6",
                                    name="Facebook")
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,
         command_executor="http://Desperado:3c2da000-5590-4b14-8c70-eec80cf76c26@ondemand.saucelabs.com:80/wd/hub")

    def test_login(self):
        self.driver.start_client()
        self.driver.get('http://www.facebook.com')
        self.driver.find_element_by_id("email").send_keys("strazhnyk@ukr.net")
        self.driver.find_element_by_id("pass").send_keys("qwerty4321")
        self.driver.find_element_by_xpath("//*[contains(@class, 'uiButton uiButtonConfirm')]").click()
        self.assertTrue(self.driver.current_url=='http://www.facebook.com/home.php')
        
        
    def test_logout(self):
        self.driver.start_client()
        self.driver.get('http://www.facebook.com')
        self.driver.find_element_by_id("email").send_keys("strazhnyk@ukr.net")
        self.driver.find_element_by_id("pass").send_keys("qwerty4321")
        self.driver.find_element_by_xpath("//*[contains(@class, 'uiButton uiButtonConfirm')]").click()
        self.assertTrue(self.driver.current_url=='http://www.facebook.com/home.php')
        self.driver.find_element_by_id("navAccountLink").click()
        self.driver.find_element_by_css_selector("label.uiLinkButton.logoutButton").click()
        self.assertTrue(self.driver.find_element_by_id("email"))
        self.assertTrue(self.driver.find_element_by_id("pass"))

    def test_post_datetime(self):
        self.driver.start_client()
        self.driver.get('http://www.facebook.com')
        self.driver.find_element_by_id("email").send_keys("strazhnyk@ukr.net")
        self.driver.find_element_by_id("pass").send_keys("qwerty4321")
        
        self.driver.find_element_by_xpath("//*[contains(@class, 'uiButton uiButtonConfirm')]").click()
        self.assertTrue(self.driver.current_url=='http://www.facebook.com/home.php')

        localtime = time.asctime( time.localtime(time.time()) )
        self.driver.find_element_by_css_selector("textarea.uiTextareaAutogrow.input.mentionsTextarea.textInput.DOMControl_placeholder").send_keys(localtime)
        self.driver.find_element_by_css_selector("label.uiOverlayButton.uiButton.uiButtonConfirm").click()   
        self.driver.find_element_by_css_selector("a.uiTooltip.uiSelectorButton.uiButtonSuppressed.uiButtonNoText").click()
         
        self.driver.find_element_by_link_text("Friends of Friends").click()
        
        self.driver.find_element_by_css_selector("label.submitBtn.uiButton.uiButtonConfirm.uiButtonLarge").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
