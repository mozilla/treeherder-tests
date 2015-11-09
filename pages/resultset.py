# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class ResultsetPage(Base):

    _job_details_actionbar_locator = (By.ID, 'job-details-actionbar')
    _job_result_status_locator = (By.CSS_SELECTOR, '#result-status-pane > div:nth-child(1) > span')
    _logviewer_button_locator = (By.ID, 'logviewer-btn')
    _resultset_locator = (By.CSS_SELECTOR, 'div.row.result-set')
    _result_status_locator = (By.ID, 'job-details-panel')
    _unclassified_failure_count_locator = (By.ID, 'unclassified-failure-count')

    @property
    def job_result_status(self):
        return self.selenium.find_element(*self._job_result_status_locator).text

    @property
    def unclassified_failure_count(self):
        return int(self.selenium.find_element(*self._unclassified_failure_count_locator).text)

    def go_to_page(self):
        self.open('')

    def open_next_unclassified_failure(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.find_element(*self._resultset_locator).is_displayed())
        self.selenium.find_element(*self._resultset_locator).send_keys("n")

    def open_logviewer(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.find_element(*self._job_details_actionbar_locator).is_displayed())
        self.selenium.find_element(*self._resultset_locator).send_keys("l")


class LogviewerPage(Base):

    _page_title = 'Log for'
    _job_header_locator = (By.CSS_SELECTOR, 'div.job-header')

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
