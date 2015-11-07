# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.common.exceptions import NoSuchElementException


class Page(object):

    _url = None

    def __init__(self, base_url, selenium):
        self.base_url = base_url
        self.selenium = selenium
        self.timeout = 10

    def open(self):
        self.selenium.get(self.url)
        return self.wait_for_page_to_load()

    @property
    def url(self):
        if self._url is not None:
            return self._url.format(base_url=self.base_url)
        return self.base_url

    def wait_for_page_to_load(self):
        return self

    def is_element_visible(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException):
            return False
