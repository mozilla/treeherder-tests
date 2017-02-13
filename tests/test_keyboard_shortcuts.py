# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random

from pages.treeherder import TreeherderPage


def test_next_job_shortcut(base_url, selenium):
    """Open Treeherder, verify shortcut: 'Right Arrow' opens next job.
    Open Treeherder page, select random job and get the keyword name, select next job
    using Right Arrow shortcut, verify job keywords match."""

    page = TreeherderPage(selenium, base_url).open()
    all_jobs = page.all_jobs

    # Check number of jobs
    num_of_jobs = len(all_jobs) - 1
    random_index = random.randint(0, num_of_jobs)

    # Select random job and job next to it
    all_jobs[random_index].click()
    assumed_job_keyword = page.job_details.job_keyword_name

    page.select_next_job()

    assert page.job_details.job_keyword_name == assumed_job_keyword


def test_previous_job_shortcut(base_url, selenium):
    """Open Treeherder, verify shortcut: 'Left Arrow' opens previous job.
    Open Treeherder page, select random job and get the keyword name, select previous job
    using Left Arrow shortcut, verify job keywords match."""

    page = TreeherderPage(selenium, base_url).open()
    all_jobs = page.all_jobs

    # Check number of jobs
    number_of_jobs = len(all_jobs)
    random_index = random.randint(1, number_of_jobs - 1)

    # Select random job and job to the left
    all_jobs[random_index].click()
    assumed_job_keyword = page.job_details.job_keyword_name
    page.select_previous_job()

    assert page.job_details.job_keyword_name == assumed_job_keyword
