# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.treeherder import TreeherderPage


@pytest.mark.nondestructive
def test_expand_job_count(base_url, selenium):
    page = TreeherderPage(selenium, base_url).open()
    assert len(page.result_sets[0].jobs) >= 1

    job_total = len(page.result_sets[0].jobs)
    page.result_sets[0].expand_group_count()

    new_job_total = len(page.result_sets[0].jobs)
    assert new_job_total > job_total
