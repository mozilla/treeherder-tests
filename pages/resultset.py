#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class ResultsetPage(Base):

    _job_details_locator = (By.ID, 'result-status-pane')
    _job_details_status_locator = (By.CSS_SELECTOR, '#result-status-pane > div:nth-child(1) > span:nth-child(2)')
    _logviewer_locator = (By.ID, 'logviewer-btn')
    _resultset_locator = (By.CSS_SELECTOR, 'div.row.result-set')


    @property
    def job_details_status(self):
        self.selenium.find_element(*self._job_details_locator)
        return self.selenium.find_element(*self._job_details_status_locator).text

    def go_to_page(self):
        self.open('')

    def open_next_unclassified_failure(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.find_element(*self._resultset_locator).is_displayed())
        self.selenium.find_element(*self._resultset_locator).send_keys("n")

    def open_logviewer(self):
        self.selenium.find_element(*self._job_details_locator)
        self.selenium.find_element(*self._logviewer_locator).click()

    def select_logviewer(self):
        self.selenium.find_element(*self._logviewer_locator).click()

class LogviewerPage(Base):

    _page_title = 'Log for'
    _job_header_locator = (By.CSS_SELECTOR, '.job-header')


    def __init__(self, testsetup):
        Base.__init__(self, testsetup)

        if self.selenium.title != self._page_title:
            for handle in self.selenium.window_handles:
                self.selenium.switch_to_window(handle)
                WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        else:
            raise Exception('Page has not loaded')

    @property
    def is_job_status_visible(self):
        return self.is_element_visible(*self._job_header_locator)
