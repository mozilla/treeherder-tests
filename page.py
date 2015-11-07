# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class Page(object):
    """
    Base class for all Pages
    """

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def is_the_current_page(self):
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.title)
        Assert.equal(self.selenium.title, self._page_title,
                     'Expected page title: %s. Actual page title: %s' % (self._page_title, self.selenium.title))
        return True

    @property
    def current_page_url(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return(self.selenium.current_url)

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        return self.selenium.title

    def is_element_visible(self, *locator):
        try:
            self.selenium.find_element(*locator).is_displayed()
            return True
        except (ElementNotVisibleException, NoSuchElementException):
            # this will return a snapshot, which takes time.
            return False

    def open(self, url_fragment):
        self.selenium.get(self.base_url + url_fragment)
        self.selenium.maximize_window()
