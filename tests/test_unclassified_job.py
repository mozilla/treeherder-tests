# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.resultset import ResultsetPage


class TestUnclassifiedJobs:

    @pytest.mark.nondestructive
    def test_unclassified_failure(self, base_url, selenium):
        # Open resultset page and search for next unclassified failure
        resultset_page = ResultsetPage(base_url, selenium).open()
        Assert.greater_equal(resultset_page.unclassified_failure_count, 1)
        resultset_page.open_next_unclassified_failure()
        teststatus = resultset_page.job_result_status
        assert teststatus in ['busted', 'testfailed', 'exception']

    @pytest.mark.nondestructive
    def test_open_unclassified_failure_log(self, base_url, selenium):
        # Open the job log and verify there is content
        resultset_page = ResultsetPage(base_url, selenium).open()
        Assert.greater_equal(resultset_page.unclassified_failure_count, 1)
        resultset_page.open_next_unclassified_failure()
        logviewer_page = resultset_page.open_logviewer()
        Assert.true(logviewer_page.is_job_status_visible)
