#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from selenium.webdriver.common.by import By

from pages.resultset import ResultsetPage
from pages.resultset import JobLogPage


class TestUnclassifiedJobs:

    @pytest.mark.nondestructive
    def test_unclassified_job_failure(self, mozwebqa):
        # Open resultset page and search for next unclassified failure
        resultset_page = ResultsetPage(mozwebqa)
        resultset_page.go_to_page()
        resultset_page.open_next_failed_job()

        teststatus = resultset_page.job_resultpane_status
        Assert.equal(teststatus, 'testfailed')

    @pytest.mark.nondestructive
    def test_open_failed_job_log(self, mozwebqa):
        # Open the job log and verify there is content
        resultset_page = ResultsetPage(mozwebqa)
        resultset_page.go_to_page()
        resultset_page.open_next_failed_job()
        joblog_page = resultset_page.open_job_log()
        joblog_page = JobLogPage(mozwebqa)

        Assert.true(joblog_page.is_job_status_visible)