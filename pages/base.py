#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class Base(Page):

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    def _go_to_page(self, path_to_page):
        self.selenium.maximize_window()
        self.selenium.get(self.base_url + path_to_page)
        self.is_the_current_page
