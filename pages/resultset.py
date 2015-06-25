#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class ResultsetPage(Base):

    _job_log_locator = (By.CSS_SELECTOR, '.logviewer-icon')
    _job_resultpane_status = (By.CSS_SELECTOR, '#result-status-pane > div:nth-child(1) > span:nth-child(2)')
    _log_viewer_locator = (By.CSS_SELECTOR, 'logviewer-icon')
    _resultset_locator = (By.CSS_SELECTOR, 'div.row.result-set')
    _result_status_locator = (By.ID, 'result-status-pane')

    @property
    def job_resultpane_status(self):
        self.selenium.find_element(*self._result_status_locator)
        return self.selenium.find_element(*self._job_resultpane_status).text

    def go_to_page(self):
        self.open('')

    def open_next_failed_job(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.find_element(*self._resultset_locator).is_displayed())
        self.selenium.find_element(*self._resultset_locator).send_keys("n")

    def open_job_log(self):
        self.selenium.find_element(*self._result_status_locator)
        self.selenium.find_element(*self._job_log_locator).click()

    def select_log_viewer(self):
        self.selenium.find_element(*self._log_viewer_locator).click()

class JobLogPage(Base):

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
