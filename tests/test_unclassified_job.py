#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from selenium.webdriver.common.by import By

from pages.resultset import ResultsetPage
from pages.resultset import LogviewerPage


class TestUnclassifiedJobs:

    @pytest.mark.nondestructive
    def test_unclassified_failure(self, mozwebqa):
        # Open resultset page and search for next unclassified failure
        resultset_page = ResultsetPage(mozwebqa)
        resultset_page.go_to_page()
        Assert.greater_equal(resultset_page.unclassified_failure_count, 1)

        resultset_page.open_next_unclassified_failure()

        teststatus = resultset_page.job_result_status
        jobstatus = ["busted", "testfailed", "exception"]

        for i in range(len(jobstatus)):
            'assert jobstatus in teststatus'

    @pytest.mark.nondestructive
    def test_open_unclassified_failure_log(self, mozwebqa):
        # Open the job log and verify there is content
        resultset_page = ResultsetPage(mozwebqa)
        resultset_page.go_to_page()
        Assert.greater_equal(resultset_page.unclassified_failure_count, 1)

        resultset_page.open_next_unclassified_failure()
        logviewer_page = resultset_page.open_logviewer()
        logviewer_page = LogviewerPage(mozwebqa)

        Assert.true(logviewer_page.is_job_status_visible)
