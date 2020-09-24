from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TripsMo(unittest.TestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxProfile()
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

        # Enter Path of the directory where you want to download the file in the below line
        firefox_options.set_preference("browser.download.dir", '/home/tanveerkhan/Documents/')
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                       "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")

        self.driver = webdriver.Firefox(executable_path=r'/home/tanveerkhan/trips_mo/tripsmo/tripsmo/geckodriver-v0.24.0-linux32/geckodriver')

    def test_login(self):

        self.driver.get('https://www.kayak.com/h/trips/consoles/pm/regressionjob')


        WebDriverWait(self.driver, timeout=500).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#idp-discovery-submit')))

        with open('/home/tanveerkhan/Downloads/credentials.csv', 'r') as csv_file:
            for credentials in csv_file:
                username =  credentials.split()

        user_name = self.driver.find_element_by_css_selector('#idp-discovery-username')
        user_name.send_keys(username)

        next_Button = self.driver.find_element_by_css_selector('#idp-discovery-submit')
        next_Button.click()

        WebDriverWait(self.driver, timeout=500).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '#input8')))

        with open('/home/tanveerkhan/Downloads/credentials2.csv', 'r') as csv_file:
            for credentials in csv_file:
                password = credentials.split()

        pas = self.driver.find_element_by_css_selector('#input8')
        pas.send_keys(password)

        verify_button = self.driver.find_element_by_css_selector('html body.auth.okta-container div.content div#signin-container div#okta-sign-in.auth-container.main-container div.auth-content div.auth-content-inner div.mfa-verify form#form6.mfa-verify-password.o-form.o-form-edit-mode div.o-form-button-bar input.button.button-primary')
        verify_button.click()

        WebDriverWait(self.driver, timeout=500).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'html body.auth.okta-container div.content div#signin-container div#okta-sign-in.auth-container.main-container div.auth-content div.auth-content-inner div.mfa-verify form#form9.mfa-verify-push.o-form.o-form-edit-mode div.o-form-button-bar input.button.button-primary')))

        send_push_button = self.driver.find_element_by_css_selector('html body.auth.okta-container div.content div#signin-container div#okta-sign-in.auth-container.main-container div.auth-content div.auth-content-inner div.mfa-verify form#form9.mfa-verify-push.o-form.o-form-edit-mode div.o-form-button-bar input.button.button-primary')
        send_push_button.click()

        WebDriverWait(self.driver, timeout=500).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.ant-table-thead > tr:nth-child(1) > th:nth-child(8) > span:nth-child(1) > div:nth-child(1) > span:nth-child(1)')))


        url = raw_input('Enter the job with number you want to get download : eg jobs/1234\n')


        self.driver.get("https://www.kayak.com/h/trips/consoles/pm/regressionjob/#/" + url)

        time.sleep(5)
        if self.driver.find_element_by_css_selector('html body div#rc-1 section.layout.ant-layout main.ant-layout-content div div.ant-row div.ant-col.ant-col-xs-16 div.ant-card.ant-card-bordered div.ant-card-body div p span.ant-tag.ant-tag-green'):
            clickdownload = self.driver.find_element_by_css_selector('html body div#rc-1 section.layout.ant-layout main.ant-layout-content div div.ant-row div.ant-col.ant-col-xs-24 div.ant-card.ant-card-bordered div.ant-card-head div.ant-card-head-wrapper div.ant-card-extra a button.ant-btn.ant-btn-primary')
            clickdownload.click()

        elif self.driver.find_elements_by_xpath("//*[contains(text(), 'Labels (OR)')]"):
            print("This file cannot be downloaded")


    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()