# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.resultset import ResultsetPage


class TestLogin():

    @pytest.mark.nondestructive
    def test_that_a_new_user_can_login(self, base_url, selenium, new_user):
        resultset_page = ResultsetPage(base_url, selenium).open()
        assert not resultset_page.is_user_logged_in

        resultset_page.login(new_user)
        assert resultset_page.is_user_logged_in
