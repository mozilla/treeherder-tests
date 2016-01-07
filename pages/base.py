# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page, PageRegion


class Base(Page):

    @property
    def header(self):
        return Base.Header(self)

    class Header(PageRegion):

        _dropdown_menu_switch_page_locator = (By.CSS_SELECTOR, '.open ul > li a')
        _dropdown_menu_locator = (By.ID, 'th-logo')

        def switch_page_using_dropdown(self):
            self.selenium.find_element(*self._dropdown_menu_locator).click()
            self.selenium.find_element(*self._dropdown_menu_switch_page_locator).click()
