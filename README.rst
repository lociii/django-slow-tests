django-slowtests
========================

.. image:: https://travis-ci.org/realpython/django-slow-tests.svg?branch=master
    :target: https://travis-ci.org/realpython/django-slow-tests

.. image:: https://coveralls.io/repos/realpython/django-slow-tests/badge.svg?branch=master
  :target: https://coveralls.io/r/realpython/django-slow-tests?branch=master

.. image:: https://img.shields.io/pypi/v/django-slowtests.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

Welcome!
--------

Welcome to the documentation for django-slowtests!

.. list-table:: Test matrix
   :header-rows: 1

   * - Django release
     - Python 3.8
     - Python 3.9
     - Python 3.10
     - Python 3.11
     - Python 3.12
   * - 4.2
     - x
     - x
     - x
     - x
     - x
   * - 5.0
     -
     -
     - x
     - x
     - x
   * - 5.1
     -
     -
     - x
     - x
     - x

This library is compatible with `freezegun` and `time-machine` to travel time.

Settings
--------

NUM_SLOW_TESTS
~~~~~~~~~~~~~~

Set the count of slow tests to report.  
Set to `None` to list all slow tests.

| Type: int
| Default: 10

SLOW_TEST_THRESHOLD_MS
~~~~~~~~~~~~~~~~~~~~~~

Threshold in milliseconds on when a test case is considered to be slow.

| Type: int
| Default: 200

ALWAYS_GENERATE_SLOW_REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flag if a slow test report should always be generated.
If set to `False`, the report is only generated if requested with the `--slowreport` flag.

| Type: boolean
| Default: True

Instructions
-------------

1. Install::

    $ pip install django-slowtests

2. Use the provided test runner::

    TEST_RUNNER = 'django_slowtests.testrunner.DiscoverSlowestTestsRunner'

3. Run test suite::

    Adjust optional settings, see above

4. Run test suite::

    $ python manage.py test


4.1. Save report to file::
    $ python manage.py test --slowreportpath report.json

4.2. Generating full reports to file::
    In some situations, you may need to generate full tests reports. To do so,
    set NUM_SLOW_TESTS to None in your settings and run the following command:
    $ python manage.py test --slowreportpath report.json


5. Sample output::


    $ python manage.py test
    Creating test database for alias 'default'...
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.413s

    OK
    Destroying test database for alias 'default'...

    Ten slowest tests:
    0.3597s test_detail_view_with_a_future_poll (polls.tests.PollIndexDetailTests)
    0.0284s test_detail_view_with_a_past_poll (polls.tests.PollIndexDetailTests)
    0.0068s test_index_view_with_a_future_poll (polls.tests.PollViewTests)
    0.0047s test_index_view_with_a_past_poll (polls.tests.PollViewTests)
    0.0045s test_index_view_with_two_past_polls (polls.tests.PollViewTests)
    0.0041s test_index_view_with_future_poll_and_past_poll (polls.tests.PollViewTests)
    0.0036s test_index_view_with_no_polls (polls.tests.PollViewTests)
    0.0003s test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
    0.0002s test_was_published_recently_with_recent_poll (polls.tests.PollMethodTests)
    0.0002s test_was_published_recently_with_old_poll (polls.tests.PollMethodTests)



Running the Tests
------------------------------------

You can run the tests via::

    $ python setup.py test

or::

    $ make test

or::

    $ make all

or::

    $ python runtests.py


Known Issues
------------



License
-------

This code is distributed under the terms of the MIT license. See the `LICENSE` file.
