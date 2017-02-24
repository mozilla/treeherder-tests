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
    all_jobs = page.all_jobs[:-1]

    # Check number of jobs
    random_index = random.randint(0, len(all_jobs))
    jobs = all_jobs[random_index:(random_index + 2)]

    # Select random job and job next to it
    jobs[0].click()
    assert jobs[0].selected
    assert not jobs[1].selected

    page.select_next_job()

    assert jobs[1].selected
    assert not jobs[0].selected


def test_previous_job_shortcut(base_url, selenium):
    """Open Treeherder, verify shortcut: 'Left Arrow' opens previous job.
    Open Treeherder page, select random job and get the keyword name, select previous job
    using Left Arrow shortcut, verify job keywords match."""

    page = TreeherderPage(selenium, base_url).open()
    all_jobs = page.all_jobs[:-1]

    # Check number of jobs
    random_index = random.randint(0, len(all_jobs))
    jobs = all_jobs[random_index:(random_index + 2)]

    # Select random job and previous job
    jobs[1].click()
    assert jobs[1].selected
    assert not jobs[0].selected

    page.select_previous_job()

    assert jobs[0].selected
    assert not jobs[1].selected
